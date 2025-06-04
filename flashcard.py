class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer 
    
    def __str__(self):
        return f"\n{self.question}\n{self.answer}"


if __name__ == "__main__":
    q = input("Question: ")
    a = input("Answer: ")

    f1 = Flashcard(q, a)

    print(f1)