

def main():
    my_input = input("> ")
    while my_input != "quit":
        parse_input(my_input)
        my_input = input("> ")


def parse_input(my_input_param):
    input_array = my_input_param.split()
    print(input_array)
    x = 0
    while x < len(input_array):
        has_upper = not input_array[x].islower()

        if x+1 < len(input_array):
            next_has_upper = not input_array[x+1].islower()
        else:
            next_has_upper = False
        if has_upper and next_has_upper:
            input_array[x] = input_array[x] + ' ' + input_array[x+1]
            input_array.pop(x+1)
            x = x - 1
        x = x + 1
    print(input_array)

    if len(input_array) < 2:
        if input_array[0] == "counties":
            show_all_counties()
        elif input_array[0] == "seats":
            show_all_county_seats()
        elif input_array[0] == "schema":
            get_schema()
        elif input_array[0] == "help":
            display_help()
        else:
            print("not a valid command, type help for more information")
    elif len(input_array) == 2:
        # simple 2 arg queries
        if input_array[0] == "county":
            simple_county_query(input_array)
        elif input_array[0] == "seat":
            simple_county_seat_query(input_array)
        else:
            print("not a valid command, type help for more information")
    elif len(input_array) == 3:
        if input_array[0] == "county":
            county_attribute_query(input_array)
        elif input_array[0] == "seat":
            county_seat_attribute_query(input_array)
        else:
            print("not a valid command, type help for more information")
    elif len(input_array) == 4:
        if (input_array[0] == "county") & (input_array[2] == "seat"):
            county_to_seat_join(input_array)
        elif (input_array[0] == "seat") & (input_array[2] == "county"):
            seat_to_county_join(input_array)
        else:
            print("not a valid command, type help for more information")
    return


def display_help():
    print("\n - California County and County Seat Access System\n")
    command_dict = {
        "quit": "exit application",
        "help": "display all commands and what they do",
        "schema": "list the database tables and column names",
        "counties": "display entire table of california counties",
        "county COUNTY": "search county table for specified county COUNTY, return entire row",
        "county ATTR COUNTY": "search county table for specified county COUNTY, return ATTR column value",
        "county ATTR seat SEAT": "search county table for a specific ATTR, join on seat SEAT",
        "seats": "display entire table of california county seats",
        "seat SEAT": "search county seat table for specified county seat SEAT, return entire row",
        "seat ATTR SEAT": "search county seat table for specified county seat SEAT, return ATTR column value",
        "seat ATTR county COUNTY": "search seat table for a specific ATTR, join on county COUNTY"
        # will add more help info after i get a schema of the database
    }
    for command in command_dict:
        print("{:>23s}   {}".format(command, command_dict[command]))
    return


def get_schema():
    print("schema here")
    return


def show_all_counties():
    print("searching county table")
    # query SELECT * FROM county/counties
    return


def show_all_county_seats():
    print("displaying seats table")
    # query SELECT * FROM seats
    return


def simple_county_query(some_input_array):
    print("checking county table for", some_input_array[1])
    # build and execute query of county table
    return


def simple_county_seat_query(some_input_array):
    print("checking county seat table for", some_input_array[1])
    # build and execute query of county seat table
    return


def county_attribute_query(some_input_array):
    print("checking county table for column", some_input_array[1], "where county is", some_input_array[2])
    return


def county_seat_attribute_query(some_input_array):
    print("checking county seat table for column", some_input_array[1], "where county seat is", some_input_array[2])


def county_to_seat_join(some_input_array):
    print("checking county table for", some_input_array[1], "where county seat is", some_input_array[3])
    return


def seat_to_county_join(some_input_array):
    print("checking county seat table for", some_input_array[1], "where county is", some_input_array[3])
    return


# main()
