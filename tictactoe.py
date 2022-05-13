import tkinter as tk

window = tk.Tk()
window.title("Tic Tac Toe")
window.geometry("450x550")
window.resizable(0, 0)
window.iconbitmap("icon.ico")
cells = {}
buttons = {}
xcell = {}
ocell = {}
sign = True

'''-------------------------------Functions for commands-------------------------------'''
def clear() :
    global sign
    for row in range(3) :
        for column in range(3) :
            buttons[row, column]['text'] = ""
    xcell.clear()
    ocell.clear()
    sign = True

def pop_up(result) :
    top = tk.Toplevel(window)
    top.grab_set()
    top.geometry("300x150")
    top.resizable(0, 0)
    top.title("Tic Tac Toe")
    label = tk.Label(top, text=result, font=("Arial", 20))
    label.place(anchor=tk.CENTER, relx=0.5, rely=0.4)
    button = tk.Button(top, text="OK", font=("Arial", 10), width=10, height=1, command=lambda : [top.destroy(), clear(), top.grab_release()])
    button.place(anchor=tk.CENTER, relx=0.5, rely=0.8)
    top.protocol("WM_DELETE_WINDOW", lambda : [top.destroy(), top.grab_release(), clear()])

def check_winner() :
    check1 = 0
    check2 = 0
    #row check
    for row in range(3) :
        for column in range(3) :
            if (row, column) in xcell :
                check1 += 1
            if (row, column) in ocell :
                check2 += 1
        if check1 == 3 :
            return "X wins!"
        elif check2 == 3 :
            return "O wins!"
        check1 = 0
        check2 = 0
    #column check
    for column in range(3) :
        for row in range(3) :
            if (row, column) in xcell :
                check1 += 1
            if (row, column) in ocell :
                check2 += 1
        if check1 == 3 :
            return "X wins!"
        elif check2 == 3 :
            return "O wins!"
        check1 = 0
        check2 = 0
    #diagonal check
    if (0, 0) in xcell and (1, 1) in xcell and (2, 2) in xcell :
        return "X wins!"
    elif (0, 0) in ocell and (1, 1) in ocell and (2, 2) in ocell :
        return "O wins!"
    elif (0, 2) in xcell and (1, 1) in xcell and (2, 0) in xcell :
        return "X wins!"
    elif (0, 2) in ocell and (1, 1) in ocell and (2, 0) in ocell :
        return "O wins!"
    #check tie
    if len(xcell) + len(ocell) == 9 :
        return "Draw!"

def on_click(row, column):
    global sign

    check = (row, column)
    if check in xcell or check in ocell :
        return
    if sign == True :
        buttons[(row, column)]['text'] = "X"
        xcell[(row, column)] = buttons[(row, column)]
        sign = not sign
    elif sign == False :
        buttons[(row, column)]['text'] = "O"
        ocell[(row, column)] = buttons[(row, column)]
        sign = not sign

    winner = check_winner()
    if winner != None :
        pop_up(winner)

'''-------------------------------Creating grid and buttons-------------------------------'''
for row in range (3):
    for column in range (3):
        cell = tk.Frame(window, width=150, height=150, padx=3, pady=3, highlightbackground="black", highlightthickness=1)
        cell.grid(row=row, column=column)
        cells[(row, column)] = cell

for row in range (3):
    for column in range (3):
        button = tk.Button(cells[(row, column)], text="", font=("Arial", 40), command=lambda row=row, column=column: on_click(row, column))
        button.place(anchor=tk.CENTER, relx=0.5, rely=0.5, relheight=1, relwidth=1)
        buttons[(row, column)] = button

clear_button = tk.Button(window, text="Clear", font=("Arial", 20), command=lambda: clear())
clear_button.place(anchor=tk.CENTER, relx=0.5, rely=0.9, relheight=0.1, relwidth=0.5)

window.mainloop()