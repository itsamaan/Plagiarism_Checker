import tkinter as tk
from tkinter import filedialog
from difflib import SequenceMatcher

class PlagiarismCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Plagiarism Checker")
        self.root.state('zoomed')  # Maximize the window

        self.create_widgets()

    def create_widgets(self):
        # Original Text
        self.original_text_label = tk.Label(self.root, text="Original Text:", font=("Helvetica", 14))
        self.original_text_label.pack()

        self.original_text_box = tk.Text(self.root, height=10, width=70, font=("Helvetica", 12))
        self.original_text_box.pack()

        self.load_original_button = tk.Button(self.root, text="Load Original Text", font=("Helvetica", 12), command=self.load_original_text)
        self.load_original_button.pack()

        # Suspect Text
        self.suspect_text_label = tk.Label(self.root, text="Suspect Text:", font=("Helvetica", 14))
        self.suspect_text_label.pack()

        self.suspect_text_box = tk.Text(self.root, height=10, width=70, font=("Helvetica", 12))
        self.suspect_text_box.pack()

        self.load_suspect_button = tk.Button(self.root, text="Load Suspect Text", font=("Helvetica", 12), command=self.load_suspect_text)
        self.load_suspect_button.pack()

        # Check Plagiarism
        self.check_button = tk.Button(self.root, text="Check Plagiarism", font=("Helvetica", 14, "bold"), command=self.check_plagiarism)
        self.check_button.pack()

        # Similarity Label
        self.similarity_label = tk.Label(self.root, text="", font=("Helvetica", 16, "bold"))
        self.similarity_label.pack()

    def load_original_text(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                self.original_text_box.delete("1.0", "end")
                self.original_text_box.insert("1.0", file.read())

    def load_suspect_text(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                self.suspect_text_box.delete("1.0", "end")
                self.suspect_text_box.insert("1.0", file.read())

    def calculate_similarity(self, text1, text2):
        similarity_ratio = SequenceMatcher(None, text1, text2).ratio()
        return similarity_ratio

    def check_plagiarism(self):
        original_text = self.original_text_box.get("1.0", "end-1c")
        suspect_text = self.suspect_text_box.get("1.0", "end-1c")

        similarity_ratio = self.calculate_similarity(original_text, suspect_text)
        self.similarity_label.config(text=f"Plagiarism: {similarity_ratio:.2%}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PlagiarismCheckerApp(root)
    root.mainloop()
