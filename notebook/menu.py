import sys
from notebook import Notebook


class Menu:
    """Display an interactive menu and respond to user input."""

    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            '1': self.show_notes,
            '2': self.search_notes,
            '3': self.add_note,
            '4': self.modify_note,
            '5': self.quit,
        }

    def display_menu(self):
        print(

"""
Notebook Menu

1. Show all Notes
2. Search Notes
3. Add Note
4. Modify Note
5. Quit
"""

        )

    def run(self):
        """Display the menu and respond to user input."""
        while True:
            self.display_menu()
            choice = input('Enter an option: ')
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f'{choice} is not a valid choice')

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(f'{note.id}: tags: {note.tags}\n{note.memo}')

    def search_notes(self):
        query = input('Search for: ')
        notes = self.notebook.search(query)
        self.show_notes(notes)

    def add_note(self):
        memo = input('Enter a memo: ')
        self.notebook.new_note(memo)
        print('Note added!')

    def modify_note(self):
        _id = input('Enter a note ID: ')
        memo = input('Enter a memo: ')
        tags = input('Enter tags: ')
        if memo:
            self.notebook.modify_memo(_id, memo)
        if tags:
            self.notebook.modify_tags(_id, tags)

    def quit(self):
        print('Bye!')
        sys.exit(0)

if __name__ == '__main__':
    Menu().run()
