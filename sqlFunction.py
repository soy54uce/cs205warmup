#! /usr/local/bin/python3

#########################################################
# WARMUP    -    SQL<->PYTHON    -    CS205             #
# CODE TO LINK SQLITE QUERIES & PYTHON                  #
# BARRY SMITH - CS205 - FEBRUARY 2019                   #
#########################################################

from command import Command
import sqlite3

# Function to run queries
def do_query(cmd, *some_input_array):

    # Create a connection & cursor
    conn = sqlite3.connect('cali.db')
    c = conn.cursor()
    # Everything runs on this sequence of if-else statements that 
    # key off the names of the functions calling do_query
    
    # Get schema - gives us tables and schemas
    if (cmd == Command.Schema):

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
    elif(cmd == Command.Counties):
        for row in c.execute("select * from counties"):
            print(row)

    # Shows all the data in the seats table        
    elif(cmd == Command.Seats):
        for row in c.execute("select * from seats"):
            print(row)
            
    # Shows a row for any given county
    elif (cmd == Command.CountyQ):
        # Using * for variable parameters for function, so
        # need to call some_input_array nested, like some_input_array[0][1]
        # https://thispointer.com/python-args-how-to-pass-multiple-arguments-to-function/
        c.execute("select * from {} where \"Name\" = '{}'".format('counties', some_input_array[0][1]))
        print(c.fetchone())
    
    # Shows a row for any given county seat   
    elif (cmd == Command.SeatsQ):
        c.execute("select * from {} where \"Name\" = '{}'".format('seats', some_input_array[0][1]))
        print(c.fetchone())
        
    # Show any county attribute   
    elif(cmd == Command.CountyAQ):
        c.execute("select {} from {} where \"Name\" = '{}'".format(some_input_array[0][1], 'counties', some_input_array[0][2]))
        print(c.fetchone())

    # Shows any seat attribute    
    elif(cmd == Command.SeatsAQ):
        c.execute("select {} from {} where \"Name\" = '{}'".format(some_input_array[0][1], 'seats', some_input_array[0][2]))
        print(c.fetchone())
    
    # Shows a county to seat join - i.e., "give me the attribute of the county with this seat
    elif(cmd == Command.CountyASeatQ):
        c.execute("select {}.{} from {}, {} where {}.name = {}.county and {}.name = '{}'".format('counties', some_input_array[0][1], 'counties', 'seats', 'counties', 'seats', 'seats', some_input_array[0][3]))
        print(c.fetchone())        
    
    # Shows a seat to county join - i.e., "give me the attribute of the seat in this county    
    elif(cmd == Command.SeatsACountyC):
        c.execute("select {}.{} from {}, {} where {}.name = {}.county and {}.name = '{}'".format('seats', some_input_array[0][1], 'counties', 'seats', 'counties', 'seats', 'counties', some_input_array[0][3]))
        print(c.fetchone())      
    return
