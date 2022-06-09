from src.get_file_name import get_file_name
from src.note import Note


class AppendNote(Note):
    """Append note"""

    def operation(self, *args):
        filename = args[0]
        note = args[1]
        file = get_file_name(filename)

        with open(file, 'a+') as f:
            # Move read cursor to the start of file.
            f.seek(0)
            # If file is not empty then append '\n'
            data = f.read(100)
            if len(data) > 0:
                f.write("\n")
            # Append text at the end of file
            f.write(note)
