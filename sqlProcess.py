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

    #table = ('counties' )
    table = (some_input_array[0])
    # print(some_input_array[0])

    # "Clearing" code to get rid of brackets/quotes around array vars
    # https://stackoverflow.com/questions/29642188/removing-the-square-brackets-commas-and-single-quote
    table_cleared = (" ".join(some_input_array[0]))
    # print(table_cleared)
    attrib = (some_input_array[1])
    attrib_cleared = (" ".join(some_input_array[1]))
    # print(attrib_cleared)

    #u = (some_input_array[1],)

    # Working simple query
    # c.execute("select population from counties where \"County seat\" = 'Sonora'")

    # Working simple query with variable sub
    c.execute("select population from {} where \"County seat\" = {}".format(table_cleared, attrib_cleared))

    print(c.fetchone())

    # Working join
    c.execute("select seats.population from counties, seats where counties.name = seats.county and counties.name = 'Yuba County'")
    print(c.fetchone())


# some_input_array = []
some_input_array = ["counties"],["'Sonora'"]
do_query(some_input_array)
