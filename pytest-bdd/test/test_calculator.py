from pytest_bdd import scenarios, given, when, then, parsers
import pytest
from app import calculator

#load the scenarios from the feature file
scenarios('../features/calculator.feature')

#shared storage
@pytest.fixture
def context():
    return {}


# GIVEN step: parameterized to accept integers a and b
@given(parsers.cfparse('the calculator has numbers {a:d} and {b:d}'))
def given_numbers(context, a, b):
    # store parsed integers into context
    context['a'] = a
    context['b'] = b
# WHEN step for addition
@when('I add them')
def when_add(context):
    context['sum_result'] = calculator.add(context['a'], context['b'])

# THEN step for addition (parameterized expected value)
@then(parsers.cfparse('the addition result should be {expected:d}'))
def then_check_add(context, expected):
    assert context['sum_result'] == expected, f"addition expected {expected}, got {context['sum_result']}"


# WHEN step for multiplication
@when('I multiply them')
def when_multiply(context):
    context['product_result'] = calculator.multiply(context['a'], context['b'])

# THEN step for multiplication (parameterized expected value)
@then(parsers.cfparse('the multiplication result should be {expected:d}'))
def then_check_mult(context, expected):
    assert context['product_result'] == expected, f"multiplication expected {expected}, got {context['product_result']}"
