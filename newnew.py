import tkinter as tk
import time
import threading 
import random 

class typespeedgui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Typing Speed Application")
        self.root.geometry("800x600+200+10")
        self.root.state("zoomed")
        self.root.configure(bg = "yellow")
        
        self.texts = open("texts.txt", "r").read().split("\n")

        self.frame = tk.Frame(self.root)

        self.sample_label = tk.Label(self.frame,text="Welcome to Typing Speed Application",font=("Times New Roman", 24, "italic bold"), bg="powder blue", fg="red", width=50)
        self.sample_label.grid(row=1,column=0,columnspan=2,padx=0,pady=10)

        self.sample_label = tk.Label(self.frame,text=random.choice(self.texts),font=("Time New Roman", 18),bg="powder blue", width=100)
        self.sample_label.grid(row=2,column=0,columnspan=2,padx=0,pady=10)

        self.input_entry = tk.Entry(self.frame, width=40, font=("Times New Roman", 20), bg="white", bd=10)
        self.input_entry.grid(row=3,column=0,columnspan=2,padx=0,pady=10)
        self.input_entry.bind("<KeyPress>", self.start)
        self.input_entry.focus_set()

        self.speed_label = tk.Label(self.frame, text ="Your Typing Speed: \n0.00 CPS\n0.00 CPM\n0.00 WPS\n0.00 WPS",font = ("Time New Roman", 18),bg="powder blue", fg="green")
        self.speed_label.grid(row=4,column=0,columnspan=2,padx=0,pady=10)

        self.reset_button = tk.Button(self.frame, text="Reset", comman=self.reset)
        self.reset_button.grid(row=5,column=0,columnspan=2,padx=0,pady=10)

        self.frame.pack(expand=True)

        self.counter = 0
        self.running = False

        self.root.mainloop()

    def start(self, event):
        if not self.running:
            if not event.keycode in [16,17,18]:
                self.running = True
                t = threading.Thread(target=self.time_thread)
                t.start()
        if not self.sample_label.cget('text').startswith(self.input_entry.get()):
            self.input_entry.config(fg="red")
        else:
            self.input_entry.config(fg="black")
        if self.input_entry.get() == self.sample_label.cget('text')[:-1]:
            self.running = False
            self.input_entry.config(fg="green")

    def time_thread(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1
            cps = len(self.input_entry.get()) / self.counter
            cpm = cps * 60
            wps = len(self.input_entry.get().split(" ")) / self.counter
            wpm = wps * 60
            self.speed_label.config(text=f"Speed: \n{cps:.2f} CPS\n{cpm:.2f} CPM\n{wps:.2f} WPS\n {wpm:.2f} WPM")

    def reset(self):
        self.running = False
        self.counter = 0
        self.speed_label.config(text="Speed: \n0.00 CPS\n0.00 CPM\n0.00 WPS\n0.00 WPS") 
        self.sample_label.config(text=random.choice(self.texts))
        if(self.input_entry.get() == self.input_label["texts"]):
            print("Matched")
        else:
            print("Not Matched")
        self.input_entry.delete(0, tk.END)

typespeedgui()