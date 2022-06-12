from mcq import Question

question_prompts = [
    "How can you represent 22/7 as a mixed fraction?\n (i) 3(1/7)\n (ii) 7(1/3)\n (iii) 1(7/3)\n  (iv) 0\n \n",
    "What is the equivalent fraction of 9/15?\n (i) 3/81\n (ii) 18/30\n (iii) 31/8\n (iv) 0\n \n",
    "What is the value of 3(4/7) ÷ 7?\n (i) 42/59\n (ii) 24/95\n (iii) 25/49\n (iv) 0\n \n"
]

questions = [
    Question(question_prompts[0], "i"),
    Question(question_prompts[1], "ii"),
    Question(question_prompts[2], "iii"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Your score -> "+ str(score) + "/" + str(len(questions)))

run_test(questions)
