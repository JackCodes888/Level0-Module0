from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    qeustion1 =simpledialog.askstring(title='Question #1', prompt='what is my name')
    #      // 3.  Use an if statement to check if their answer is correct
    if qeustion1 == 'Jack':
    #      // 4.  if the user's answer was correct, add one to their score
        score += 1
    else:
        score -= 1
        messagebox.showinfo(message='incorrect')
    qeustion2 =simpledialog.askstring(title='Question #2', prompt='what is my brothers name')
    #      // 3.  Use an if statement to check if their answer is correct
    if qeustion2 == 'Blake':
    #      // 4.  if the user's answer was correct, add one to their score
        score += 1
    else:
        score -= 1
        messagebox.showinfo(message='icorrect')

    qeustion3 =simpledialog.askstring(title='Question #3', prompt='what is my sisters name')
    #      // 3.  Use an if statement to check if their answer is correct
    if qeustion3 == 'You do not have a sister':
    #      // 4.  if the user's answer was correct, add one to their score
        score += 1
    else:
        score -= 1
        messagebox.showinfo(message='icorrect')
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
 
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    messagebox.showinfo(message=score)
    # Run the window's .mainloop() method
    window.mainloop()
