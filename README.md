🧠 Flashcard App

A simple command-line flashcard application written in Python to help users create, load, and quiz themselves using digital flashcards. Great for language learning or general study.

📦 Features

- Create flashcards manually through the terminal
- Load flashcards from a JSON file
- Take randomized quizzes
- Case-insensitive answer checking
- Easily extensible for more features

🛠 Project Structure
* flashcard-app/

- flashcard.py -- Defines the Flashcard class
- deck.py -- Manages a collection of flashcards
- quiz.py -- Handles quiz logic and scoring
- main.py -- Entry point, runs the app
- italian_flashcards.json -- Sample flashcard deck (Italian)

▶️ How to Run

1. Clone the repository:
   bash
   git clone https://github.com/alex-lisi/flashcard-app.git
   cd flashcard-app

2. Run the app:
   bash
   python main.py

> Make sure you have Python 3 installed.

📚 Sample Flashcards

This repo includes a `italian_flashcards.json` file you can test with. You can also create your own using this format:

json
[
  {
    "question": "What does 'ciao' mean?",
    "answer": "hello"
  }
]

 To Do:
- Add support for categories/tags
- Export scores or session summaries
- GUI version with Tkinter or Flask

Author:
Alex Lisi
[GitHub](https://github.com/alex-lisi)

Pull requests and suggestions are welcome!
