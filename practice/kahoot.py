# Define player 
player = {
    "correct": 0, 
    "wrong": 0
}

# Ask question

quiz = [ {
    # Define question
    "question": "What is the capital of Georgia?",
    # Define answers
    "answers": [
        {"text": "Tbilisi", "is_correct": True},
        {"text": "Batumi", "is_correct": False},
        {"text": "Kutaisi", "is_correct": False},
        {"text": "Baku", "is_correct": False},
    ]
}
]

# Print main question
def ask(question):
    print(question["question"])

def get_answers(answer):
    for i, answer in enumerate(question["answers"]):
        print(f"{i}: {answer["text"]}")


for question in quiz:
    ask(question)
    # Print answers
    get_answers()
    # Get user's answer
    choice = int(input("Choose your answer:"))
    chosen_answer = question["answers"][choice]
    # "If" statement to sort answers
    if chosen_answer ["is_correct"]:
        player["correct"] +=1
    else:
        player["wrong"] +=1
print(player)





