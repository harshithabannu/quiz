# Quiz Game

## Overview

The Quiz Game is a simple command-line Python application that presents users with a series of multiple-choice questions. Users answer by selecting the number corresponding to their choice. The game provides immediate feedback on each answer and displays the total score at the end.

## Features

- **Multiple Questions:** Includes a set of predefined questions with multiple-choice answers.
- **Immediate Feedback:** Notifies users whether their answer is correct or incorrect.
- **Score Calculation:** Displays the total score based on correct answers.
- **Customizable:** Easily update questions and answers as needed.

## Requirements

- Python 3.x

## How to Run

1. **Save the Script:** Ensure the script is saved as `quiz_game.py`.

2. **Run the Script:**
    ```sh
    python quiz_game.py
    ```

3. **Interact with the Game:**
    - Answer each question by entering the number corresponding to your choice.
    - The game will inform you whether your answer is correct or wrong.
    - Your final score will be displayed after all questions are answered.

## Code Explanation

### `display_question(question, options, correct_option)`

- **Parameters:**
  - `question` (str): The question to display.
  - `options` (list): List of possible answers.
  - `correct_option` (str): The correct answer.

- **Returns:**
  - `True` if the user's answer is correct, otherwise `False`.

### `main()`

- Contains a list of questions, options, and correct answers.
- Iterates through the questions and uses `display_question()` to present each question.
- Tracks the user's score and displays the final result.

## Example

**Run the application:**

```sh
python quiz_game.py

**Sample Output:**
Welcome to the Quiz Game!
You will be asked 5 questions. Try to answer them correctly!

What is the capital of France?
1. Berlin
2. Madrid
3. Paris
4. Lisbon
Enter the number of your answer: 3
Correct!
...
You got 5 out of 5 questions correct!

##Customization
**To modify the questions or answers:**

Update the questions list in the main() function with new questions and options.


## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.


## Acknowledgments

Thanks to Python documentation and the programming community for resources and support.

