

def main():
    my_input = input("> ")
    while my_input != "quit":
        parse_input(my_input)
        my_input = input("> ")


def parse_input(my_input_param):
    input_array = my_input_param.split()
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
    if len(input_array) == 2:
        # simple 2 arg queries
        if input_array[0] == "county":
            simple_county_query(input_array)
        elif input_array[0] == "seat":
            simple_county_seat_query(input_array)
    return


def display_help():
    print("California County and County Seat Access System\n")
    command_dict = {
        "help": "display all commands and what they do",
        "schema": "list the database tables and column names",
        "counties": "display entire table of california counties",
        "seats": "display entire table of california county seats",
        "county COUNTY": "search county table for specified county COUNTY, return entire row",
        "county ATTR COUNTY": "search county table for specified county COUNTY, return ATTR column value",
        "seat SEAT": "search county seat table for specified county seat SEAT, return entire row",
        "seat ATTR SEAT": "search county seat table for specified county seat SEAT, return ATTR column value",
        # will add more help info after i get a schema of the database
    }
    for command in command_dict:
        print("{:>18s}   {}".format(command, command_dict[command]))
    return


def get_schema():
    print("schema here")
    return


def show_all_counties():
    print("searching county table")
    # query SELECT * FROM county
    return


def show_all_county_seats():
    print("displaying seats table")
    # query SELECT * FROM seats
    return


def simple_county_query(some_input_array):
    print("checking county table for", some_input_array[1])
    # build query of county table
    return


def simple_county_seat_query(some_input_array):
    print("checking county seat table for", some_input_array[1])
    # build query of county seat table
    return


main()
