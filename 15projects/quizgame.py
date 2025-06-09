import random

questions = [
    {
        "question": "What is the capital city of Kenya?",
        "choices": ["A. Nairobi", "B. Mombasa", "C. Kisumu", "D. Eldoret"],
        "answer": "A"
    },
    {
        "question": "Who was the first President of Kenya?",
        "choices": ["A. Jomo Kenyatta", "B. Daniel Arap Moi", "C. Raila Odinga", "D. Uhuru Kenyatta"],
        "answer": "A"
    },
    {
        "question": "What gas do plants absorb from the atmosphere for photosynthesis?",
        "choices": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
        "answer": "C"
    },
    {
        "question": "Which of the following is a programming language?",
        "choices": ["A. HTML", "B. Python", "C. Excel", "D. WiFi"],
        "answer": "B"
    },
    {
        "question": "Who wrote the novel 'Things Fall Apart'?",
        "choices": ["A. Ngũgĩ wa Thiong'o", "B. Chinua Achebe", "C. Wole Soyinka", "D. Chimamanda Adichie"],
        "answer": "B"
    },
    {
        "question": "Which is the largest ocean in the world?",
        "choices": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "What is the square root of 144?",
        "choices": ["A. 12", "B. 14", "C. 11", "D. 13"],
        "answer": "A"
    },
    {
        "question": "What does CPU stand for?",
        "choices": ["A. Computer Processing Unit", "B. Central Processing Unit", "C. Control Panel Utility", "D. Central Program User"],
        "answer": "B"
    }
]

def start_quizgame():
    score = 0
    random.shuffle(questions)  # Shuffle once before the loop

    print("🎮 Welcome to the Quiz Game!\n")

    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for choice in q["choices"]:
            print(choice)
        
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        
        if user_answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.\n")

    print(f"🏁 Game over! You scored {score}/{len(questions)}.\n")

# Main loop
while True:
    start_quizgame()
    play_again = input("Do you want to play again? (YES/NO): ").strip().upper()
    if play_again not in ["YES", "Y"]:
        print("👋 BYE! Thanks for playing.")
        break
