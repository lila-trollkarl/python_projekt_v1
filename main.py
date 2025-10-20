from itertools import permutations, combinations
from collections import Counter

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
position = (None, None)
direction = "hehe" 
#



multiplier_board = [
['TB', '.', '.', '.', 'TO', '.', '.', 'DB', '.', '.', 'TO', '.', '.', '.', 'TB'],
['.', 'DB', '.', '.', '.', 'TB', '.', '.', '.', 'TB', '.', '.', '.', 'DB', '.'],
['.', '.', 'DO', '.', '.', '.', 'DB', '.', 'DB', '.', '.', '.', 'DO', '.', '.'],
['.', '.', '.', 'TB', '.', '.', '.', 'DO', '.', '.', '.', 'TB', '.', '.', '.'],
['TO', '.', '.', '.', 'DO', '.', 'DB', '.', 'DB', '.', 'DO', '.', '.', '.', 'TO'],
['.', 'TB', '.', '.', '.', 'TB', '.', '.', '.', 'TB', '.', '.', '.', 'TB', '.'],
['.', '.', 'DB', '.', 'DB', '.', '.', '.', '.', '.', 'DB', '.', 'DB', '.', '.'],
['DB', '.', '.', 'DO', '.', '.', '.', '.', '.', '.', '.', 'DO', '.', '.', 'DB'],
['.', '.', 'DB', '.', 'DB', '.', '.', '.', '.', '.', 'DB', '.', 'DB', '.', '.'],
['.', 'TB', '.', '.', '.', 'TB', '.', '.', '.', 'TB', '.', '.', '.', 'TB', '.'],
['TO', '.', '.', '.', 'DO', '.', 'DB', '.', 'DB', '.', 'DO', '.', '.', '.', 'TO'],
['.', '.', '.', 'TB', '.', '.', '.', 'DO', '.', '.', '.', 'TB', '.', '.', '.'],
['.', '.', 'DO', '.', '.', '.', 'DB', '.', 'DB', '.', '.', '.', 'DO', '.', '.'],
['.', 'DB', '.', '.', '.', 'TB', '.', '.', '.', 'TB', '.', '.', '.', 'DB', '.'],
['TB', '.', '.', '.', 'TO', '.', '.', 'DB', '.', '.', 'TO', '.', '.', '.', 'TB'],
] 
board = [
['.', '.', 'j', 'a', 'k', 't', 'e', 'r', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', 'i', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', 'n', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', 'g', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', 'l', 'y', 's', 't', 'r', 'a', 'd', 'e'],
['.', '.', '.', '.', '.', '.', '.', 'a', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', 't', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', 's', 'l', 'e', 'm', 'm', 'a', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
] 
# hand = ['a', 't', 'e', 'r', 'n', 'o', 'l']
hand = ["b", "e", "t", "a", "s", "e", "s"]
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
##########################################################

# Checks how much points a word is worth with regards to only letters
def individual_word_points(word):
    points = 0
    for letter in word:
        points += wordfeud_points[letter]

    return points

# # mycket bättre för minnet
# def gen_words_hand(hand2):
#     words = set()
#     for i in range(2, len(hand2)+1):
#         for combo in combinations(hand2, i):
#             for perms in permutations(combo):
#                 word = ''.join(perms)
#                 if word in valid_words:
#                     # words.add(word)
#                     yield word


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


def can_make_word(word, letters):
    need = Counter(word)
    return not (need - Counter(letters))



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

# Check if word in row is next to letters inother rows, and if it is, make sure that new text is also a word
def check_other_rows(merged_row, row, ind):
    new_letters = [x if x != '.' and y == '.' else y for x, y in zip(merged_row, row)]
    temp_board = [row.copy() for row in board]
    temp_board[ind] = new_letters
    for i in range(len(new_letters)):
        if new_letters[i] != '.':
            col = [row[i] for row in temp_board]
            new_texts = ''.join(col).split('.')
            for word in new_texts:
                if len(word) >= 2:
                    if word not in valid_words:
                        return False
    return True


# Kollar så att ordet inte bara ligger helt själv
def check_loneliness(possibility, row, ind):

# ------ kollar så att minst en bokstav överlappar i possibility och row --- #
    for x, y in zip(possibility, row):
        if x != '.' and y != '.':
            return False
    
# ------ kollar så att det finns minst en bokstav över eller under --------- #
    for index, c in enumerate(possibility):
        if c == '.':
            continue
        over = board[ind - 1][index] if ind >= 1 else '.' 
        under = board[ind + 1][index] if ind < len(board)-1 else '.'

        if over != '.' or under != '.':
            return False
    

    return True



#####################################
#####################################
#####################################
#####################################


def is_valid(word, row, ind): 
    for possibility in generate_possibilities(word, row):
        merged_row = merge_row(possibility, row)
        
        if not check_no_letter_collision(possibility, row):
            continue

        if not check_letters_ok(row, merged_row, hand):
            continue

        if not check_next_letter(possibility, word, row):
            continue
        
        if check_loneliness(possibility, row, ind):
            continue

        if not check_other_rows(merged_row, row, ind):
            continue 

        # print(possibility)
        # print(row)
        # print(merged_row)
        # print(word)
        # print(individual_word_points(word))
        r = ind
        c = possibility.index(word[0])

        return True, (r, c)
    return False, (0, 0)



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

print("hej")

def main_function(grid, dir):
    global max_points
    global best_word
    global position
    global direction
    for ind, row in enumerate(grid):
        
        letters = hand + [c for c in row if c != '.']

        for word in valid_words:
            if len(word) < 2 or len(word) > len(letters):
                continue
            if can_make_word(word, letters):
                valid, (r, c) = is_valid(word, row, ind)
                if valid:
                    
                    if individual_word_points(word) > max_points:

                        best_word = word
                        max_points = individual_word_points(word)
                        position = (r, c) if dir == "right" else (c, r)
                        direction = dir

    
main_function(board, "right")
transpose_board = [list(row) for row in zip(*board)]
main_function(transpose_board, "down")





print(best_word)            
print(max_points)
print(position)
print(direction)
