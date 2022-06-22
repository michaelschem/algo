#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'contacts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY queries as parameter.
#

class ContactBook:
    def __init__(self) -> None:
        self.contacts = {}

    def add(self, name):
        indexes = [name[:i] for i in range(1, len(name)+1)]
        for index in indexes:
            if self.contacts.get(index):
                self.contacts[index] += 1
            else:
                self.contacts[index] = 1

    def find(self, name):
        return self.contacts.get(name, 0)

def contacts(queries):
    contact_book = ContactBook()
    for command, name in queries:
        if command == 'add':
            contact_book.add(name)
        if command == 'find':
            yield contact_book.find(name)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    print('\n'.join(map(str, result)))
    print('\n')
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
