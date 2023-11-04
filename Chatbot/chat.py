import random
import json
import torch
import tkinter as tk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from NeuralNetwork import NN
from Nltk import tokenize,bgfw
import pyttsx3


def speak(text, rate=150):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)  
    engine.say(text)
    engine.runAndWait()
    
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"F:\Chatbot\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def load_data(file_path):
    data = torch.load(file_path)
    return data

def process_input(model, sentence, all_words, tags):
    sentence = tokenize(sentence)
    X = bgfw(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    return tag, prob

def generate_response(model, intents, sentence, all_words, tags):
    tag, prob = process_input(model, sentence, all_words, tags)

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                response = random.choice(intent['responses'])
                return response
    else:
        return "I do not understand..."

def send_message():
    user_input = entry_2.get()
    entry_2.delete(0, tk.END)
    
    if user_input == "quit":
        window.quit()
        return
    
    response = generate_response(model, intents, user_input, all_words, tags)
    entry_1.config(state=tk.NORMAL)
    entry_1.insert(tk.END, f"You: {user_input}\n")
    entry_1.insert(tk.END, f"{bot_name}: {response}\n")
    entry_1.config(state=tk.DISABLED)
    entry_1.see(tk.END)
    window.update()
    speak(response, rate=150)
    
def trigger_send_message(event):
    send_message()

# Main GUI setup
window = Tk()
img = PhotoImage(file="C:\\Users\\HP\\Downloads\\atom (6).png")
window.iconphoto(True, img)
window.geometry("1147x600")
window.title('Proton')
window.configure(bg = "#FFFFFF")



canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 1147,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    573.0,
    300.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    710.5,
    254.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#000000",
    fg="#ffffff",
    highlightthickness=0,
    font=('verdana', 13, 'bold')
)
entry_1.place(
    x=377.0,
    y=98.0,
    width=667.0,
    height=311.0
)


entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    661.5,
    518.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#000000",
    fg="#ffffff",
    highlightthickness=0,
    font=('verdana', 13, 'bold')
)
entry_2.place(
    x=384.0,
    y=494.0,
    width=555.0,
    height=46.0,
    
)
entry_2.bind("<Return>", trigger_send_message)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=send_message    ,
    relief="flat"
)
button_1.place(
    x=995.0,
    y=473.0,
    width=98.0,
    height=92.0
)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('F:\Chatbot\pytorch-chatbot\intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = load_data(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NN(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Proton"
speak('hello my name is proton',rate=150)

window.resizable(False, False)
window.mainloop()
