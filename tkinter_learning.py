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
    for letter, (r,c) in move['move']:
        board[r][c] = letter
    with open("working_board.json", "w") as file:
        write_2d_array("working_board.json", board)
    root.destroy()

def show_move(move, board):
    # clear screen
    for ridx,r in enumerate(board):
        for cidx,c in enumerate(r):
            if c != grid_entries[ridx][cidx].get():
                grid_entries[ridx][cidx].delete(0,tk.END)
                grid_entries[ridx][cidx].config(bg="gray11")

    coords = move['move']
    for letter, (r,c) in coords:
        grid_entries[r][c].insert(0,letter)
        grid_entries[r][c].config(bg="green")

    points = move['points']
    points_label.config(text=f"Poäng för draget: {points}")
    points_label.pack()

def show_next(best_moves, idx, board):
    if idx[0] > -len(best_moves):
        idx[0] -= 1
        show_move(best_moves[idx[0]], board)

def show_previous(best_moves, idx, board):
    if idx[0] < -1:
        print("he,lo")
        idx[0] += 1
        show_move(best_moves[idx[0]], board)

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

    move_idx = [-1]
    show_move(best_moves[-1], board)

    next = tk.Button(frame, text="Nästa drag", command= lambda: show_next(best_moves, move_idx, board))
    previous = tk.Button(frame, text="Tidigare drag", command= lambda: show_previous(best_moves, move_idx, board))
    next.pack()
    previous.pack()

    approve_button = tk.Button(frame, text="Godkänn drag", command= lambda: approve_move(best_moves[move_idx[0]], board))
    approve_button.pack()


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

points_label = tk.Label(frame, text="")
points_label.pack()

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