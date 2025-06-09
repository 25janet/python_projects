import random
responses = [
    ["Yes, definitely.", "It is certain.", "Without a doubt."],         # Positive
    ["Ask again later.", "Cannot predict now.", "Reply unclear."],      # Neutral
    ["Don't count on it.", "My reply is no.", "Very doubtful."]         # Negative
]
def magic8_ball():
    print("welcome to the magic 8 ball game")
    while True:
        question = input("\nAsk your question (or type 'exit' / 'quit to quit the game)").strip()
        if question.lower() in ["quit", "exit"]:
            print("\nthanks for playing")
            break 
        elif question == "":
            print("Ypu did not type anything")
        else:
            print("Thinking")
            category = random.choice(responses)
            answer = random.choice(category)
            print(f"🎱 {answer}")
magic8_ball()