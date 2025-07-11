# 🧠 Flashcard Quiz App

A modern flashcard application written in Python with both graphical (GUI) and command-line (CLI) interfaces. Perfect for language learning, exam preparation, or any type of study that benefits from spaced repetition and active recall.

## ✨ Features

### Core Functionality
- **Create flashcards manually** through intuitive interfaces
- **Load flashcards from JSON files** for easy sharing and backup
- **Take randomized quizzes** with instant feedback
- **Case-insensitive answer checking** with smart normalization
- **Save and load decks** for persistent storage
- **Real-time progress tracking** during quizzes

### GUI Features (New!)
- **Modern three-panel interface** with professional design
- **Interactive quiz area** with visual feedback (✅❌)
- **Drag-and-drop file loading** via file browser
- **Card management** with scrollable list and removal options
- **Multi-line text support** for complex questions and answers
- **Keyboard shortcuts** for efficient navigation
- **Score tracking** with encouraging feedback messages
- **Responsive design** that adapts to window resizing

### CLI Features
- **Terminal-based interface** for command-line enthusiasts
- **Simple menu system** for quick navigation
- **Batch card creation** with continuous input
- **Lightweight and fast** execution

## 🛠 Project Structure

```
flashcard-app/
├── flashcard.py           # Flashcard class definition
├── deck.py               # Deck management and card operations
├── quiz.py               # Quiz logic and scoring system
├── main.py               # Entry point with GUI/CLI selection
├── flashcard_gui.py      # GUI implementation using Tkinter
├── italian_flashcards.json  # Sample flashcard deck
├── README.md             # This file
└── .gitignore           # Git ignore rules
```

## 🚀 Installation & Setup

### Prerequisites
- **Python 3.7+** installed on your system
- **Tkinter** (usually included with Python installations)

### Quick Start
1. **Clone the repository:**
   ```bash
   git clone https://github.com/alex-lisi/flashcard-app.git
   cd flashcard-app
   ```

2. **Run the application:**
   ```bash
   python main.py
   ```

## 📖 Usage

### Running Different Interfaces

**Default (Interactive Choice):**
```bash
python main.py
```
*Prompts you to choose between GUI and CLI*

**GUI Mode (Recommended):**
```bash
python main.py --gui
```

**CLI Mode:**
```bash
python main.py --cli
```

### GUI Interface Guide

1. **Adding Cards:**
   - Click "Add Card Manually" for the card creation dialog
   - Use multi-line text areas for questions and answers
   - Press "Save Card" to add to your deck

2. **Loading Existing Decks:**
   - Click "Load from JSON" to open file browser
   - Select your JSON file (try `italian_flashcards.json`)
   - Cards will be loaded and displayed in the list

3. **Taking Quizzes:**
   - Click "Start Quiz" when you have cards in your deck
   - Type your answer and press Enter or click "Submit Answer"
   - Get instant feedback with correct/incorrect indicators
   - View your final score with encouraging messages

4. **Managing Your Deck:**
   - View all cards in the scrollable list on the right
   - Select and remove unwanted cards
   - Save your deck to JSON for future use
   - Clear the entire deck when needed

### CLI Interface Guide

1. **Choose option 1** to create cards manually
2. **Choose option 2** to load from a JSON file
3. **Follow the prompts** to add cards or specify file paths
4. **Take the quiz** when your deck is ready

## 📚 Sample Flashcards

The repository includes `italian_flashcards.json` with Italian language learning cards. You can create your own JSON files using this format:

```json
[
  {
    "question": "Come si dice 'to improve' in italiano?",
    "answer": "migliorare"
  },
  {
    "question": "Qual è il contrario di 'veloce'?",
    "answer": "lento"
  }
]
```

## 🎯 Use Cases

- **Language Learning:** Vocabulary, phrases, and grammar rules
- **Exam Preparation:** Key concepts, formulas, and definitions
- **General Knowledge:** Facts, dates, and trivia
- **Professional Development:** Technical terms and procedures
- **Academic Study:** Course material and review sessions

## 🔧 Technical Details

### Dependencies
- **Python 3.7+** - Core language
- **Tkinter** - GUI framework (included with Python)
- **JSON** - Data storage format
- **Random** - Quiz randomization

### Key Classes
- **`Flashcard`** - Individual card with question/answer pairs
- **`Deck`** - Collection of flashcards with management methods
- **`Quiz`** - Quiz logic, scoring, and answer validation
- **`FlashcardGUI`** - Complete GUI implementation

### Answer Normalization
The app uses smart answer checking that:
- Ignores case differences
- Trims whitespace
- Removes trailing punctuation (.?!)
- Ensures fair and flexible matching

## 🚧 Planned Features

- **Spaced repetition algorithm** for optimized learning
- **Category/tag system** for better organization
- **Statistics tracking** and learning analytics
- **Export capabilities** (PDF, CSV formats)
- **Multi-language support** for interface
- **Cloud sync** for cross-device access
- **Audio support** for pronunciation practice

## 🤝 Contributing

Pull requests and suggestions are welcome! Here's how to contribute:

1. **Fork the repository**
2. **Create a feature branch:** `git checkout -b feature-name`
3. **Make your changes** and test thoroughly
4. **Commit your changes:** `git commit -m 'Add feature description'`
5. **Push to the branch:** `git push origin feature-name`
6. **Open a Pull Request**

### Development Setup
```bash
# Clone your fork
git clone https://github.com/your-username/flashcard-app.git
cd flashcard-app

# Test the application
python main.py --gui
python main.py --cli
```

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Alex Lisi**
- GitHub: [@alex-lisi](https://github.com/alex-lisi)
- Feel free to reach out with questions or suggestions!

---

## 🎉 Acknowledgments

- Thanks to the Python community for excellent documentation
- Inspired by traditional flashcard study methods
- Built with modern software development best practices

**Happy studying! 🎓**