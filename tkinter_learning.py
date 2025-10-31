import tkinter as tk
import main as m

def retrieve(my_entry,result_label, grid_entries):
    result_label.config(text="")

    hand = list(my_entry.get().strip().lower())
    print(hand)
    if (len(hand) > 7 or not all(letter.isalpha() or letter == "*" for letter in hand)):
        result_label.config(text="Måste vara 7 bokstäver långt!")
    
    board = []
    for row in grid_entries:
        board_row = []
        for entry in row:
            value = entry.get().strip().lower()
            board_row.append(value if value else '.')
        board.append(board_row)
    print(board)

    m.init(hand, board)


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