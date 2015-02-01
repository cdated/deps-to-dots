#!/usr/bin/env python

import sys
import re
import os

files_in_tree = {}
inspected = {}

include_regex = r'#include [<"](.*)[>"]'

def inspect_file(file_name):
    """ Recursively evaluate the file #includes and throughout the project. """

    # Ensure the inspected files are within the project tree
    if not file_name in files_in_tree:
        return

    file_obj = open(files_in_tree[file_name])

    inspected[file_name] = True
    for line in file_obj:
        match = re.match(include_regex, line)
        if match:
            dep = match.group(1)
            print('\t"%s" -> "%s"' % (file_name, dep))

            if not dep in inspected:
                inspect_file(dep)

    file_obj.close()

def record_project_files(root_path):
    """ Walk the root path of the project to keep a dict of files within
        the project. This keeps the script in the bounds of the project. """

    for root, dirs, files in os.walk(root_path):
        for name in files:
            if not ".git" in root:
                abs_file_path = os.path.abspath(os.path.join(root, name))
                if not name in files_in_tree:
                    files_in_tree[name] = abs_file_path

def usage():
    """ Let the user know the expected runtime args """

    if len(sys.argv) < 3:
        print("Usage: ./make_dot.py [top_level_file] [project_root]")
        sys.exit()

def main():
    usage()

    initial_file = sys.argv[1]
    root_path = sys.argv[2]

    files_in_tree[initial_file] = initial_file
    record_project_files(root_path)

    print('digraph "source tree" {')

    # Start with the user specified main file
    # and recurse through it's included files
    inspect_file(initial_file)

    # Check the remaining files in the project
    for source_file in files_in_tree:
        if not source_file in inspected:
            inspect_file(source_file)
    print('}')

if __name__ == '__main__':
    main()