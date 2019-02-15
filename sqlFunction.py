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
    
    # Everything runs on this sequence of if-else statements that 
    # key off the names of the functions calling do_query
    
    
    # Get schema - gives us tables and schemas
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
    
    # Shows all the data in the counties table
    elif(function_name == "show_all_counties"):
        #Print table header
        print("Counties in California:")
        print("{:<5}{:<25}{:<25}{:<20}{:<15}".format("#", "Name", "Seat", "Population", "Founded"))
        print("----------------------------------------------------------------------------------")
        #Print each table row with nice formatting
        for row in c.execute("select * from counties"):
            print("{:<5}{:<25}{:<25}{:<20}{:<15}".format(row[0], row[1], row[2], row[3], row[4]))

    # Shows all the data in the seats table        
    elif(function_name == "show_all_county_seats"):
        #Print table header
        print("County Seats in California:")
        print("{:<5}{:<25}{:<25}{:<20}".format("#", "Name", "Population", "County"))
        print("----------------------------------------------------------------------------------")
        #Print each row in the table
        for row in c.execute("select * from seats"):
            print("{:<5}{:<25}{:<25}{:<20}".format(row[0], row[1], row[2], row[3]))
            
    # Shows a row for any given county
    elif (function_name == "simple_county_query"):
        # Using * for variable parameters for function, so
        # need to call some_input_array nested, like some_input_array[0][1]
        # https://thispointer.com/python-args-how-to-pass-multiple-arguments-to-function
        c.execute("select * from {} where \"Name\" = '{}'".format('counties', some_input_array[0][1]))
        # Store the result of the sql query (list)
        output_array = c.fetchone()
        # Check for valid key
        if (output_array is None):
            print("Invalid county")
        else:
            print("{:<5}{:<25}{:<25}{:<20}{:<15}".format("#", "Name", "Seat", "Population", "Founded"))
            print("----------------------------------------------------------------------------------")
            print("{:<5}{:<25}{:<25}{:<20}{:<15}".format(output_array[0], output_array[1], output_array[2], output_array[3], output_array[4]))
    
    # Shows a row for any given county seat   
    elif (function_name == "simple_county_seat_query"):
        c.execute("select * from {} where \"Name\" = '{}'".format('seats', some_input_array[0][1]))
        # Store the result of the sql query (list)
        output_array = c.fetchone()
        #Check for valid key
        if (output_array is None):
            print("Invalid county seat")
        else:
            print("{:<5}{:<25}{:<25}{:<20}".format("#", "Name", "Population", "County"))
            print("------------------------------------------------------------------------")
            print("{:<5}{:<25}{:<25}{:<20}".format(output_array[0], output_array[1], output_array[2], output_array[3]))
        
    # Show any county attribute   
    elif(function_name == "county_attribute_query"):
        #Check for valid county attribute
        if (some_input_array[0][1] != "population" and some_input_array[0][1] != "established" and some_input_array[0][1] != "name"):
            print("Invalid attribute")
        else :
            c.execute("select {} from {} where \"Name\" = '{}'".format(some_input_array[0][1], 'counties', some_input_array[0][2]))
            #Store the result of the sql query (list)
            output_array = c.fetchone()
            #Check if key was not found
            if (output_array is None):
                print("Invalid county")
            else:
                #Decision tree for attributes formatting
                if (some_input_array[0][1] == "established"):
                    print("{} was established in: {}".format(some_input_array[0][2], output_array[0]))
                elif(some_input_array[0][1] == "population" or some_input_array[0][1] == "seat" or some_input_array[0][1] == "name"):
                    print("The {} of {} is: {}".format(some_input_array[0][1], some_input_array[0][2], output_array[0]))


    # Shows any seat attribute    
    elif(function_name == "county_seat_attribute_query"):
        # Check for valid county attribute
        if (some_input_array[0][1] != "population"  and some_input_array[0][1] != "name"):
            print("Invalid attribute")
        else:
            c.execute("select {} from {} where \"Name\" = '{}'".format(some_input_array[0][1], 'seats', some_input_array[0][2]))
            # Store the result of the sql query (list)
            output_array = c.fetchone()
            if (output_array is None):
                print("Invalid county seat")
            else:
                # Decision tree for attributes
                if (some_input_array[0][1] == "county"):
                    print("{} is the seat of: {}".format(some_input_array[0][2], output_array[0]))
                elif (some_input_array[0][1] == "population" or some_input_array[0][1] == "name"):
                    print("The {} of {} is: {}".format(some_input_array[0][1], some_input_array[0][2], output_array[0]))


    # Shows a county to seat join - i.e., "give me the attribute of the county with this seat
    elif(function_name == "county_to_seat_join"):
        # Check for valid county attribute
        if (some_input_array[0][1] != "population" and some_input_array[0][1] != "established" and some_input_array[0][
            1] != "name"):
            print("Invalid attribute")
        else:
            c.execute("select {}.{} from {}, {} where {}.name = {}.county and {}.name = '{}'".format('counties', some_input_array[0][1], 'counties', 'seats', 'counties', 'seats', 'seats', some_input_array[0][3]))
            #Store the results of the query
            output_array = c.fetchone()
            #Check for valid key
            if (output_array is None):
                print("Invalid county or seat")
            else:
                # Decision tree for attributes formatting
                if (some_input_array[0][1] == "established"):
                    print("The county with seat {} was established in: {}".format(some_input_array[0][3], output_array[0]))
                elif (some_input_array[0][1] == "population" or some_input_array[0][1] == "name"):
                    print("The {} of the county with seat {} is: {}".format(some_input_array[0][1], some_input_array[0][3], output_array[0]))

    
    # Shows a seat to county join - i.e., "give me the attribute of the seat in this county    
    elif(function_name == "seat_to_county_join"):
        # Check for valid county attribute
        if (some_input_array[0][1] != "population" and some_input_array[0][1] != "name"):
            print("Invalid attribute")
        else:
            c.execute("select {}.{} from {}, {} where {}.name = {}.county and {}.name = '{}'".format('seats', some_input_array[0][1], 'counties', 'seats', 'counties', 'seats', 'counties', some_input_array[0][3]))
            # Store the results of the query
            output_array = c.fetchone()
            # Check for valid key
            if (output_array is None):
                print("Invalid county or seat")
            else:
                print("The {} of the {} seat is: {}".format(some_input_array[0][1], some_input_array[0][3],output_array[0]))
    
    return

