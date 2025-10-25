import tkinter as tk

# below are different tiers of difficulty that ranges from easy, moderate. and advanced. Correspondingly going from 1 digit to 4 digit numbers

PROBLEMS = {
    1: [  
        (3, '+', 4), (8, '-', 5), (6, '+', 2), (9, '-', 3), (5, '+', 1),
        (7, '-', 6), (2, '+', 3), (9, '-', 4), (1, '+', 8), (4, '+', 5)
    ],
    2: [  
        (12, '+', 15), (34, '-', 12), (56, '+', 23), (78, '-', 44), (19, '+', 61),
        (25, '-', 14), (83, '+', 16), (90, '-', 45), (67, '+', 20), (72, '-', 31)
    ],
    3: [  
        (1200, '+', 3500), (7890, '-', 2345), (4567, '+', 3210), (9800, '-', 7890), (6400, '+', 2500),
        (7200, '-', 3100), (5100, '+', 4200), (9000, '-', 6500), (8400, '+', 1000), (9999, '-', 8888)
    ]
}

def displayMenu():
    # this is for the difficulty selection
    clear_window() 
    tk.Label(root, text="Select Difficulty Level", font=("Arial", 16, "bold")).pack(pady=10)
    tk.Button(root, text="Easy (1-digit)", width=20, command=lambda: start_quiz(1)).pack(pady=5)
    tk.Button(root, text="Moderate (2-digit)", width=20, command=lambda: start_quiz(2)).pack(pady=5)
    tk.Button(root, text="Advanced (4-digit)", width=20, command=lambda: start_quiz(3)).pack(pady=5)

def displayProblem():
   # proceeds to next problem
    global correct_ans, attempt # I had to look this part up since I needed the same variables that are outside this function

    num1, op, num2 = PROBLEMS[difficulty][question_no]
    correct_ans = num1 + num2 if op == '+' else num1 - num2
    attempt = 1 # resets the attempts to 1

# updates the question text and clears the answer box
    lbl_question.config(text=f"Question {question_no + 1}: {num1} {op} {num2} = ?")
    entry_answer.delete(0, tk.END)
    lbl_feedback.config(text="") 

def isCorrect(user_ans):
    # checks if the answer is correct
    try:
        return int(user_ans) == correct_ans
    except ValueError:
        return False

def submit_answer():
    # this part handles the answer submission
    global question_no, score, attempt

    ans = entry_answer.get().strip() # the user gets 10 points if the answer  is right  the first time.  5 points  if the  answer is gotten the 2nd try . and 0 points if its wrong on both tries
    if isCorrect(ans):
        lbl_feedback.config(text="✅ Correct!", fg="green")
        score += 10 if attempt == 1 else 5 # here is the scoring mentioned earlier
        root.after(1000, next_question)
    else:
        if attempt == 1:
            lbl_feedback.config(text="❌ Incorrect. Try again!", fg="red")
            attempt += 1 
        else:
            lbl_feedback.config(text=f"❌ Wrong again! Correct was {correct_ans}.", fg="red")
            root.after(1500, next_question)

def next_question():
    # this moves to the next question/finishes the test
    global question_no
    question_no += 1
    if question_no < 10:
        displayProblem() # displays the number of questions left
    else:
        displayResults() # quiz is done

def displayResults():
    # shows the final results and grade
    clear_window()
    tk.Label(root, text="Quiz Complete!", font=("Arial", 16, "bold")).pack(pady=10)
    tk.Label(root, text=f"Final Score: {score}/100", font=("Arial", 14)).pack(pady=5)

# below are the scores and grades you can get
    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"

#displays the grade and it gives the user to either play again or quit
    tk.Label(root, text=f"Grade: {grade}", font=("Arial", 14, "bold")).pack(pady=5)
    tk.Button(root, text="Play Again", command=displayMenu, width=15).pack(pady=10)
    tk.Button(root, text="Exit", command=root.quit, width=15).pack()

def start_quiz(level):
    # starts the quiz state
    global difficulty, question_no, score
    difficulty = level
    question_no = 0
    score = 0
    clear_window()

    tk.Label(root, text="Arithmetic Quiz", font=("Arial", 16, "bold")).pack(pady=10)
    global lbl_question, entry_answer, lbl_feedback

    lbl_question = tk.Label(root, text="", font=("Arial", 14))
    lbl_question.pack(pady=5)

    entry_answer = tk.Entry(root, font=("Arial", 14), justify="center")
    entry_answer.pack(pady=5)

    tk.Button(root, text="Submit", command=submit_answer, width=12).pack(pady=5)
    lbl_feedback = tk.Label(root, text="", font=("Arial", 12))
    lbl_feedback.pack(pady=10)

    displayProblem()

def clear_window():
    
    for widget in root.winfo_children():
        widget.destroy()

root = tk.Tk()
root.title("Arithmetic Quiz Game")
root.geometry("350x300")
root.resizable(False, False)

displayMenu()
root.mainloop()
