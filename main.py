import random
import string
from itertools import permutations

# Hej välkommen
# bla bla bla
# hehe
# okej
bla = 1

dictionary = "SAOL13_AND_14.txt"

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
hand = ["a", "b", "n", "c", "w", "a", "d"]

wordfeud_points_sv = {
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
# def new_hand(hand, row):
#     # copy to avoid just making a reference
#     new_hand = hand.copy()
#     for c in row:
#         if c != ' ':
#             new_hand += c
#     return new_hand

# rotate board clockwise and counter clockwise
def rotate_clock(board):
    return list(list(row) for row in zip(*board[::-1]))
def rotate_counter(board):
    return (list(list(row) for row in zip(*board)))[::-1]

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


# Exprimeterade lite....
def is_valid(word, row):
    possibilities = []
    fits = True
    for i in range(len(row)-len(word)+1):
        new_word = ['.']*i + list(word) + ['.']*(len(row)-len(word)-i)
        possibilities.append(new_word)

    for w in possibilities:
        fits = True
        for x, y in zip(w, row):
            if y != '.' and x != '.' and x != y:
                fits = False
                break
        if fits == True:
            return True
    return False


# print(gen_possible_words(permutate_hand(hand)))
# print(gen_possible_words(permutate_hand(hand)))'
# a = ['.']*10
ls = ["b", ".", "x", ".", ".", ".", ".", "a", ".", "a"]
# b = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# print(is_valid("hej", b))
#
word_list = gen_possible_words(permutate_hand(hand))
print(word_list)
g = []
for word in word_list:
    if is_valid(word, ls):
        g.append(word)
        print(word)

