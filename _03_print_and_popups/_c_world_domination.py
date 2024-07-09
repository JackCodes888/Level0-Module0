from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Ask the user if they know how to write code.
    can_you_code =simpledialog.askstring(title='I have I question,',prompt='do you how to code? ')
    # 2. If they say "yes", tell them they will rule the world in a message box pop-up.
    if can_you_code == 'yes' :
        messagebox.showinfo(message='you will rule the world')
    else:
        simpledialog.askstring(title='sign up for The League',prompt='write you name below to sign up for The League ')
    # 3. Otherwise, tell them to sign up for classes at The League in an error box pop-up.
    
    # Run the window's .mainloop() method
    window.mainloop()
