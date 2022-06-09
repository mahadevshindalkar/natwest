import glob
import os
import sys

from src.note import Note


class ListNotes(Note):

    def operation(self):
        for f in glob.glob(sys.path[0] + '/resources/*'):
            file_name = os.path.split(f)[-1]
            note_name = file_name.split('.')[0]
            print(note_name)
