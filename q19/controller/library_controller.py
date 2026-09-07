class LibraryController:

    def __init__(self, model, view):

        self.model = model
        self.view = view

        # Connect buttons to controller functions
        self.view.add_button.config(
            command=self.add_book
        )

        self.view.issue_button.config(
            command=self.issue_book
        )

        self.view.return_button.config(
            command=self.return_book
        )

        self.view.search_button.config(
            command=self.search_books
        )

        self.view.show_all_button.config(
            command=self.show_all_books
        )

        # Display all books when application starts
        self.show_all_books()

    # =========================================================
    # ADD BOOK
    # =========================================================

    def add_book(self):

        book_id = self.view.book_id_entry.get().strip()
        title = self.view.title_entry.get().strip()
        author = self.view.author_entry.get().strip()
        quantity = self.view.quantity_entry.get().strip()

        # Validation
        if not book_id or not title or not author or not quantity:
            self.view.show_error(
                "Please fill all fields."
            )
            return

        try:
            book_id = int(book_id)
            quantity = int(quantity)

            if book_id <= 0:
                self.view.show_error(
                    "Book ID must be greater than 0."
                )
                return

            if quantity < 0:
                self.view.show_error(
                    "Quantity cannot be negative."
                )
                return

        except ValueError:
            self.view.show_error(
                "Book ID and Quantity must be numbers."
            )
            return

        success, message = self.model.add_book(
            book_id,
            title,
            author,
            quantity
        )

        if success:

            self.view.show_info(message)

            self.view.clear_add_form()

            self.show_all_books()

        else:
            self.view.show_error(message)

    # =========================================================
    # ISSUE BOOK
    # =========================================================

    def issue_book(self):

        book_id = self.view.issue_book_id_entry.get().strip()
        student_name = self.view.student_name_entry.get().strip()
        issue_date = self.view.issue_date_entry.get().strip()

        if not book_id or not student_name or not issue_date:

            self.view.show_error(
                "Please fill all fields."
            )

            return

        try:
            book_id = int(book_id)

        except ValueError:

            self.view.show_error(
                "Book ID must be a number."
            )

            return

        success, message = self.model.issue_book(
            book_id,
            student_name,
            issue_date
        )

        if success:

            self.view.show_info(message)

            self.view.clear_issue_form()

            self.show_all_books()

        else:

            self.view.show_error(message)

    # =========================================================
    # RETURN BOOK
    # =========================================================

    def return_book(self):

        book_id = self.view.return_book_id_entry.get().strip()

        if not book_id:

            self.view.show_error(
                "Please enter Book ID."
            )

            return

        try:
            book_id = int(book_id)

        except ValueError:

            self.view.show_error(
                "Book ID must be a number."
            )

            return

        success, message = self.model.return_book(
            book_id
        )

        if success:

            self.view.show_info(message)

            self.view.clear_return_form()

            self.show_all_books()

        else:

            self.view.show_error(message)

    # =========================================================
    # SEARCH BOOKS
    # =========================================================

    def search_books(self):

        search_text = self.view.search_entry.get().strip()

        if not search_text:

            self.show_all_books()

            return

        books = self.model.search_books(
            search_text
        )

        self.view.display_books(books)

        if not books:

            self.view.show_info(
                "No books found."
            )

    # =========================================================
    # SHOW ALL BOOKS
    # =========================================================

    def show_all_books(self):

        books = self.model.get_all_books()

        self.view.display_books(books)

