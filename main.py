#! /usr/local/bin/python3

from parse import parse_input

def main():
    my_input = input("> ")
    while my_input != "quit":
        parse_input(my_input)
        my_input = input("> ")

main()
