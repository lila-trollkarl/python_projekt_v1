import pygame
import random
import string

# Hej välkommen
# bla bla bla
# hehe
# okej
bla = 1


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

hand = random.sample(letters, 7)

# print(letters)
# print(board)
# print(hand)

# creates a new hand with the letters from a given row
def new_hand(hand, row):
    new_hand = hand
    for c in row:
        if c is not ' ':
            new_hand += c
    return new_hand

# rotate board clockwise and counter clockwise
def rotate_clock(board):
    return list(list(row) for row in zip(*board[::-1]))
def rotate_counter(board):
    return (list(list(row) for row in zip(*board)))[::-1]

# takes a hand and generates all possible permutaions in a list
def permutate_hand(hand):

    return

# checks which perms are an actual word and returns a list with those words
def gen_possible_words(perms):
    return

def is_valid(word, row):
    return

a = [[1,2,3],[4,5,6],[7,8,9]]
print(a)
r = rotate_counter(a)
print(r)
