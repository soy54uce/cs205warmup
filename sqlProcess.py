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

    if len(some_input_array) < 2:



        if (some_input_array[0] == "schema"):
            # Way to get schema is a little odd...have to use "PRAGMA" as below
            # https://www.tomordonez.com/get-schema-sqlite-python.html
            if(table == "counties"):
                print("Here is the {} schema:".format(table))
                for row in c.execute("PRAGMA table_info('counties')").fetchall():
                    print(row)
            elif(table == "seats"):
                print("Here is the {} schema:".format(table))
                for row in c.execute("PRAGMA table_info('seats')").fetchall():
                    print(row)
            print()

        elif(some_input_array[0] == "tables"):
            c.execute("SELECT name FROM sqlite_master WHERE type='table';")
            print("Here are the tables:")
            print(c.fetchall())
            print()


    elif len(some_input_array) == 2:
        # "Clearing" code to get rid of brackets/quotes around array vars
        # https://stackoverflow.com/questions/29642188/removing-the-square-brackets-commas-nd-single-quote
        attrib = (some_input_array[0])
        attrib_cleared = (" ".join(attrib))
        #print(attrib_cleared)
        value_cleared = (" ".join(some_input_array[1]))
        #print(value_cleared)

        # Working simple query
        # c.execute("select population from counties where \"County seat\" = 'Sonora'")

        # Working simple query with variable sub
        c.execute("select {} from {} where \"Name\" = {}".format(attrib_cleared, table, value_cleared))
        print("Here is the {} of {}:".format(attrib_cleared, value_cleared))
        print(c.fetchone())
        print()


    else:
        attrib = (some_input_array[0])
        attrib_cleared = (" ".join(attrib))
        join_value = (some_input_array[1])
        join_value_cleared = (" ".join(join_value))
        #value_cleared = (" ".join(some_input_array[2]))
        value_cleared = some_input_array[2]

        
        if join_value_cleared == "County seat":
            table1 = "seats"
            table2 = "counties"
        
            print(attrib_cleared)
            print(table1)
            print(table2)
            print(value_cleared)
            # Extra work here to strip off the array brackets alone (leaving single quotes)
            value_cleared = str(value_cleared)[1:-1]
            print(value_cleared)
            
            print()
            print("Here is the population of the {} of {}:".format(join_value_cleared, value_cleared))
            c.execute("select {}.{} from {}, {} where {}.name = {}.county and {}.name = {}".format(table1, attrib_cleared, table2, table1, table2, table1, table2, value_cleared))  
            print(c.fetchone())
      
        
        
        # Working join - for input like <population seat Yuba County>
        # This takes three inputs? Population, seat, and Yuba County?
        print()
        c.execute("select seats.population from counties, seats where counties.name = seats.county and counties.name = 'Yuba County'")
        print("Here is the population the county seat of Yuba County:")
        print(c.fetchone())




# INPUT TESTING BELOW HERE -----------------------------------------

# What table are we going to use? Will depend on input string. Pick this up from Ben's code - here, we'll say it's "county"
table_choice = "county"
if table_choice == "county":
    table = "counties"
else:
    table = "seats"

# List tables
first_input_array = ["tables"]
do_query(table, first_input_array)

# Show schema of counties
second_input_array = ["schema"]
do_query(table, second_input_array)

# Show schema of seats
third_input_array = ["schema"]
table = "seats"
do_query(table, third_input_array)

# Pretend user wants pop of Los Angeles County: an
# "attribute of a county" query
table = "counties"
fourth_input_array = ["population"],["'Los Angeles County'"]
do_query(table, fourth_input_array)

fifth_input_array = ["established"], ["'Marin County'"]

sixth_input_array = ["population"], ["County seat"], ["Alameda County"]
do_query(table, sixth_input_array)
