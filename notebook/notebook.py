import datetime


# Store the next available ID for all new notes
last_id = 0

class Note:
    """Represents note in the notebook. Match against a string in searches and store tags for
    each note."""

    def __init__(self, memo, tags=''):
        """Initialize a note with memo and optional space-separated tags. Automatically set the
        note's creation date and a unique ID."""
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, query):
        """Determine if this note matches the filter query. Return True if it matches, False
        otherwise. Search is case insensitive and matches both text and tags."""
        return query.lower() in self.memo.lower() or query.lower() in self.tags.lower()


class Notebook:
    """Represent a collection of notes that can be tagged, modified, and searched."""

    def __init__(self):
        """Initialize a new notebook with an empty list."""
        self.notes = []

    def new_note(self, memo, tags=''):
        """Create a new note and add it to the list."""
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        """Return the note with the passed ID."""
        note = [note for note in self.notes
                if str(note_id) == str(note.id)]
        if not note:
            return None
        return note[0]

    def modify_memo(self, note_id, memo):
        """Modify the memo of the note with the passed in ID."""
        note = self._find_note(note_id)
        if not note:
            return False
        note.memo = memo
        return True

    def modify_tags(self, note_id, tags):
        """Modify the tags of the note with the passed in ID."""
        note = self._find_note(note_id)
        if not note:
            return False
        note.tags = tags
        return True

    def search(self, query):
        """Find all notes that match the given query string."""
        if not self.notes:
            print('\nNo matching notes!')
            return None
        return [note for note in self.notes
                if note.match(query)]
