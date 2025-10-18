import string
from itertools import permutations

# Hej välkommen
# bla bla bla
# hehe
# okej

################################
dictionary = "SAOL13_AND_14.txt"

best_word = ""
max_points = 0

letters = list(string.ascii_lowercase) + ['å','ä','ö']

board = [
    [' ', 'e', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', 'c', ' ', ' ', ' '],
    [' ', ' ', ' ', 'b', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', 'a', ' ']
]

# hand = random.sample(letters, 7)

wordfeud_points = {
    'a': 1,
    'b': 4,
    'c': 8,
    'd': 1,
    'e': 1,
    'f': 3,
    'g': 2,
    'h': 3,
    'i': 1,
    'j': 7,
    'k': 3,
    'l': 2,
    'm': 3,
    'n': 1,
    'o': 2,
    'p': 4,
    'q': 10,
    'r': 1,
    's': 1,
    't': 1,
    'u': 4,
    'v': 3,
    'w': 10,
    'x': 8,
    'y': 7,
    'z': 10,
    'å': 4,
    'ä': 4,
    'ö': 4
}

# print(letters)
# print(board)
# print(hand)

# creates a new hand with the letters from a given row
def new_hand(hand, row):
    # copy to avoid just making a reference
    new_hand = hand.copy()
    for c in row:
        if c != '.':
            new_hand.append(c)
    return new_hand

# rotate board clockwise and counter clockwise
def rotate_clock(board):
    return list(list(row) for row in zip(*board[::-1]))
def rotate_counter(board):
    return (list(list(row) for row in zip(*board)))[::-1]

# Checks how much points a word is worth with regards to only letters
def word_points(word):
    points = 0
    for letter in word:
        points += wordfeud_points[letter]

    return points


# takes a hand and generates all possible permutaions in a list
def permutate_hand(hand):
    perms = []
    for i in range(2, len(hand)+1):
        for w in permutations(hand, i):
            perms.append(''.join(w))
    return perms

# checks which perms are an actual word and returns a list with those words
def gen_possible_words(perms):
    # set for removing duplicates
    words = set()
    with open (dictionary, "r", encoding="utf-8") as f:
        # set because its faster to search through
        valid_words = set(line.strip() for line in f)
    for w in perms:
        if w in valid_words:
            words.add(w)
    return words

# Sätter igop ett ord och en rad
def merge_row(word_row, row):
    return [x if (x != '.' or y == '.') else y for x, y in zip(word_row, row)]


# Helper functions to is_valid()

def generate_possibilities(word, row):
    possibilities = []
    for i in range(len(row)-len(word)+1):
            new_word = ['.']*i + list(word) + ['.']*(len(row)-len(word)-i)
            possibilities.append(new_word)
    return possibilities

def check_no_letter_collision(possibility, row):
    for x, y in zip(possibility, row): 
            if (y != '.' and x != '.') and x != y:
                return False
    return True

def check_letters_ok(row, merged_row, hand):
    hand_copy = hand.copy()
    for old, new in zip(row, merged_row):
        if old == '.' and new != '.':
            if new in hand_copy:
                hand_copy.remove(new)
            else:
                return False
    return True

def check_next_letter(possibility, word, row):
    start_of_word = possibility.index(word[0])
    end_of_word = start_of_word + len(word) - 1
    if (start_of_word >= 1 and row[start_of_word - 1] != '.') or (end_of_word < len(row) - 1 and row[end_of_word + 1] != '.'):
        return False
    return True



def is_valid(word, row, hand): 
    for possibility in generate_possibilities(word, row):
        merged_row = merge_row(possibility, row)
        
        if not check_no_letter_collision(possibility, row):
            continue

        if not check_letters_ok(row, merged_row, hand):
            continue

        if not check_next_letter(possibility, word, row):
            continue

        print(possibility)
        print(row)
        print(merged_row)

        return True
    return False

print(is_valid("hepp", ['.','.','.','.'], ["h", "j", "p", "e"]))
