import tkinter as tk
from tkinter import messagebox

def check_winner():
    global winner
    for combination in [[0,1,2],[3,4,5],[6,7,8],
                        [0,3,6],[1,4,7],[2,5,8],
                        [0,4,8],[2,4,6]
                        ]: #possible combinations
        if buttons[combination[0]]["text"] == buttons[combination[1]]["text"] == buttons[combination[2]]["text"] != "":
            buttons[combination[0]].config(bg="green")
            buttons[combination[1]].config(bg="green")
            buttons[combination[2]].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe",f"Player{[buttons[combination[0]]['text']]} Wins!!")
            winner = True
            root.quit()
            return

    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
        winner = True
        root.quit()

def click_button(index):
    if buttons[index]["text"] == "" and not winner: #avoid overwriting
        buttons[index]["text"] = current_player
        check_winner()
        if not winner:
            toggle_player() #to change player

def toggle_player():
    global current_player
    current_player = 'O' if current_player == 'X' else 'X'
    label.config(text=f"{current_player}'s turn")

root = tk.Tk()
root.title('Tic-Tac-Toe')

winner = False
current_player = 'X'

buttons = [tk.Button(root, text="",font=("bold",25), width=6,
                     height=2, command=lambda i=i: click_button(i))
                     for i in range(9)
          ]
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3) # for creating board

label = tk.Label(root, text=f"{current_player}'s turn", font=("bold", 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()
    
