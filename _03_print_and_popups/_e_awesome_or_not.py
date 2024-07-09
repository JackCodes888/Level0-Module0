from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    a = random.randint(0, 3)
    # 2. Print your variable to the console
    print(a)
    # 3. Get the user to enter something that they think is awesome
    awsome =simpledialog.askstring(title='',prompt='What do you think is awsome')
    # 4. If your variable is  0
    if a == 0 :
        # -- tell the user whatever they entered is awesome!
        messagebox.showinfo(message='That is very awsome')
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
    if a == 1 :
        # -- tell the user whatever they entered is awesome!
        messagebox.showinfo(message='That is very ok')
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
    if a == 2 :
        # -- tell the user whatever they entered is awesome!
        messagebox.showinfo(message='That is very bor bor')
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
    if a == 3 :
        # -- tell the user whatever they entered is awesome!
        messagebox.showinfo(message='you have to help put this chair down')
