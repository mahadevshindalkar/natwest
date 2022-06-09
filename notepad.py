import argparse
from src.append_note import AppendNote
from src.create_new_note import CreateNewNote
from src.list_notes import ListNotes

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='CLI app for quickly taking notes.')
    parser.add_argument('-c', '--create', type=str, help='Name of the new note')
    parser.add_argument('-n', '--note', type=str, help='Content of the note')
    parser.add_argument('-a', '--append', type=str, help='Name of the existing note to append')
    parser.add_argument('-l', '--list', action='store_true', help='List of all notes')

    args = parser.parse_args()

    if args.list:
        list_notes = ListNotes()
        list_notes.operation()
    elif args.note:
        if args.create:
            create_note = CreateNewNote()
            create_note.operation(args.create, args.note)
        elif args.append:
            append_note = AppendNote()
            append_note.operation(args.append, args.note)
