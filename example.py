from unittest import mock
import pytest

DATA = (
    (
        # case_name
        "case1: Success",
        # input for function
        {"number": 11},
        # mock_value_for_fucntion
        {"add_one": 12},
        # expect value
        True,
    ),
    (
        # case_name
        "case2: False",
        # input for function
        {"number": 10},
        # mock_value_for_fucntion
        {"add_one": 12},
        # expect value
        False,
    ),
)

# external function
def add_one(number):
    return number + 1


# function need write unittest
def print_plus(number):
    total = add_one(number)
    print(total)
    return total == number + 1


@pytest.mark.parametrize(["case", "input_params", "mock_value", "expect"], DATA)
def test_print_plus(case, input_params, mock_value, expect):
    # mock value return from add_one in function to test
    mock.patch("example.add_one", return_value=mock_value.get("add_one")).start()
    # get return value in function to test
    return_value = print_plus(input_params.get("number"))
    assert return_value == expect
