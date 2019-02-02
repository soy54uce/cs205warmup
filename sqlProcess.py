#########################################################
# WARMUP - SQL<->PYTHON - CS205                         #
# CODE TO LINK SQLITE QUERIES & PYTHON                  #
# BARRY SMITH - FEBRUARY 2019                           #
#########################################################

#! /usr/bin/env python3

import sqlite3

# Test function: will SQL and our dbase will work?
def do_query_test():

    # Create a connection & cursor
    conn = sqlite3.connect('cali.db')
    c = conn.cursor()

    c.execute('SELECT * FROM COUNTIES')
    for row in c.execute('SELECT * FROM COUNTIES'):
        print(row)

# Function to run queries
def do_query(some_input_array):

    # Create a connection & cursor
    conn = sqlite3.connect('cali.db')
    c = conn.cursor()


    # Effort to sanitize SQL
    table = ('counties', )
    t = (some_input_array[0],)
    #u = (some_input_array[1],)
    #c.execute("SELECT population FROM COUNTIES WHERE name = '?'", (t,))

    # Working simple query
    c.execute("select population from counties where \"County seat\" = 'Sonora'")
    print(c.fetchone())

    # Working join
    c.execute("select seats.population from counties, seats where counties.name = seats.county and counties.name = 'Yuba County'")
    print(c.fetchone())


# some_input_array = []
some_input_array = ["Los Angeles"]
do_query(some_input_array)
