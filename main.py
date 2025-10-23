#### BEHLVER LÄGGA TILL"""""transpose_multiplier_board

# så att valid_words inte returnerar på en gång utan kolla alla giltiga positioner
#
# att move score endast ska ta hänsyn till dem nya bokstäverna som har lagts och inte "ordet", kanske genom, att skicka in en lista av tuples i formen(bokstav, position)




from itertools import permutations, combinations
from collections import Counter

# Hej välkommen
# bla bla bla
# hehe
# okej

################################
dictionary = "SAOL13_AND_14.txt"
valid_words = set()
with open (dictionary, "r", encoding="utf-8") as f:
    for line in f:
         word = line.strip().lower()
         valid_words.add(word)
        

best_word = ""
max_points = 0
position = (None, None)
direction = "hehe" 
best_move = []
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
[".", ".", ".", ".", ".", ".", ".", "r", "e", ".", "s", "t", "e", "g", "e"],
[".", ".", ".", ".", "p", "a", "n", "i", "k", ".", "t", ".", ".", ".", "."],
[".", ".", ".", ".", "c", ".", ".", "n", ".", ".", "e", ".", ".", ".", "."],
[".", ".", ".", ".", ".", ".", ".", "g", ".", ".", "n", ".", ".", ".", "."],
[".", ".", ".", ".", ".", ".", ".", "f", "y", "s", "i", "s", "k", ".", "."],
[".", ".", ".", ".", ".", ".", ".", "i", ".", ".", "g", ".", ".", ".", "."],
[".", ".", ".", ".", ".", ".", ".", "n", ".", ".", ".", ".", ".", ".", "."],
[".", ".", ".", ".", ".", ".", ".", "g", "l", "ö", "m", "s", "k", ".", "."],
[".", ".", ".", ".", ".", ".", ".", "e", ".", ".", ".", ".", ".", ".", "."],
[".", ".", ".", ".", ".", ".", ".", "r", ".", ".", ".", ".", ".", ".", "."],
[".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
[".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
[".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
[".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
[".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
]

def word_list(board):
    words = []

    # finds left to right words
    for row in board:
        for word in ''.join(row).split('.'):
            if len(word) >=2 and word in valid_words:
                words.append(word)

    # finds words vertically
    for col in [list(row) for row in zip(*board)]:
        for word in ''.join(col).split('.'):
            if len(word) >=2 and word in valid_words:
                words.append(word)
    return words

board_words= word_list(board)

hand = ["s", "l", "a", "a", "t", "a", "t"]
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
def word_score(word):
    points = 0
    for letter in word:
        points += wordfeud_points[letter]

    return points


def move_score(move, word, dir):
    new_board = [row[:] for row in board]
    total_points = 0
    multiplier = 1

    for letter, (row, col) in move:
        # if dir == "right":
        new_board[row][col] = letter
        if multiplier_board[row][col] != '.':
            if multiplier_board[row][col] == "TO":
                multiplier *= 3
            if multiplier_board[row][col] == "DO":
                multiplier *= 2
            if multiplier_board[row][col] == "TB":
                total_points += wordfeud_points[letter]*2
            if multiplier_board[row][col] == "DB":
                total_points += wordfeud_points[letter]
        # elif dir == "down":
        #     new_board[col][row] = letter
        #     if multiplier_board[col][row] != '.':
        #         if multiplier_board[col][row] == "TO":
        #             multiplier *= 3
        #         if multiplier_board[col][row] == "DO":
        #             multiplier *= 2
        #         if multiplier_board[col][row] == "TB":
        #             total_points += wordfeud_points[letter]*2
        #         if multiplier_board[col][row] == "DB":
        #             total_points += wordfeud_points[letter]

    # ---- skapar en lista med alla ord i det nya brädet ---#
    new_board_word_list = word_list(new_board)
    new_words = []
    # ---- kollar vilka ord som är helt nya --- #
    for w in new_board_word_list:
        if w not in board_words:
            new_words.append(w)

    ws = word_score(word)
    total_points += multiplier * ws
    for w in new_words:
        total_points += word_score(w)
    return total_points-ws # account for couting it twice






# -------------------- helper functions ----------------------------------- # 

# Sätter igop ett ord och en rad
def merge_row(word_row, row):
    return [x if (x != '.' or y == '.') else y for x, y in zip(word_row, row)]


def can_make_word(word, letters):
    need = Counter(word)
    return not (need - Counter(letters))



# ------------------- Generates "possibilitys" in this way -------------#

# ["o", "r", encoding="utf-8", "d", "e", "t", ".", ".", ".", "."]
# [".", "o", "r", encoding="utf-8", "d", "e", "t", ".", ".", "."]
# [".", ".", "o", "r", encoding="utf-8", "d", "e", "t", ".", "."]
# [".", ".", ".", "o", "r", encoding="utf-8", "d", "e", "t", "."]
# [".", ".", ".", ".", "o", "r", encoding="utf-8", "d", "e", "t"]

# -----------------------------------------------------------------------# 
def generate_possibilities(word, row):
    possibilities = []
    for i in range(len(row)-len(word)+1):
            new_word = ['.']*i + list(word) + ['.']*(len(row)-len(word)-i)
            possibilities.append(new_word)
    return possibilities

# ---------- Checks that 2 overlapping letters dont differ ---------------#
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
        # print(word_score(word))
        r = ind
        c = possibility.index(word[0])
        
        # ------------ make a move tuple ------------- #
        

        move = [(l, (ind, i)) for i, l in enumerate(merged_row)]
        # remove letters that are in row
        move = [m for m, r in zip(move, row) if m[0] != r]



        return True, move
    return False, (None)
    


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

def main_function(grid, dir, m_board):
    global max_points
    global best_word
    global position
    global direction
    global best_move

    for ind, row in enumerate(grid):
        
        print("~"*50)
        print(" "*17, end="")
        print(f"looking at row {ind}") if dir == "right" else print(f"looking at col {ind}")
        print("~"*50) 

        letters = hand + [c for c in row if c != '.']

        for word in valid_words:
            if len(word) < 2 or len(word) > len(letters):
                continue
            if can_make_word(word, letters):
                valid, move = is_valid(word, row, ind)
                if valid:
                    score = move_score(move, word, dir)
                    print(f"{word} {score}")
                    if score > max_points:

                        best_word = word
                        max_points = score
                        best_move = move
                        first_letter, position = best_move[0]
                        direction = dir

    
main_function(board, "right", multiplier_board)
board = [list(row) for row in zip(*board)]
multiplier_board = [list(row) for row in zip(*multiplier_board)]
main_function(board, "down", multiplier_board)
board = [list(row) for row in zip(*board)]


print("==="*20)
print(best_word)            
print(max_points)
print(position)
print(direction)
print(best_move)

# Print the board with new letters highlighted and color based on multiplier
if best_move:
    board_to_print = [row.copy() for row in board]
    color_map = {
        'TB': '\033[91m',  # Red
        'TO': '\033[93m',  # Yellow
        'DB': '\033[94m',  # Blue
        'DO': '\033[92m',  # Green
        '.': '',
    }
    reset = '\033[0m'
    # Print color legend
    print("Legend: "
          f"{color_map['TB']}[X]{reset}=TB "
          f"{color_map['TO']}[X]{reset}=TO "
          f"{color_map['DB']}[X]{reset}=DB "
          f"{color_map['DO']}[X]{reset}=DO "
          f"[X]=normal")
    for letter, (row_idx, col_idx) in best_move:
        # Swap coordinates if the move is vertical
        if direction == "down":
            row_idx, col_idx = col_idx, row_idx
        if board[row_idx][col_idx] == '.':
            mult = multiplier_board[row_idx][col_idx]
            color = color_map.get(mult, '')
            board_to_print[row_idx][col_idx] = f'{color}[{letter}]{reset}'
        else:
            board_to_print[row_idx][col_idx] = letter
    print("\nBoard with best move (new letters in brackets, colored by multiplier):")
    for r, row in enumerate(board_to_print):
        row_str = ''
        for c, cell in enumerate(row):
            if isinstance(cell, str) and cell.startswith('\033'):
                row_str += f'{cell:>6}'
            else:
                row_str += f'{cell:>3}'
        print(row_str)
else:
    print("No valid move found.")