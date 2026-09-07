import tkinter as tk
from tkinter import ttk, messagebox


class LibraryView:

    def __init__(self, root):

        self.root = root

        self.root.title("Library Management System")
        self.root.geometry("950x650")
        self.root.resizable(False, False)

        # ---------------- TITLE ----------------

        title = tk.Label(
            root,
            text="LIBRARY MANAGEMENT SYSTEM",
            font=("Arial", 22, "bold"),
            bg="#2c3e50",
            fg="white",
            pady=15
        )

        title.pack(fill="x")

        # ---------------- NOTEBOOK ----------------

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # Create tabs
        self.add_tab = ttk.Frame(self.notebook)
        self.issue_tab = ttk.Frame(self.notebook)
        self.return_tab = ttk.Frame(self.notebook)
        self.search_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.add_tab, text="Add Book")
        self.notebook.add(self.issue_tab, text="Issue Book")
        self.notebook.add(self.return_tab, text="Return Book")
        self.notebook.add(self.search_tab, text="Search Books")

        self.create_add_tab()
        self.create_issue_tab()
        self.create_return_tab()
        self.create_search_tab()

    # =========================================================
    # ADD BOOK TAB
    # =========================================================

    def create_add_tab(self):

        frame = ttk.Frame(self.add_tab, padding=30)
        frame.pack()

        ttk.Label(
            frame,
            text="Add New Book",
            font=("Arial", 18, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=20)

        ttk.Label(
            frame,
            text="Book ID:"
        ).grid(row=1, column=0, sticky="w", pady=10)

        self.book_id_entry = ttk.Entry(frame, width=35)
        self.book_id_entry.grid(row=1, column=1, pady=10)

        ttk.Label(
            frame,
            text="Book Title:"
        ).grid(row=2, column=0, sticky="w", pady=10)

        self.title_entry = ttk.Entry(frame, width=35)
        self.title_entry.grid(row=2, column=1, pady=10)

        ttk.Label(
            frame,
            text="Author:"
        ).grid(row=3, column=0, sticky="w", pady=10)

        self.author_entry = ttk.Entry(frame, width=35)
        self.author_entry.grid(row=3, column=1, pady=10)

        ttk.Label(
            frame,
            text="Quantity:"
        ).grid(row=4, column=0, sticky="w", pady=10)

        self.quantity_entry = ttk.Entry(frame, width=35)
        self.quantity_entry.grid(row=4, column=1, pady=10)

        self.add_button = ttk.Button(
            frame,
            text="Add Book"
        )

        self.add_button.grid(
            row=5,
            column=0,
            columnspan=2,
            pady=25
        )

    # =========================================================
    # ISSUE BOOK TAB
    # =========================================================

    def create_issue_tab(self):

        frame = ttk.Frame(self.issue_tab, padding=30)
        frame.pack()

        ttk.Label(
            frame,
            text="Issue Book",
            font=("Arial", 18, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=20)

        ttk.Label(
            frame,
            text="Book ID:"
        ).grid(row=1, column=0, sticky="w", pady=10)

        self.issue_book_id_entry = ttk.Entry(
            frame,
            width=35
        )

        self.issue_book_id_entry.grid(
            row=1,
            column=1,
            pady=10
        )

        ttk.Label(
            frame,
            text="Student Name:"
        ).grid(row=2, column=0, sticky="w", pady=10)

        self.student_name_entry = ttk.Entry(
            frame,
            width=35
        )

        self.student_name_entry.grid(
            row=2,
            column=1,
            pady=10
        )

        ttk.Label(
            frame,
            text="Issue Date:"
        ).grid(row=3, column=0, sticky="w", pady=10)

        self.issue_date_entry = ttk.Entry(
            frame,
            width=35
        )

        self.issue_date_entry.grid(
            row=3,
            column=1,
            pady=10
        )

        ttk.Label(
            frame,
            text="Format: DD-MM-YYYY",
            foreground="gray"
        ).grid(
            row=4,
            column=1,
            sticky="w"
        )

        self.issue_button = ttk.Button(
            frame,
            text="Issue Book"
        )

        self.issue_button.grid(
            row=5,
            column=0,
            columnspan=2,
            pady=25
        )

    # =========================================================
    # RETURN BOOK TAB
    # =========================================================

    def create_return_tab(self):

        frame = ttk.Frame(
            self.return_tab,
            padding=30
        )

        frame.pack()

        ttk.Label(
            frame,
            text="Return Book",
            font=("Arial", 18, "bold")
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            pady=20
        )

        ttk.Label(
            frame,
            text="Book ID:"
        ).grid(
            row=1,
            column=0,
            sticky="w",
            pady=10
        )

        self.return_book_id_entry = ttk.Entry(
            frame,
            width=35
        )

        self.return_book_id_entry.grid(
            row=1,
            column=1,
            pady=10
        )

        self.return_button = ttk.Button(
            frame,
            text="Return Book"
        )

        self.return_button.grid(
            row=2,
            column=0,
            columnspan=2,
            pady=25
        )

    # =========================================================
    # SEARCH TAB
    # =========================================================

    def create_search_tab(self):

        top_frame = ttk.Frame(
            self.search_tab,
            padding=10
        )

        top_frame.pack(fill="x")

        ttk.Label(
            top_frame,
            text="Search:"
        ).pack(side="left", padx=5)

        self.search_entry = ttk.Entry(
            top_frame,
            width=40
        )

        self.search_entry.pack(
            side="left",
            padx=5
        )

        self.search_button = ttk.Button(
            top_frame,
            text="Search"
        )

        self.search_button.pack(
            side="left",
            padx=5
        )

        self.show_all_button = ttk.Button(
            top_frame,
            text="Show All"
        )

        self.show_all_button.pack(
            side="left",
            padx=5
        )

        # ---------------- TABLE ----------------

        table_frame = ttk.Frame(self.search_tab)
        table_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        columns = (
            "book_id",
            "title",
            "author",
            "quantity"
        )

        self.book_table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        self.book_table.heading(
            "book_id",
            text="Book ID"
        )

        self.book_table.heading(
            "title",
            text="Title"
        )

        self.book_table.heading(
            "author",
            text="Author"
        )

        self.book_table.heading(
            "quantity",
            text="Available Quantity"
        )

        self.book_table.column(
            "book_id",
            width=100
        )

        self.book_table.column(
            "title",
            width=300
        )

        self.book_table.column(
            "author",
            width=250
        )

        self.book_table.column(
            "quantity",
            width=150
        )

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.book_table.yview
        )

        self.book_table.configure(
            yscrollcommand=scrollbar.set
        )

        self.book_table.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

    # =========================================================
    # DISPLAY BOOKS
    # =========================================================

    def display_books(self, books):

        # Remove old records
        for item in self.book_table.get_children():
            self.book_table.delete(item)

        # Insert new records
        for book in books:
            self.book_table.insert(
                "",
                "end",
                values=book
            )

    # =========================================================
    # MESSAGE FUNCTIONS
    # =========================================================

    def show_info(self, message):
        messagebox.showinfo(
            "Library Management",
            message
        )

    def show_error(self, message):
        messagebox.showerror(
            "Error",
            message
        )

    # =========================================================
    # CLEAR ADD BOOK FORM
    # =========================================================

    def clear_add_form(self):

        self.book_id_entry.delete(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

    # =========================================================
    # CLEAR ISSUE FORM
    # =========================================================

    def clear_issue_form(self):

        self.issue_book_id_entry.delete(0, tk.END)
        self.student_name_entry.delete(0, tk.END)
        self.issue_date_entry.delete(0, tk.END)

    # =========================================================
    # CLEAR RETURN FORM
    # =========================================================

    def clear_return_form(self):

        self.return_book_id_entry.delete(0, tk.END)

