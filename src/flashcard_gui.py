import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import random
from flashcard import Flashcard
from deck import Deck
from quiz import Quiz

class FlashcardGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 Flashcard Quiz App")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        # Initialize deck and quiz
        self.deck = Deck()
        self.quiz = None
        self.current_quiz_index = 0
        self.quiz_score = 0
        
        # Create main interface
        self.create_widgets()
        
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="🧠 Flashcard Quiz App", 
                               font=('Arial', 24, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 30))
        
        # Left panel - Deck management
        deck_frame = ttk.LabelFrame(main_frame, text="Deck Management", padding="15")
        deck_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 10))
        
        # Add card button
        ttk.Button(deck_frame, text="Add Card Manually", 
                  command=self.add_card_dialog).grid(row=0, column=0, pady=5, sticky=tk.W+tk.E)
        
        # Load from file button
        ttk.Button(deck_frame, text="Load from JSON", 
                  command=self.load_from_file).grid(row=1, column=0, pady=5, sticky=tk.W+tk.E)
        
        # Save to file button
        ttk.Button(deck_frame, text="Save to JSON", 
                  command=self.save_to_file).grid(row=2, column=0, pady=5, sticky=tk.W+tk.E)
        
        # Clear deck button
        ttk.Button(deck_frame, text="Clear Deck", 
                  command=self.clear_deck).grid(row=3, column=0, pady=5, sticky=tk.W+tk.E)
        
        # Deck info
        self.deck_info = ttk.Label(deck_frame, text="Cards in deck: 0")
        self.deck_info.grid(row=4, column=0, pady=(20, 5))
        
        # Start quiz button
        self.start_quiz_btn = ttk.Button(deck_frame, text="Start Quiz", 
                                        command=self.start_quiz, state='disabled')
        self.start_quiz_btn.grid(row=5, column=0, pady=10, sticky=tk.W+tk.E)
        
        # Middle panel - Card display/quiz
        self.quiz_frame = ttk.LabelFrame(main_frame, text="Quiz Area", padding="15")
        self.quiz_frame.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10)
        self.quiz_frame.columnconfigure(0, weight=1)
        
        # Quiz content (initially hidden)
        self.quiz_question = ttk.Label(self.quiz_frame, text="", 
                                      font=('Arial', 14, 'bold'), wraplength=300)
        self.quiz_question.grid(row=0, column=0, pady=20)
        
        self.answer_var = tk.StringVar()
        self.answer_entry = ttk.Entry(self.quiz_frame, textvariable=self.answer_var, 
                                     font=('Arial', 12), width=30)
        self.answer_entry.grid(row=1, column=0, pady=10)
        self.answer_entry.bind('<Return>', lambda e: self.submit_answer())
        
        # Quiz buttons frame
        quiz_buttons_frame = ttk.Frame(self.quiz_frame)
        quiz_buttons_frame.grid(row=2, column=0, pady=20)
        
        self.submit_btn = ttk.Button(quiz_buttons_frame, text="Submit Answer", 
                                    command=self.submit_answer)
        self.submit_btn.grid(row=0, column=0, padx=5)
        
        self.next_btn = ttk.Button(quiz_buttons_frame, text="Next Question", 
                                  command=self.next_question, state='disabled')
        self.next_btn.grid(row=0, column=1, padx=5)
        
        self.end_quiz_btn = ttk.Button(quiz_buttons_frame, text="End Quiz", 
                                      command=self.end_quiz)
        self.end_quiz_btn.grid(row=0, column=2, padx=5)
        
        # Result display
        self.result_label = ttk.Label(self.quiz_frame, text="", 
                                     font=('Arial', 12))
        self.result_label.grid(row=3, column=0, pady=10)
        
        # Quiz progress
        self.progress_label = ttk.Label(self.quiz_frame, text="")
        self.progress_label.grid(row=4, column=0, pady=5)
        
        # Right panel - Card list
        list_frame = ttk.LabelFrame(main_frame, text="Current Cards", padding="15")
        list_frame.grid(row=1, column=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(10, 0))
        
        # Scrollable listbox for cards
        list_scroll_frame = ttk.Frame(list_frame)
        list_scroll_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        list_frame.rowconfigure(0, weight=1)
        list_frame.columnconfigure(0, weight=1)
        
        self.cards_listbox = tk.Listbox(list_scroll_frame, width=35, height=15)
        scrollbar = ttk.Scrollbar(list_scroll_frame, orient=tk.VERTICAL, 
                                 command=self.cards_listbox.yview)
        self.cards_listbox.configure(yscrollcommand=scrollbar.set)
        
        self.cards_listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        list_scroll_frame.rowconfigure(0, weight=1)
        list_scroll_frame.columnconfigure(0, weight=1)
        
        # Remove card button
        ttk.Button(list_frame, text="Remove Selected", 
                  command=self.remove_selected_card).grid(row=1, column=0, pady=10)
        
        # Hide quiz elements initially
        self.hide_quiz_elements()
        
    def add_card_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Add New Card")
        dialog.geometry("400x300")
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Center the dialog
        dialog.geometry("+%d+%d" % (self.root.winfo_rootx() + 50, 
                                   self.root.winfo_rooty() + 50))
        
        frame = ttk.Frame(dialog, padding="20")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        ttk.Label(frame, text="Question:").grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        question_text = tk.Text(frame, height=4, width=40)
        question_text.grid(row=1, column=0, pady=(0, 10))
        
        ttk.Label(frame, text="Answer:").grid(row=2, column=0, sticky=tk.W, pady=(0, 5))
        answer_text = tk.Text(frame, height=4, width=40)
        answer_text.grid(row=3, column=0, pady=(0, 20))
        
        def save_card():
            question = question_text.get("1.0", tk.END).strip()
            answer = answer_text.get("1.0", tk.END).strip()
            
            if question and answer:
                card = Flashcard(question, answer)
                self.deck.add_card(card)
                self.update_display()
                dialog.destroy()
                messagebox.showinfo("Success", "Card added successfully!")
            else:
                messagebox.showerror("Error", "Both question and answer are required!")
        
        button_frame = ttk.Frame(frame)
        button_frame.grid(row=4, column=0)
        
        ttk.Button(button_frame, text="Save Card", command=save_card).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Cancel", command=dialog.destroy).grid(row=0, column=1, padx=5)
        
        question_text.focus()
        
    def load_from_file(self):
        file_path = filedialog.askopenfilename(
            title="Load Flashcards",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                self.deck.load_from_path(file_path)
                self.update_display()
                messagebox.showinfo("Success", f"Loaded {len(self.deck)} flashcards!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load file: {str(e)}")
    
    def save_to_file(self):
        if len(self.deck) == 0:
            messagebox.showwarning("Warning", "No cards to save!")
            return
            
        file_path = filedialog.asksaveasfilename(
            title="Save Flashcards",
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                self.deck.save_to_file(file_path)
                messagebox.showinfo("Success", "Flashcards saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {str(e)}")
    
    def clear_deck(self):
        if len(self.deck) > 0:
            if messagebox.askyesno("Confirm", "Are you sure you want to clear all cards?"):
                self.deck.cards.clear()
                self.update_display()
                self.hide_quiz_elements()
    
    def remove_selected_card(self):
        selection = self.cards_listbox.curselection()
        if selection:
            index = selection[0]
            del self.deck.cards[index]
            self.update_display()
        else:
            messagebox.showwarning("Warning", "Please select a card to remove!")
    
    def update_display(self):
        # Update deck info
        self.deck_info.config(text=f"Cards in deck: {len(self.deck)}")
        
        # Update cards listbox
        self.cards_listbox.delete(0, tk.END)
        for i, card in enumerate(self.deck.cards):
            # Truncate long questions for display
            question_preview = card.question[:50] + "..." if len(card.question) > 50 else card.question
            self.cards_listbox.insert(tk.END, f"{i+1}. {question_preview}")
        
        # Enable/disable start quiz button
        self.start_quiz_btn.config(state='normal' if len(self.deck) > 0 else 'disabled')
    
    def start_quiz(self):
        if len(self.deck) == 0:
            messagebox.showwarning("Warning", "No cards available for quiz!")
            return
        
        self.deck.shuffle()
        self.current_quiz_index = 0
        self.quiz_score = 0
        self.show_quiz_elements()
        self.show_current_question()
    
    def show_quiz_elements(self):
        # Show quiz elements
        self.quiz_question.grid()
        self.answer_entry.grid()
        self.submit_btn.grid()
        self.next_btn.grid()
        self.end_quiz_btn.grid()
        self.result_label.grid()
        self.progress_label.grid()
        
        # Reset button states
        self.submit_btn.config(state='normal')
        self.next_btn.config(state='disabled')
        self.answer_entry.config(state='normal')
        
    def hide_quiz_elements(self):
        # Hide quiz elements
        self.quiz_question.grid_remove()
        self.answer_entry.grid_remove()
        self.submit_btn.grid_remove()
        self.next_btn.grid_remove()
        self.end_quiz_btn.grid_remove()
        self.result_label.grid_remove()
        self.progress_label.grid_remove()
    
    def show_current_question(self):
        if self.current_quiz_index < len(self.deck):
            card = self.deck.cards[self.current_quiz_index]
            self.quiz_question.config(text=card.question)
            self.answer_var.set("")
            self.result_label.config(text="", foreground="black")
            self.progress_label.config(text=f"Question {self.current_quiz_index + 1} of {len(self.deck)}")
            
            # Reset button states
            self.submit_btn.config(state='normal')
            self.next_btn.config(state='disabled')
            self.answer_entry.config(state='normal')
            self.answer_entry.focus()
        else:
            self.end_quiz()
    
    def submit_answer(self):
        if self.current_quiz_index >= len(self.deck):
            return
        
        user_answer = self.answer_var.get().strip()
        if not user_answer:
            messagebox.showwarning("Warning", "Please enter an answer!")
            return
        
        card = self.deck.cards[self.current_quiz_index]
        
        # Use the normalize function from Quiz class
        def normalize(text):
            return text.strip().lower().rstrip(".?!")
        
        if normalize(user_answer) == normalize(card.answer):
            self.result_label.config(text="✅ Correct!", foreground="green")
            self.quiz_score += 1
        else:
            self.result_label.config(text=f"❌ Incorrect! Answer: {card.answer}", 
                                   foreground="red")
        
        # Disable submit button and entry, enable next button
        self.submit_btn.config(state='disabled')
        self.answer_entry.config(state='disabled')
        self.next_btn.config(state='normal')
        self.next_btn.focus()
    
    def next_question(self):
        self.current_quiz_index += 1
        if self.current_quiz_index < len(self.deck):
            self.show_current_question()
        else:
            self.end_quiz()
    
    def end_quiz(self):
        if self.current_quiz_index > 0:  # Only show results if quiz was started
            score_percentage = (self.quiz_score / len(self.deck)) * 100
            message = f"Quiz Complete!\n\nFinal Score: {self.quiz_score}/{len(self.deck)} ({score_percentage:.1f}%)"
            
            if score_percentage >= 90:
                message += "\n🎉 Excellent work!"
            elif score_percentage >= 70:
                message += "\n👍 Good job!"
            elif score_percentage >= 50:
                message += "\n📚 Keep studying!"
            else:
                message += "\n💪 Practice makes perfect!"
            
            messagebox.showinfo("Quiz Results", message)
        
        self.hide_quiz_elements()
        self.current_quiz_index = 0
        self.quiz_score = 0

def main():
    root = tk.Tk()
    app = FlashcardGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()