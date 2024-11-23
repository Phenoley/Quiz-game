import random

questions = [
("The Earth is the fourth planet from the Sun. True or False?", False),

("Venus is the hottest planet in the solar system. True or False?", True),

("A group of lions is called a pride. True or False?", True),

("The Amazon River is the longest river in the world.True or False?", False),

("Sound travels faster in water than in air. True or False?",True),

("Polar bears are native to Antarctica. True or False?", False),

("The currency of Japan is the Yen. True or False?", True),

("Albert Einstein was awarded the Nobel Prize for inventing the theory of relativity. True or False?", False),

("A leap year has 364 days. True or False?", False),

("The Great Barrier Reef is located off the coast of Australia. True or False?", True),

("The speed of light is faster than the speed of sound. True or False?", True),

("The Eiffel Tower is taller than the Empire State Building. True or False?", False),

("Honey never spoils. True or False?", True),

("The Statue of Liberty was a gift from France. True or False?", True),

("Humans share about 50% of their DNA with bananas. True or False?", True),

("The Pacific Ocean is the smallest ocean on Earth. True or False?", False),

("Elephants are the only mammals that cannot jump. True or False?", True),

("The human heart has four chambers. True or False?", True),

("The capital of Canada is Toronto. True or False?", False),

("Coffee is made from berries. True or False?", True)
]

#initializes the quiz and shuffles the question
def quiz(questions):
    print("Welcome to quiz game.")
    random.shuffle(questions)
    return questions

#accepts users input or answer
def ask_questions(questions):
    score = 0
    #iterates over the items in questions and uses slicing to limit the questions asked to just ten 
    for i, (question, answer) in enumerate(questions[:10], start= 1):
        user_answer = input(f"Q{i}. {question}: ").strip().capitalize()

        #convert str to boolean
        if user_answer == "True":
            user_answer = True
        elif user_answer == "False":
            user_answer == False
        else: 
            print("Invalid response! Please answer 'True' or 'False'.")
            continue

        #Check answer and update score
        if user_answer == answer: 
            print("Correct!")
            score += 1
        else: 
            print(f"Incorrect!")
    return score

#displays the the score after the test is taken
def display_score(score, total_questions):
    print(f"You got: {score}/{total_questions}")

shuffle_questions = quiz(questions)
score = ask_questions(shuffle_questions)
display_score(score,len(questions[:10]))





    