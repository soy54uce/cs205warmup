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

    table = ('counties', )
    t = (some_input_array[0],)
    #u = (some_input_array[1],)
    #c.execute("SELECT population FROM COUNTIES WHERE name = '?'", (t,))
    #c.execute("SELECT population FROM COUNTIES WHERE name = 'Los Angeles'")
    c.execute("select population from counties where \"County seat\" = 'Sonora'")

    print(c.fetchone())

    
    
#do_query_test()
# some_input_array = []
some_input_array = ["Los Angeles"]
# some_input_array[1] = "Los Angeles"
do_query(some_input_array)