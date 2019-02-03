#! /usr/local/bin/python3

#########################################################
# WARMUP    -    SQL<->PYTHON    -    CS205             #
# CODE TO LINK SQLITE QUERIES & PYTHON                  #
# BARRY SMITH - CS205 - FEBRUARY 2019                   #
#########################################################

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
def do_query(table, some_input_array):

    # Create a connection & cursor
    conn = sqlite3.connect('cali.db')
    c = conn.cursor()

    # If we're looking for a simple attribute of a single table,
    # there will only be two values in the array

    if len(some_input_array) == 2:
        # "Clearing" code to get rid of brackets/quotes around array vars
        # https://stackoverflow.com/questions/29642188/removing-the-square-brackets-commas-nd-single-quote
        attrib = (some_input_array[0])
        attrib_cleared = (" ".join(some_input_array[0]))
        print(attrib_cleared)
        value_cleared = (" ".join(some_input_array[1]))
        print(value_cleared)

        # Working simple query
        # c.execute("select population from counties where \"County seat\" = 'Sonora'")

        # Working simple query with variable sub
        c.execute("select {} from {} where \"Name\" = {}".format(attrib_cleared, table, value_cleared))

        print(c.fetchone())

        # Working join
        c.execute("select seats.population from counties, seats where counties.name = seats.county and counties.name = 'Yuba County'")
        print(c.fetchone())


# INPUT TESTING BELOW HERE -----------------------------------------

# What table are we going to use? Will depend on input string. Pick this up from Ben's code - here, we'll say it's "county"
table_choice = "county"
if table_choice == "county":
    table = "counties"
else:
    table = "seats"

# Pretend user wants pop of Los Angeles County
some_input_array = ["population"],["'Los Angeles County'"]
do_query(table, some_input_array)
