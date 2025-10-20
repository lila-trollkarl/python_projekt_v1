
import string
from itertools import permutations
import copy
from collections import Counter

# ---------- läs in ordlistan ----------
dictionary = "SAOL13_AND_14.txt"
valid_words = set()
with open(dictionary, "r", encoding="utf-8") as f:
    for line in f:
        word = line.strip().lower()
        if word:
            valid_words.add(word)

# ---------- poängsättning ----------
wordfeud_points = {
    'a': 1,'b': 4,'c': 8,'d': 1,'e': 1,'f': 3,'g': 2,'h': 3,'i': 1,'j': 7,
    'k': 3,'l': 2,'m': 3,'n': 1,'o': 2,'p': 4,'q': 10,'r': 1,'s': 1,'t': 1,
    'u': 4,'v': 3,'w': 10,'x': 8,'y': 7,'z': 10,'å': 4,'ä': 4,'ö': 4
}
def word_points(word):
    return sum(wordfeud_points.get(c, 0) for c in word)

# ---------- board & hand (exempel) ----------
board = [
    ['.', 'e', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', 'c', '.', '.', '.'],
    ['.', '.', '.', 'b', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', 'a', '.']
]
hand = ["b", "e", "t", "a", "s", "e", "s"]

# ---------- hjälp: lägg till bokstäver från raden i handen ----------
def new_hand(hand, row):
    new = list(hand)  # shallow copy is enough for list of str
    for c in row:
        if c != '.':
            new.append(c)
    return new

# ---------- generera placements av ett ord i en rad ----------
def generate_possibilities(word, row_len):
    # returnerar list av start-index där ordet kan placeras i raden
    for start in range(0, row_len - len(word) + 1):
        yield start

# ---------- merge_row förenklad ----------
def merge_row_at(possibility_start, word, row):
    # returnerar den merge:ade raden (lista)
    new_row = list(row)
    for i, ch in enumerate(word):
        new_row[possibility_start + i] = ch
    return new_row

# ---------- kollisonskontroller ----------
def check_no_letter_collision(start, word, row):
    # om row redan har bokstav, måste den matcha
    for i, ch in enumerate(word):
        rch = row[start + i]
        if rch != '.' and rch != ch:
            return False
    return True

def check_letters_ok(start, word, row, hand):
    # nya bokstäver som behövs av ordet ska finnas i hand (multimängd)
    needed = []
    for i, ch in enumerate(word):
        if row[start + i] == '.':
            needed.append(ch)
    needed_count = Counter(needed)
    hand_count = Counter(hand)
    for k, v in needed_count.items():
        if hand_count[k] < v:
            return False
    return True

def check_next_letter(start, word, row):
    # ingen bokstav direkt före eller efter ordet
    if start - 1 >= 0 and row[start - 1] != '.':
        return False
    end = start + len(word) - 1
    if end + 1 < len(row) and row[end + 1] != '.':
        return False
    return True

def check_other_rows(merged_row, full_board, row_index):
    # kolla varje kolumn där vi lagt bokstäver — om en kolumns "vertikala" text
    # bildar ord >=2 ska den finnas i ordlistan
    temp = [list(r) for r in full_board]
    temp[row_index] = merged_row
    ncols = len(merged_row)
    for c in range(ncols):
        col = ''.join(temp[r][c] for r in range(len(temp)))
        for candidate in col.split('.'):
            if len(candidate) >= 2 and candidate not in valid_words:
                return False
    return True

# ---------- is_valid (nu tar den hand2 — med radens bokstäver inkluderade) ----------
def is_valid(word, row, hand2, full_board, row_index):
    row_len = len(row)
    for start in generate_possibilities(word, row_len):
        if not check_no_letter_collision(start, word, row):
            continue
        if not check_letters_ok(start, word, row, hand2):
            continue
        if not check_next_letter(start, word, row):
            continue
        merged = merge_row_at(start, word, row)
        if not check_other_rows(merged, full_board, row_index):
            continue
        return True
    return False

# ---------- effektivitetsförbättring: kolla ordlistan istället för att permutera -->
#  loopa genom ordlistan och testa ord som kan bildas av hand2 + radens fasta bokstäver.
def words_from_hand_and_row(hand2, row, min_len=2):
    # skapar en Counter med bokstäver som finns tillgängliga (hand + fasta bokstäver i raden)
    base_count = Counter(hand2)
    # obs: vi kan behöva ta bort fasta bokstäver som redan finns i raden när vi räknar "behövs"
    for w in valid_words:
        if len(w) < min_len:
            continue
        # snabb pruning: om w innehåller bokstäver som inte finns i hand2 och inte i row, skip
        need = Counter(w)
        # räkna bort bokstäver som redan finns i raden på passande positioner är mer komplicerat,
        # men vi gör enklare pruning: om totalt behov av en bokstav > (antal i hand2 + antal av samma bokstav i row) -> skip
        row_count = Counter(ch for ch in row if ch != '.')
        ok = True
        for ch, cnt in need.items():
            if cnt > base_count.get(ch, 0) + row_count.get(ch, 0):
                ok = False
                break
        if ok:
            yield w

# ---------- huvudloop (rekomenation: använda words_from_hand_and_row för prestanda) ----------
best_word = ""
max_points = 0

for _ in range(2):  # kör horisontellt och sedan transponerat (vertikalt)
    for ind, row in enumerate(board):
        hand2 = new_hand(hand, row)          # korrekt: hand + rads bokstäver
        # snabbvariant: iterera ordlistan och testa is_valid istället för att permutera
        for word in words_from_hand_and_row(hand2, row):
            if is_valid(word, row, hand2, board, ind):
                pts = word_points(word)
                if pts > max_points:
                    best_word = word
                    max_points = pts
    # transponera brädet för att pröva andra riktningen
    board = [list(r) for r in zip(*board)]

print("Bästa ord:", best_word)
print("Poäng:", max_points)
