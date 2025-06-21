import pytest
from pytest_bdd import scenario, given, when, then

from src.Calculator import Calculator


@pytest.fixture
def calculator_context():
    """계산기 테스트를 위한 컨텍스트"""
    return {
        'number1': None,
        'number2': None,
        'result': None
    }

@scenario('features/calculator.feature', '더하기')
def test_addition():
    pass

@given("두 숫자가 주어진다")
def step_given_numbers(calculator_context):  # 픽스처 사용
    calculator_context['number1'] = 5
    calculator_context['number2'] = 3

@when("주어진 숫자를 더한다")
def step_when_add_numbers(calculator_context):  # 픽스처 사용
    calculator_context['result'] = Calculator.add(number1=calculator_context['number1'], number2=calculator_context['number2'])

@then("주어진 두 숫자의 합이 일치한다.")
def step_then_sum(calculator_context):  # 픽스처 사용
    assert calculator_context['result'] == 8

@scenario('features/calculator.feature', 'A rule for valid cases')
def test_success():
    pass

@given("2 and 5")
def step_impl(calculator_context):
    calculator_context['number1'] = 2
    calculator_context['number2'] = 5

@when("I add given numbers")
def step_impl(calculator_context):
    calculator_context['result'] = calculator_context['number1'] + calculator_context['number2']


@then("return 7")
def step_impl(calculator_context):
    assert calculator_context['result'] == 7
