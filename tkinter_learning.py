import tkinter as tk
import json
import main as m

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
        json.dump(board, file)

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
for row in range(15):
    row_entries = []
    for col in range(15):
        grid_entry = tk.Entry(grid_frame, width=2)
        grid_entry.grid(row=row, column=col, padx=1, pady=1)
        row_entries.append(grid_entry)
    grid_entries.append(row_entries)
    

button = tk.Button(frame, text = "Skicka", command = lambda: retrieve(my_entry, result_label, grid_entries))
button.pack()

root.mainloop()