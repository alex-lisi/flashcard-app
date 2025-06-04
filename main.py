from deck import Deck
from quiz import Quiz

def main():
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

if __name__ == "__main__":
    main()