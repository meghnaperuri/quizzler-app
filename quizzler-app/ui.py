import tkinter as tk
from PIL import Image, ImageTk
import html
from data import question_data
import random

THEME_COLOR = "#375362"


class QuizInterface():
    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry("400x600")
        self.window.title("quizzler")
        self.window.config(bg=THEME_COLOR)

        self.canvas=tk.Canvas(width=350,height=400, bg=THEME_COLOR, highlightthickness=0 )
        self.canvas.pack()
        self.canvas.create_rectangle(10,70,340,400,fill="white")

        self.score=0
        self.label = tk.Label(self.canvas, text=f"Score: {self.score}", bg=THEME_COLOR, fg="white")
        self.label.place(relx=1.0, rely=0.0, anchor='ne', x=-40, y=10)


        ques,ans =self.generate_question()
        print(ques, ans)

        self.text_x = (10 + 340) // 2
        self.text_y = (70 + 400) // 2
        self.text_width = 340 - 10 - 2 * 20
        self.question_text=self.canvas.create_text(
            self.text_x, self.text_y,
            # text=question_text,
            text=html.unescape(ques),
            font=('Arial', 20, 'italic'),
            fill=THEME_COLOR,
            width=self.text_width
        )

        self.true_image_load=Image.open("./images/true.png")
        self.true_image=ImageTk.PhotoImage(self.true_image_load)
        self.true_button=tk.Button(image=self.true_image, command=self.is_true)
        self.true_button.place(x=250,y=450)

        self.false_image_load=Image.open("./Images/false.png")
        self.false_image=ImageTk.PhotoImage(self.false_image_load)
        self.false_button=tk.Button(image=self.false_image,command=self.is_false)
        self.false_button.place(x=45, y=450)

        self.window.mainloop()

    def update_score(self, correct):
        if correct:
            self.score+=1
        self.label.config(text=f"Score: {self.score}")

    def update_question(self):
        ques, ans = self.generate_question()
        # print(ques, ans)
        self.current_answer = html.unescape(ans)  # Store the current answer
        self.canvas.itemconfig(self.question_text, text=html.unescape(ques))  # Update text

    def generate_question(self):
        random_question=random.choice(question_data)
        ques=html.unescape(random_question["question"])
        ans=html.unescape(random_question["correct_answer"])
        print(f"question: {html.unescape(ques)}")
        print(f"answer: {html.unescape(ans)}")
        # print("question: "+random_question["question"]+"answer: "+random_question["correct_answer"])
        return ques, ans
    def is_true(self):
        ques,ans=self.generate_question()
        # print(f"question: {html.unescape(ques)}")
        # print(f"answer: {html.unescape(ans)}")
        correct = html.unescape(ans).lower() == "true"
        self.update_score(correct)
        self.update_question()
        print("true button clicked!")

    def is_false(self):
        ques, ans = self.generate_question()
        # print(f"question: {html.unescape(ques)}")
        # print(f"answer: {html.unescape(ans)}")
        correct = html.unescape(ans).lower() == "false"
        self.update_score(correct)
        self.update_question()
        print("false button clicked!")
