#! /usr/bin/env python3

import sqlite3

# Test whether SQL and our dbase will work
def do_query_test():
    
    # Create a connection
    conn = sqlite3.connect('cali.db')
    
    # Create a cursor
    c = conn.cursor()

    c.execute('SELECT * FROM COUNTIES')
    for row in c.execute('SELECT * FROM COUNTIES'):
        print(row)
    
def do_query(some_input_array):
    
    # Create a connection
    conn = sqlite3.connect('cali.db')
    
    # Create a cursor
    c = conn.cursor()

    
    
do_query_test()