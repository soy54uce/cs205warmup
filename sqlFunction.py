#! /usr/local/bin/python3

#########################################################
# WARMUP    -    SQL<->PYTHON    -    CS205             #
# CODE TO LINK SQLITE QUERIES & PYTHON                  #
# BARRY SMITH - CS205 - FEBRUARY 2019                   #
#########################################################

import sqlite3


# Function to run queries
def do_query(function_name, *some_input_array):

    # Create a connection & cursor
    conn = sqlite3.connect('cali.db')
    c = conn.cursor()
    if (function_name == "get_schema"):

        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        print("Here are the tables:")
        print(c.fetchall())

        print("Here is the {} schema:".format("counties"))
        for row in c.execute("PRAGMA table_info('counties')").fetchall():
            print(row)

        print("Here is the {} schema:".format("county seats"))
        for row in c.execute("PRAGMA table_info('seats')").fetchall():
            print(row)


    elif (function_name == "simple_county_query"):
        # Using * for variable parameters for function, so
        # need to call some_input_array nested, like some_input_array[0][1]
        # https://thispointer.com/python-args-how-to-pass-multiple-arguments-to-function/
        c.execute("select * from {} where \"Name\" = '{}'".format('counties', some_input_array[0][1]))
        print(c.fetchone())
    elif(function_name == "county_attribute_query"):
        c.execute("select {} from {} where \"Name\" = '{}'".format(some_input_array[0][1], 'counties', some_input_array[0][2]))
        print(c.fetchone())
    return


# INPUT TESTING BELOW HERE -----------------------------------------
