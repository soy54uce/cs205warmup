import main


def test_schema():
    input_string = "schema"
    main.parse_input(input_string)


def test_help():
    input_string = "help"
    main.parse_input(input_string)


test_help()
test_schema()
