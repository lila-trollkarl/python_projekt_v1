import main

hand = ["a", "f", "g", "h", "s", "c", "b"]
row = [".", ".", ".", "h", ".", ".", "s", ".", ".", "."]
new_hand = main.new_hand(hand, row)

perms = main.permutate_hand(new_hand)
word_list = main.gen_possible_words(perms)

# [a,b,c,d,e,f,g] + [h,i,j,k]

for letters in merge_row:
    if letter in row and not in hand:
        ls = row.index(letter) == merge_row.index(letter)

