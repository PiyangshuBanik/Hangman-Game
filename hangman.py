import tkinter as tk
from tkinter import messagebox
import random
import os

class HangmanApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Piyangshu's Hangman Challenge")
        self.master.geometry("700x500")
        self.master.configure(bg="#f0f0f0")

        self.words = ["python", "hangman", "challenge", "programming", "developer"]
        self.word_to_guess = random.choice(self.words)
        self.guessed_letters = []
        self.max_attempts = 6
        self.incorrect_attempts = 0

        # Create GUI components
        self.title_label = tk.Label(master, text="Piyangshu's Hangman Challenge", bg="#f0f0f0", font=("Comic Sans MS", 24, "bold"))
        self.title_label.pack(pady=10)

        self.word_display = tk.Label(master, text=self.get_display_word(), bg="#f0f0f0", font=("Arial", 20))
        self.word_display.pack(pady=10)

        self.guess_entry = tk.Entry(master, font=("Arial", 14))
        self.guess_entry.pack(pady=10)

        self.submit_button = tk.Button(master, text="Guess", command=self.process_guess, bg="#4CAF50", fg="white", font=("Arial", 12))
        self.submit_button.pack(pady=5)

        self.reset_button = tk.Button(master, text="Reset Game", command=self.reset_game, bg="#FF5733", fg="white", font=("Arial", 12))
        self.reset_button.pack(pady=5)

        self.incorrect_label = tk.Label(master, text=f"Incorrect guesses remaining: {self.max_attempts}", bg="#f0f0f0", font=("Arial", 12))
        self.incorrect_label.pack(pady=10)

        self.guessed_label = tk.Label(master, text="Guessed letters: ", bg="#f0f0f0", font=("Arial", 12))
        self.guessed_label.pack(pady=10)

        self.hangman_image = tk.Label(master, bg="#f0f0f0")  # Placeholder for hangman image
        self.hangman_image.pack(pady=10)

        self.reset_game()

    def get_display_word(self):
        return ' '.join([letter if letter in self.guessed_letters else '_' for letter in self.word_to_guess])

    def process_guess(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        if len(guess) == 1 and guess.isalpha():
            if guess in self.guessed_letters:
                messagebox.showinfo("Info", "You have already guessed that letter.")
            elif guess in self.word_to_guess:
                self.guessed_letters.append(guess)
                self.word_display.config(text=self.get_display_word())
                messagebox.showinfo("Good Guess!", f"'{guess}' is in the word!")
                if self.check_win():
                    messagebox.showinfo("Congratulations!", f"You've guessed the word: {self.word_to_guess}")
            else:
                self.guessed_letters.append(guess)
                self.incorrect_attempts += 1
                self.incorrect_label.config(text=f"Incorrect guesses remaining: {self.max_attempts - self.incorrect_attempts}")
                messagebox.showwarning("Oops!", f"Sorry, '{guess}' is not in the word.")
                self.update_hangman_image()
                if self.incorrect_attempts >= self.max_attempts:
                    messagebox.showerror("Game Over", f"Sorry, you've run out of attempts! The word was '{self.word_to_guess}'")
                    self.reset_game()
        else:
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")

    def check_win(self):
        return all(letter in self.guessed_letters for letter in self.word_to_guess)

    def reset_game (self):
        self.word_to_guess = random.choice(self.words)
        self.guessed_letters = []
        self.incorrect_attempts = 0
        self.word_display.config(text=self.get_display_word())
        self.incorrect_label.config(text=f"Incorrect guesses remaining: {self.max_attempts}")
        self.guessed_label.config(text="Guessed letters: ")
        self.hangman_image.config(text="")

    def update_hangman_image(self):
        try:
            image_path = f"hangman_{self.incorrect_attempts}.png"
            if os.path.exists(image_path):
                self.hangman_image.config(image=tk.PhotoImage(file=image_path))
            else:
                self.hangman_image.config(text=f"Incorrect attempts: {self.incorrect_attempts}")
        except Exception as e:
            print(f"Error updating hangman image: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanApp(root)
    root.mainloop()