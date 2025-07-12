from deck import Deck

class Quiz:
    def __init__(self, deck):
        self.deck = deck
        self.score = 0

    def normalize(self, text):
        return text.strip().lower().rstrip(".?!")

    def start(self):
        print("\n\n\n\n\n\n\n--- Starting Quiz ---\n")
        self.deck.shuffle()

        for i, card in enumerate(self.deck.cards, start=1):
            print(f"Question {i}: {card.question}")
            answer = input("Your answer: ").strip()

            if self.normalize(answer) == self.normalize(card.answer):
                print("✅ Correct!\n")
                self.score += 1
            else:
                print(f"❌ Incorrect. Correct answer: {card.answer}\n")

        print(f"Quiz complete! Final Score: {self.score}/{len(self.deck)}\n")
