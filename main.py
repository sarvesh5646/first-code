import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class BookShopPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Book Shop")

        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TButton', background='#0078d4', foreground='white')
        self.style.map('TButton', background=[('active', '#005ea2')])
        self.style.configure('TRadiobutton', font=("Arial", 12), foreground="#333333")

        self.frame_title = ttk.Frame(master)
        self.frame_title.pack(pady=(10, 20), expand=True, fill=tk.BOTH)

        self.label_title = ttk.Label(self.frame_title, text="Welcome to the Book Shop", font=("Arial", 18, "bold"), foreground="#0078d4")
        self.label_title.pack()

        self.label_slogan = ttk.Label(self.frame_title, text="Find your next favorite book here!", font=("Arial", 12), foreground="#333333")
        self.label_slogan.pack()

        self.frame_books = ttk.Frame(master)
        self.frame_books.pack(pady=(0, 20), expand=True, fill=tk.BOTH)

        self.book_var = tk.StringVar()

        books = [
            "Python Programming",
            "Introduction to Algorithms",
            "Data Structures and Algorithms in Python",
            "Clean Code: A Handbook of Agile Software Craftsmanship",
            "Design Patterns: Elements of Reusable Object-Oriented Software",
            "Cracking the Coding Interview",
            "The Pragmatic Programmer: Your Journey to Mastery",
            "Head First Design Patterns",
            "Effective Java",
            "JavaScript: The Good Parts"
        ]

        for i, book in enumerate(books):
            label_book = ttk.Radiobutton(self.frame_books, text=f"Book {i+1}: {book}", variable=self.book_var, value=book, style="TRadiobutton")
            label_book.pack(anchor=tk.W, padx=10, pady=5)

        self.frame_buttons = ttk.Frame(master)
        self.frame_buttons.pack(pady=(0, 10), expand=True, fill=tk.BOTH)

        self.button_purchase = ttk.Button(self.frame_buttons, text="Purchase", command=self.purchase)
        self.button_purchase.pack(side="left", padx=10, expand=True, fill=tk.BOTH)

        self.button_close = ttk.Button(self.frame_buttons, text="Close", command=self.close)
        self.button_close.pack(side="left", padx=10, expand=True, fill=tk.BOTH)

    def purchase(self):
        selected_book = self.book_var.get()
        if selected_book:
            messagebox.showinfo("Purchase", f"Thank you for purchasing: {selected_book}")
        else:
            messagebox.showwarning("No Book Selected", "Please select a book to purchase.")

    def close(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    root.geometry("400x500")  # Set initial window size
    app = BookShopPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
