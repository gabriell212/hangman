from tkinter import *
from PIL import Image, ImageTk

import csv
import random

word = ""
mistakes = 0
letters = []
usedLetters = ""

# Below goes all the functions for the widgets and mechanical purposes

# This function starts the game
def start_game():
    global word
    get_random_word()

    for i in range(len(word)):
        letters.append(" ")

    update_letter_label()
    draw_gallow()

# This function restarts the game
def restart_game():
    global mistakes
    global usedLetters
    global letters

    mistakes = 0
    usedLetters = ""
    letters=[]
    playerInput.set("")

    # Deletes all canvas drawing
    draw.delete("all")

    gameoverFrame.pack_forget()
    inputFrame.pack(side="top")
    start_game()

# This function will take a random word from the csv file
def get_random_word():
    global word
    with open("C:/Users/User/Desktop/Aplicatii C#/LogicSphere Studio/Hangman/english_words.csv", "r") as csvfile:
        csvreader = csv.reader(csvfile)
        word = random.choice(list(csvreader))[0]

# This function will update the label where the letters are displayed
def update_letter_label():
    global letters
    
    for label in answerFrame.pack_slaves():
        label.destroy()
    for i, ch in enumerate(letters):
        foregroundColor = "#fff"
        if len(ch) == 2:
            foregroundColor = "#f00" if ch[1] == "-" else "lime"
            letters[i] = ch[0]
        Label(answerFrame, text=letters[i], background="#111", foreground=foregroundColor, font="Verdana 16 underline").pack(side="left")

# This function draws the gallow without the body
def draw_gallow():
    drawingCoordinates = [(90, 240), (50, 280), (130, 280), (90, 240), (90, 20), (210, 20), (210, 40), (210, 20), (130, 20), (90, 60)]

    for i, coordinateSet in enumerate(drawingCoordinates):
        if i == len(drawingCoordinates)-1:
            break
        draw.create_line(coordinateSet[0], coordinateSet[1], drawingCoordinates[i+1][0], drawingCoordinates[i+1][1], fill="#fff", width=2)

# This function updates the human according to the number of mistakes
def update_human():
    global mistakes

    drawingCoordinates = [[(210, 80), (210, 160)], [(210, 160), (190, 220)], [(210, 160), (230, 220)], [(210, 90), (190, 140)], [(210, 90), (230, 140)]]

    if mistakes == 1:
        draw.create_oval(190, 40, 230, 80, outline="#fff", width=2)
    else:
        draw.create_line(drawingCoordinates[mistakes-2][0][0], drawingCoordinates[mistakes-2][0][1], drawingCoordinates[mistakes-2][1][0], drawingCoordinates[mistakes-2][1][1], fill="#fff", width=2)

# This function handles the situations where the game is over
def handle_gameover(state):
    global letters
    global word

    if state == "failure":
        for i in range(len(letters)):
            if letters[i] == " ":
                letters[i] = word[i] + "-"
    
    if state == "success":
        for i in range(len(letters)):
            letters[i] += "+"

    inputFrame.pack_forget()
    lblGameover["text"] = "You won!" if state == "success" else "You lost!"
    lblGameover["foreground"] = "lime" if state == "success" else "#f00"
    btnGameover["background"] = "lime" if state == "success" else "#f00"
    gameoverFrame.pack(side="top")

    update_letter_label()

# This function tracks and verifies whatever the user is writing in the Entry
def validate_input(passedInput):
    validChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    inputContent = playerInput.get()
    if inputContent == "":
        return

    if inputContent[len(inputContent)-1] not in validChars:
        if len(inputContent) > 1:
            playerInput.set(playerInput.get()[-1])
        else:
            playerInput.set("")

# This function handles the input and evaluates it accordingly
def handle_input():
    global word
    global mistakes
    global letters
    global usedLetters

    # If the game is lost anything written in the textBox is ignored
    if mistakes == 6 or str(letters) == word:
        return

    inputContent = playerInput.get()
    playerInput.set("")

    # Treat the case where the input is not a single letter or a word of the same length of the chosen word
    if len(inputContent) > 1 and len(inputContent) != len(word):
        return
    
    # Treat the case where the letter has already been used
    if len(inputContent) == 1:
        if inputContent in usedLetters:
            return
        else:
            usedLetters += inputContent
    
    # Treat the case if the player wants to guess the whole word
    if len(inputContent) == len(word):
        if inputContent == word:
            for i in range(len(letters)):
                letters[i] = word[i]
            handle_gameover("success")
        else:
            while mistakes < 6:
                mistakes+=1
                update_human()
            handle_gameover("failure")

    # Treat the case where the guess is only one letter
    if len(inputContent) == 1:
        if inputContent in word:
            for i, ch in enumerate(word):
                if inputContent == ch:
                    letters[i] = ch
                    update_letter_label()
            if "".join(letters) == word:
                handle_gameover("success")
        else:
            mistakes += 1

            # Game lost
            if mistakes == 6:
                handle_gameover("failure")
            update_human()

    playerInput.set("")

# Window
window = Tk()
window.title("Hangman")
window.configure(bg="black")

# Set a custom window icon
icon_path = "C:/Users/User/Desktop/Aplicatii C#/LogicSphere Studio/Hangman/Icon.ico"
window.iconbitmap(icon_path)

# Restrict the user from resizing the window
window.resizable(width=False, height=False)

# Get window information
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()

# Predefined window size
window_width = 420
window_height = 500

# Calculate x and y coordinates for the window
x = (ws - window_width) // 2
y = (hs - window_height) // 2

# Place the window in the center of the screen
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Mainframe
mainframe = Frame(window, background="#111", padx=16, pady=16)
mainframe.pack(expand = True, fill = "both")

# Title of a game designed in a label
Label(mainframe, text="Hangman", background="#111", foreground="#fff", font="Verdana 24").pack(side="top", fill="x")

# Using canvas to create the drawing of the gallow
draw = Canvas(mainframe, width=300, height=300, background="#111", borderwidth=0, highlightthickness=0)
draw.pack(side="top", pady=10)

# Create an answer frame
answerFrame = Frame(mainframe, background="#111")
answerFrame.pack(side="top", expand=True, pady=(0, 16))

# Create an input widget for letter guessing
inputFrame = Frame(mainframe, background="#111")
inputFrame.pack(side="top", expand=True)

# Create the textBox and button for the letter input
playerInput = StringVar()

playerInput.trace("w", lambda *args: validate_input(playerInput))

Entry(inputFrame, textvariable=playerInput, font="Verdana 24", width=5).pack(side="left", padx=10)
Button(inputFrame, text="Guess", font="Verdana 16", command=handle_input).pack(side="left")

# Game over frame
gameoverFrame = Frame(mainframe, background="#111")
lblGameover = Label(gameoverFrame, text="", background="#111", foreground="#fff", font="Verdana 24")
lblGameover.pack(side="left")
btnGameover = Button(gameoverFrame, text="Restart", font="Verdana 16", command=restart_game, background="#f00")
btnGameover.pack(side="left", padx=5)

# Hide the frame until the game is over
gameoverFrame.pack_forget()

# Company's logo
originalImage = Image.open("C:/Users/User/Desktop/Aplicatii C#/LogicSphere Studio/Hangman/LogicSphere Studio logo.png")
resizedImage = originalImage.resize((100, 100))
logoImage = ImageTk.PhotoImage(resizedImage)
lblLogoImage = Label(mainframe, image=logoImage, background="#111")
lblLogoImage.place(x=-20, y=-20)

# Start the game
start_game()

# Run the GUI
window.mainloop()
