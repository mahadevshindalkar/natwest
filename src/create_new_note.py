import sys

from src.get_file_name import get_file_name
from src.note import Note


class CreateNewNote(Note):
    """Add task"""

    def operation(self, *args):

        filename = args[0]
        note = args[1]
        file = get_file_name(filename)

        with open(file, 'w') as f:
            f.write(note)
