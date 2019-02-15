from unittest import TestCase
from command import Command
from parse import parse_input
from io import StringIO

import re
import sys

# basic query function,redirect the stdout into string buffer
def test_query(query):
    old_stdout = sys.stdout
    sys.stdout = stdout = StringIO()
    parse_input(query)
    sys.stdout = old_stdout
    return stdout.getvalue().strip()


class Test(TestCase):
    # Command regex pattern test
    def test_regex(self):
        query = "county id Yuba County"
        m = re.match(Command.CountyAQ.reg, query)
        self.assertEqual(m.groups(), ("county", "id", "Yuba County"))

    def test_counties_all(self):
        query = "counties"
        result = test_query(query).split('\n')
        self.assertEqual(len(result), 58)

    def test_seats_all(self):
        query = "seats"
        result = test_query(query).split('\n')
        self.assertEqual(len(result), 58)

    def test_counties_query(self):
        query = "county Solano County"
        result = test_query(query)
        self.assertEqual(result, "('48', 'Solano County', 'Fairfield', '445,458', '1850')")

    def test_seats_query(self):
        query = "seat Woodland"
        result = test_query(query)
        self.assertEqual(result, "('57', 'Woodland', '55,468', 'Yolo County')")

    def test_county_attribute(self):
        query = "county id Solano County"
        result = test_query(query)
        self.assertEqual(result, "('48',)")

    def test_seats_attribute(self):
        query = "seat population Crescent City"
        result = test_query(query)
        self.assertEqual(result, "('7,643',)")

    def test_county_join_seat(self):
        query = "county established seat Downieville"
        result = test_query(query)
        self.assertEqual(result, "('1852',)")

    def test_seat_join_county(self):
        query = "seat population county Alameda County"
        result = test_query(query)
        self.assertEqual(result, "('390,724',)")

    def test_not_found(self):
        query = "seat population county UnKnown County"
        result = test_query(query)
        self.assertEqual(result, "None")

    def test_error(self):
        query = "county Id yuba County"
        result = test_query(query)
        self.assertEqual(result, "not a valid command, type help for more information")

    def test_exception(self):
        query = "seat iid Crescent City"
        result = test_query(query)
        self.assertEqual(result, "no such column: iid")
