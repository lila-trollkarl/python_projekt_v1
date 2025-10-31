import tkinter as tk
import json
import main as m

def write_2d_array(filename, array):
    with open(filename, "w", encoding="utf-8") as f:
        f.write('[\n')
        for i, row in enumerate(array):
            if i < len(array) - 1:
                f.write('  ' + json.dumps(row, ensure_ascii=False) + ',\n')
            else:
                f.write('  ' + json.dumps(row, ensure_ascii=False) + '\n')
        f.write(']\n')

def extract_board(grid_entries):
    board = []
    for row in grid_entries:
        board_row = []
        for entry in row:
            value = entry.get().strip().lower()
            board_row.append(value if value else '.')
        board.append(board_row)
    return board

def approve_move(move, board):
    for letter, (r,c) in move:
        board[r][c] = letter
    with open("working_board.json", "w") as file:
        write_2d_array("working_board.json", board)

def retrieve(my_entry,result_label, grid_entries):
    result_label.config(text="")
    root.update()

    hand = list(my_entry.get().strip().lower())
    print(hand)
    if (len(hand) > 7 or not all(letter.isalpha() or letter == "*" for letter in hand)):
        return result_label.config(text="Måste vara 7 bokstäver långt!")
    
    board = extract_board(grid_entries)

    button.pack_forget()
    label = tk.Label(frame, text="Tänker väldigt mycket...")
    label.pack()
    root.update()

    best_moves = m.init(hand, board)
    label.destroy()
    for letter, (r,c) in best_moves[-1]['move']:
        grid_entries[r][c].insert(0,letter)
        grid_entries[r][c].config(bg="green")

    approve_move(best_moves[-1]['move'], board)



######################################################
######################################################
################ funktioner ^ ########################
################ huvud program -> ####################
######################################################

with open("working_board.json", "r", encoding="utf-8") as file:
    board = json.load(file)

root = tk.Tk()

root.title("Hello World")

root.geometry("600x800")

frame = tk.Frame(root)
frame.pack()

label = tk.Label(frame, text="Din hand:")
label.pack()
my_entry = tk.Entry(frame)
my_entry.pack()

result_label = tk.Label(frame, text="")
result_label.pack()


grid_frame = tk.Frame(root)
grid_frame.pack()

grid_entries = []
for row_idx,row in enumerate(board):
    row_entries = []
    for col_idx,col in enumerate(row):
        grid_entry = tk.Entry(grid_frame, width=2)
        grid_entry.grid(row=row_idx, column=col_idx, padx=1, pady=1)
        grid_entry.insert(0,col if col != '.' else '')
        row_entries.append(grid_entry)
    grid_entries.append(row_entries)
    

button = tk.Button(frame, text = "Skicka", command = lambda: retrieve(my_entry, result_label, grid_entries))
button.pack()

root.mainloop()