import sys
from src.create_new_note import CreateNewNote
from src.get_file_name import get_file_name


def test_create_new_note():
    note_title = "test_note"
    note = "This is test note"

    create_note = CreateNewNote()
    create_note.operation(note_title, note)

    file = get_file_name(note_title)
    read_file = open(file, 'r')

    assert note == read_file.read()
