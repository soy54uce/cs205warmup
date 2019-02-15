from sqlFunction import do_query
from command import Command
from sqlite3 import OperationalError

import re

# Parse user input
# use the command's regular expression to match and execute the corresponding function
def parse_input(my_input_param):
    my_input_param = my_input_param.strip()
    for cmd in Command:
        m = re.match(cmd.reg, my_input_param)
        if m:
            input_array = m.groups()
            try:
                do_query(cmd, input_array) if not cmd.func and len(input_array) > 0 else cmd.func()
            except OperationalError as e:
                print(e)
            return
    print("not a valid command, type help for more information")
