# Quiz game 
 
questions = ( 
    "How many elements in the periodic table?", 
    "Which animal has the largest egg?", 
    "How many bones in the human body?", 
    "Which planet is the hottest in the solar system?" 
) 
 
options = ( 
    ("A.116", "B.117", "C.118", "D.119"), 
    ("A.Lion", "B.Cat", "C.Dog", "D.Ostrich"), 
    ("A.206", "B.207", "C.208", "D.209"), 
    ("A.Mercury", "B.Venus", "C.Earth", "D.Mars") 
) 
 
answers = ("C", "D", "A", "B") 
 
guesses = [] 
score = 0 
question_num = 0 
 
for question in questions: 
    print("---------------------------") 
    print(question) 
 
    for option in options[question_num]: 
        print(option) 
 
    guess = input("Enter (A, B, C, D): ").upper() 
    guesses.append(guess) 
 
    if guess == answers[question_num]: 
        score += 1 
        print("Correct") 
    else: 
        print("Wrong") 
 
    question_num += 1 
 
# Final Score 
print("---------------------------") 
print(f"Your score: {score}/{len(questions)}")