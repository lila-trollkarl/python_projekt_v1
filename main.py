import string
from itertools import permutations, combinations

# Hej välkommen
# bla bla bla
# hehe
# okej

################################
dictionary = "SAOL13_AND_14.txt"
valid_words = set()
with open (dictionary, "r") as f:
    for line in f:
         word = line.strip().lower()
         valid_words.add(word)
        

best_word = ""
max_points = 0

board = [
    ['.', 'e', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', 'c', '.', '.', '.'],
    ['.', '.', '.', 'b', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', 'a', '.']
]

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
###################################

# creates a new hand with the letters from a given row
def new_hand(hand, row):
    # copy to avoid just making a reference
    new_hand = hand.copy()
    for c in row:
        if c != '.':
            new_hand.append(c)
    return new_hand

##########################################################
##########################################################
# rotate board clockwise and counter clockwise
##########################################################
##########################################################
def rotate_clock(board):
    return list(list(row) for row in zip(*board[::-1]))
def rotate_counter(board):
    return (list(list(row) for row in zip(*board)))[::-1]
##########################################################
##########################################################

# Checks how much points a word is worth with regards to only letters
def word_points(word):
    points = 0
    for letter in word:
        points += wordfeud_points[letter]

    return points

# mycket bättre för minnet
def gen_words_hand(hand2):
    words = set()
    for i in range(2, len(hand2)+1):
        for combo in combinations(hand2, i):
            for perms in permutations(combo):
                word = ''.join(perms)
                if word in valid_words:
                    # words.add(word)
                    yield word


#####################################
#####################################
#####################################
# Helper functions to is_valid()
#####################################
#####################################
#####################################

# Sätter igop ett ord och en rad
def merge_row(word_row, row):
    return [x if (x != '.' or y == '.') else y for x, y in zip(word_row, row)]


# Generar alla möjliga rader såhära: 
# ["o", "r", "d", "e", "t", ".", ".", ".", "."]
# [".", "o", "r", "d", "e", "t", ".", ".", "."]
# [".", ".", "o", "r", "d", "e", "t", ".", "."]
# [".", ".", ".", "o", "r", "d", "e", "t", "."]
# [".", ".", ".", ".", "o", "r", "d", "e", "t"]
def generate_possibilities(word, row):
    possibilities = []
    for i in range(len(row)-len(word)+1):
            new_word = ['.']*i + list(word) + ['.']*(len(row)-len(word)-i)
            possibilities.append(new_word)
    return possibilities

# Kollar så att en possibility och en rad inte har överlappande bokstäver som inte är samma bokstav
def check_no_letter_collision(possibility, row):
    for x, y in zip(possibility, row): 
            if (y != '.' and x != '.') and x != y:
                return False
    return True

# kollar så att en bokstav som finns i mereged row men inte i row måste komma från handen
def check_letters_ok(row, merged_row, hand):
    hand_copy = hand.copy()
    for old, new in zip(row, merged_row):
        if old == '.' and new != '.':
            if new in hand_copy:
                hand_copy.remove(new)
            else:
                return False
    return True

# kollar så att ordet inte ligger precis brevid en annan bokstav i radenbrädet
def check_next_letter(possibility, word, row):
    start_of_word = possibility.index(word[0])
    end_of_word = start_of_word + len(word) - 1
    if (start_of_word >= 1 and row[start_of_word - 1] != '.') or (end_of_word < len(row) - 1 and row[end_of_word + 1] != '.'):
        return False
    return True

#####################################
#####################################
#####################################
#####################################


def is_valid(word, row, hand): 
    for possibility in generate_possibilities(word, row):
        merged_row = merge_row(possibility, row)
        
        if not check_no_letter_collision(possibility, row):
            continue

        if not check_letters_ok(row, merged_row, hand):
            continue

        if not check_next_letter(possibility, word, row):
            continue

        # print(possibility)
        # print(row)
        # print(merged_row)
        print(word)
        print(word_points(word))

        return True
    return False



##########################################################
###### Test grejer #######################################
##########################################################
# print(is_valid("hepp", ['.','.','.','.'], ["h", "j", "p", "e"]))
#
# # 1️⃣ Simple fit — should be True
# print(is_valid("aba", ['.','.','a','.','.'], ["a","a","b"]))  # True
#
# # 2️⃣ Not enough letters — should be False
# print(is_valid("aaa", ['.','.','a','.','.'], ["a","a","b"]))  # True
#
# # 3️⃣ Wrong letter conflict — should be False
# print(is_valid("dog", ['.','c','.','.','.'], ["d","o","g"]))  # False
#
# # 4️⃣ Adjacent letter conflict — should be False
# print(is_valid("he", ['a','.','.','.','.'], ["h","e"]))  # True
#
# # 5️⃣ Perfect match with row letters — should be True
# print(is_valid("cab", ['c','.','a','.','b'], ["x","y","z"]))  # False
#
# # 6️⃣ Empty row, exact hand letters — should be True
# print(is_valid("hepp", ['.','.','.','.'], ["h","e","p","p"]))  # True
#
# # 7️⃣ Empty row, missing one letter — should be False
# print(is_valid("hepp", ['.','.','.','.'], ["h","e","p"]))  # False
##########################################################
##########################################################
##########################################################
# row = ['.', '.', '.', 'k', 'a', 't', 't', '.', '.', '.']
hand = ['e', 'r', 's', 'a', 'l', 'o', 'p']

# hand2 = new_hand(hand, row)
#
# for word in gen_possible_words(permutate_hand(hand2)):
#     is_valid(word, row, hand)
print("hej")

for row in board:
    
    hand2 = new_hand(hand, row)

    for word in gen_words_hand(hand2):
        if is_valid(word, row, hand) and word_points(word) > max_points:
            best_word = word
            max_points = word_points(word)

print(best_word)            
print(max_points)
