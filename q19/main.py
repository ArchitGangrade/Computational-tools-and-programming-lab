import tkinter as tk

from model.library_model import LibraryModel
from view.library_view import LibraryView
from controller.library_controller import LibraryController


def main():

    root = tk.Tk()

    # Create Model
    model = LibraryModel()

    # Create View
    view = LibraryView(root)

    # Create Controller
    controller = LibraryController(
        model,
        view
    )

    # Start GUI
    root.mainloop()


if __name__ == "__main__":
    main()

