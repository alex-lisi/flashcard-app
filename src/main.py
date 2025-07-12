import sys
import tkinter as tk
from deck import Deck
from quiz import Quiz

def run_cli():
    """Run the original command-line interface"""
    deck = Deck()

    print("Welcome to the Flashcard Quiz App!\n")
    print("1. Create flashcards manually")
    print("2. Load flashcards from a JSON file")
    choice = input("Choose an option (1 or 2): ").strip()

    if choice == '1':
        while True:
            deck.add_card_manual()
            more = input("Add another card? (y/n): ").strip().lower()
            if more != 'y':
                break

    elif choice == '2':
        path = input("Enter JSON file name (e.g., flashcards.json): ").strip()
        try:
            deck.load_from_path(path)
            print(f"Loaded {len(deck)} flashcards.\n")
        except FileNotFoundError:
            print("⚠️ File not found. Exiting.")
            return
        except Exception as e:
            print(f"⚠️ Failed to load flashcards: {e}")
            return

    else:
        print("❌ Invalid choice. Exiting.")
        return

    if len(deck) == 0:
        print("No flashcards available to quiz. Exiting.")
        return

    quiz = Quiz(deck)
    quiz.start()

def run_gui():
    """Run the GUI interface"""
    try:
        from flashcard_gui import FlashcardGUI
        root = tk.Tk()
        app = FlashcardGUI(root)
        root.mainloop()
    except ImportError:
        print("GUI dependencies not available. Please install tkinter.")
        sys.exit(1)

def main():
    """Main entry point - choose between GUI and CLI"""
    if len(sys.argv) > 1:
        if sys.argv[1] == '--cli':
            run_cli()
        elif sys.argv[1] == '--gui':
            run_gui()
        else:
            print("Usage: python main.py [--gui|--cli]")
            print("  --gui: Run with graphical interface (default)")
            print("  --cli: Run with command-line interface")
            sys.exit(1)
    else:
        # Default to GUI if no arguments provided
        print("🧠 Flashcard Quiz App")
        print("Choose your interface:")
        print("1. GUI (Graphical Interface)")
        print("2. CLI (Command Line Interface)")
        
        choice = input("Choose an option (1 or 2, default 1): ").strip()
        
        if choice == '2':
            run_cli()
        else:
            run_gui()

if __name__ == "__main__":
    main()