#!/usr/bin/env python3
import argparse
import secrets
import pyperclip
import datetime
import os
import csv
import pathlib

def entry():
    global vowels, majorSeparation, minorSeparation, extensionSeparation, cwd, args
    vowels = ('A','E','I','O','U')
    majorSeparation = '_'
    minorSeparation = '-'
    extensionSeparation = '.'
    cwd = os.getcwd()

    parser = argparse.ArgumentParser(description='Filename generation utility. Default behaviour will copy a name to your clipboard, but you can also make it generate a folder or a text file with special flags.')
    parser.add_argument('--prefix', help='Prefix to generated file name.')
    parser.add_argument('--suffix', help='Suffix to add to end of generated file name.')
    parser.add_argument('--type', help='Type of project being made.')
    parser.add_argument('--time', help='Time format string')
    parser.add_argument('--stamp', action='store_true', help='Ends name generation after prefix, for quickly prefxing existing file names.')
    parser.add_argument('--bytes', type=int, default=4, help='Number of bytes for name generation.')
    parser.add_argument('--name', help='Optional Name of project being made')
    parser.add_argument('--ext', help='File extension, normally only 3 characters.')
    parser.add_argument('-c', '--clipboard', action="store_true", help='Adds name string to clipboard.')
    parser.add_argument('-C', '--clipboard-as-name', action="store_true", help='Uses existing clipboard content as name. Useful for modifying existing names or filenames by copying it to clipboard first.')
    parser.add_argument('--mkdir', action='store_true')
    parser.add_argument('--touch', action='store_true')
    args = parser.parse_args()

    name = generate()
    if args.clipboard:
        pyperclip.copy(name)
    
    print( name + "(in clipboard)" if args.clipboard else name )

    if args.mkdir == True:
        make_directory(name)

    if args.touch == True:
        touch(name)

def remove_vowels(txt):
    first_char = txt[0]
    txt = txt[1:]
    return first_char + ''.join([l for l in txt if l not in vowels])

def caps(txt):
    return txt.upper()

def hex(bytes):
    return secrets.token_hex(bytes)

def generate():
    name = ""
    if args.type is not None:
        name = name + remove_vowels(caps(args.type))
        name += majorSeparation

    if args.time is not None:
        name += datetime.date.today().strftime(args.time)
        name += majorSeparation

    if args.prefix is not None:
        name += args.prefix.lower() + minorSeparation

    if args.stamp == True:
        return name

    print(args.clipboard_as_name)
    if args.clipboard_as_name and pyperclip.paste() != "":
        clipboard_content = pyperclip.paste()
        clipboard_content = clipboard_content.lower().replace(' ', '-')
        name += clipboard_content
    elif args.name is None:
        name += hex(args.bytes)
    else:
        name += args.name.lower()

    if args.suffix is not None:
        name += minorSeparation + args.suffix.lower()

    if args.ext is not None:
        name += extensionSeparation + args.ext.lower()

    return name

def make_directory(name):
    target = os.path.join(cwd, name)
    if not os.path.exists( target ):
        os.makedirs(target)
        print( target + " directory made!")

def touch(filename, times=None):
    with open(filename, 'a'):
        os.utime(filename, times)
    print( filename + " touched!" )


if __name__ == "__main__":
    entry()
