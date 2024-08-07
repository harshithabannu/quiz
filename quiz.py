def display_question(question, options, correct_option):
    print("\n" + question)
    for index, option in enumerate(options, 1):
        print(f"{index}. {option}")
    
    answer = input("Enter the number of your answer: ")
    
    if options[int(answer) - 1].lower() == correct_option.lower():
        print("Correct!")
        return True
    else:
        print("Wrong! The correct answer was:", correct_option)
        return False

def main():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Lisbon"],
            "answer": "Paris"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["Harper Lee", "Mark Twain", "Ernest Hemingway", "F. Scott Fitzgerald"],
            "answer": "Harper Lee"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["O2", "H2O", "CO2", "NaCl"],
            "answer": "H2O"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "answer": "Jupiter"
        },
        {
            "question": "In what year did the Titanic sink?",
            "options": ["1912", "1905", "1898", "1923"],
            "answer": "1912"
        }
    ]

    score = 0

    print("Welcome to the Quiz Game!")
    print("You will be asked 5 questions. Try to answer them correctly!")

    for q in questions:
        if display_question(q["question"], q["options"], q["answer"]):
            score += 1
    
    print(f"\nYou got {score} out of {len(questions)} questions correct!")

if __name__ == "__main__":
    main()
