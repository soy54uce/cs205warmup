

def main():
    my_input = "start"
    while my_input != "quit":
        my_input = input("> ")
        parse_input(my_input)


def parse_input(my_input_param):
    input_array = my_input_param.split()
    if len(input_array) < 2:
        if input_array[0] == "counties":
            show_all_counties()
        elif input_array[0] == "seats":
            show_all_county_seats()
        elif input_array[0] == "help":
            print("help info below")
        else:
            print("not enough args")
    if len(input_array) == 2:
        # simple 2 arg queries
        if input_array[0] == "county":
            simple_county_query(input_array)
        elif input_array[0] == "seat":
            simple_county_seat_query(input_array)
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
    print("checking county table for ", some_input_array[1])
    # build query of county table
    return


def simple_county_seat_query(some_input_array):
    print("checking county seat table for ", some_input_array[1])
    # build query of county seat table
    return


main()
