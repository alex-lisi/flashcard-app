from flashcard import Flashcard
import random
import json

class Deck:
    def __init__(self):
        self.cards = []

    def __str__(self):
        return "\nFlashcards in deck:\n" + '\n'.join(str(card) for card in self.cards)
    
    def add_card(self, Flashcard):
        # append new Flashcard
        self.cards.append(Flashcard)

    def add_card_manual(self):
        # prompt user to enter a Flashcard manually
        while True:
            question = input("\nEnter the question: ").strip()
            answer = input("Enter the answer: ").strip()

            if question and answer:
                card = Flashcard(question, answer)
                self.add_card(card)
                print("\nFlashcard added successfully!\n")
                break  # Exit loop when input is valid
            else:
                print("Question and answer cannot be empty. Please try again.\n")

    def load_from_path(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                card = Flashcard(item['question'], item['answer'])
                self.add_card(card)


    def remove_card(self, index):
        # remove a Flashcard by index
        if 0 <= index < len(self.cards):
            del self[index]
    
    def shuffle(self):
        # randomly shuffle the Deck
        random.shuffle(self.cards)
    
    def __len__(self):
        return len(self.cards)
    
    def __getitem__(self, index):
        return self.cards[index]
    
    def save_to_file(self, path):
        """Save flashcards to a JSON file."""
        with open(path, 'w') as f:
            data = [{'question': c.question, 'answer': c.answer} for c in self.cards]
            json.dump(data, f, indent=4)

# test
if __name__ == '__main__':
    deck = Deck()
    while True:
        deck.add_card_manual()
        cont = input("Add another card? (y/n): ").strip().lower()
        if cont != 'y':
            break

    print(deck)