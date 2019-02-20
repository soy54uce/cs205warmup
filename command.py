#! /usr/local/bin/python3

from enum import Enum

# basic regular expression
# Contain at least one uppercase letter
reg_upper = r"(?:\w*[A-Z]+\w*\s?)+"
# All lowercase
reg_lower = r"[a-z]+"

# display all commands and what they do
def display_help():
    print("\n - California County and County Seat Access System\n")
    for cmd in Command:
        print("{:>23s}   {}".format(cmd.title, cmd.man))
    return

# All commands
class Command(Enum):
    Quit = "quit", "exit application", None
    Help = "help", "display all commands and what they do", None, display_help
    Schema = "schema", "list the database tables and column names"
    Counties = "counties", "display entire table of california counties"
    CountyQ = "county COUNTY", "search county table for specified county COUNTY, return entire row", f"(county) ({reg_upper})"
    CountyAQ = "county ATTR COUNTY", "search county table for specified county COUNTY, return ATTR column value", f"(county) ({reg_lower}) ({reg_upper})"
    CountyASeatQ = "county ATTR seat SEAT", "search county table for a specific ATTR, join on seat SEAT", f"(county) ({reg_lower}) (seat) ({reg_upper})"
    Seats = "seats", "display entire table of california county seats"
    SeatsQ = "seat SEAT", "search county seat table for specified county seat SEAT, return entire row", f"(seat) ({reg_upper})"
    SeatsAQ = "seat ATTR SEAT", "search county seat table for specified county seat SEAT, return ATTR column value", f"(seat) ({reg_lower}) ({reg_upper})"
    SeatsACountyC = "seat ATTR county COUNTY", "search seat table for a specific ATTR, join on county COUNTY", f"(seat) ({reg_lower}) (county) ({reg_upper})"

    # The regular expression of the command to match the user input
    def __init__(self, title, man, reg=None, func=None):
        self.title = title
        self.func = func
        self.man = man
        self.reg = f'({title})$' if not reg else reg + '$'
