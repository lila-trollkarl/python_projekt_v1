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

# print(letters)
# print(board)
# print(hand)

# creates a new hand with the letters from a given row
def new_hand(hand, row):
    # copy to avoid just making a reference
    new_hand = hand.copy()
    for c in row:
        if c != ' ':
            new_hand += c
    return new_hand

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
    with open (dictionary, "r") as f:
        # set because its faster to search through
        valid_words = set(line.strip() for line in f)
    for w in perms:
        if w in valid_words:
            words.add(w)
    return words

def is_valid(word, row):
    possibilities = [] 
    for i in range(len(row)-len(word)+1):
        new_word = ['.']*i + list(word) + ['.']*(len(row)-len(word)-i)
        possibilities.append(new_word)

    for w in possibilities:
        for x, y in zip(w, row):
            if y != '.' and x != '.' and x != y:
                return False
    return True


# print(gen_possible_words(permutate_hand(hand)))
# print(gen_possible_words(permutate_hand(hand)))'
a = ['.']*10
b = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(is_valid("hej", b))

word = "horseshoe"
l =["h", "o", ".", ".", "s", ".", "h", ".", "."]


print(is_valid(word, l))
