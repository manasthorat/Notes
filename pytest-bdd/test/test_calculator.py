from pytest_bdd import scenarios, given, when, then, parsers
import pytest
from app import calculator

#load the scenarios from the feature file
scenarios('../features/calculator.feature')

#shared storage
@pytest.fixture
def context():
    return {}


@given(parsers.cfparse('the calculator has numbers {a:d} and {b:d}'))
def numbers(context, a, b):
    context['a'] = a
    context['b'] = b

@when('I add them')
def add_numbers(context):
    context['result'] = calculator.add(context['a'], context['b'])

@then(parsers.cfparse('the result should be {result:d}'))
def check_result(context, result):
    assert context['result'] == result
