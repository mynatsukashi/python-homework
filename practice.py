player = {"correct": 0, "wrong": 0}

questions = [
    {
        "question": "What is a capital of Georgia?",
        "answers" : [
            {"text": "Tbilisi", "is_correct": True},
            {"text": "Batumi", "is_correct": False},
            {"text": "Kutaisi", "is_correct": False},
            {"text": "Baku", "is_correct": False},
        ]
    }
]

for question in questions:
    print(question["question"])
    for i, answer in enumerate(question["answers"],1):
        print(f" {i}: {answer["text"]}")
    choice = int(input("Choose your answer: "))

    chosen_answer = question["answers"][choice]
    if chosen_answer["is_correct"]:
        player["correct"] +=1
    else:
        player["wrong"] +=1
        