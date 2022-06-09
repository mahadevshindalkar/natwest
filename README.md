# natwest

## Problem Statement
Please build a Python CLI app that can be used for quickly taking notes on the command-line.
 
Requirements:
- The ability to create new note files from the CLI. The notes should exist in a pre-defined location in the file system.
- The ability to add content to a specific note from the CLI.


## Solution

### Requirement
- Python version: 3.8

### To execute

usage: notepad.py [-h] [-c CREATE] [-n NOTE] [-a APPEND] [-l]

CLI app for quickly taking notes.

optional arguments:
    -h, --help            show this help message and exit 
    -c CREATE, --create CREATE Name of the new note 
    -n NOTE, --note NOTE  Content of the note 
    -a APPEND, --append APPEND Name of the existing note to append 
    -l, --list  List of all notes
