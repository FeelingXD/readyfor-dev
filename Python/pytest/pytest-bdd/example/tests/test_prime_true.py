import pytest
from pytest_bdd import scenario, given, when, then

from src.prime import is_prime


@pytest.fixture
def context():
    return {"number":2}

@scenario("features/prime-true.feature", "Validate")
def test_prime():
    pass

@given("take 2")
def step_take_two(context):
    context["number"] = 2
    # raise NotImplementedError(u'STEP: Given : take 2')


@when("validate prime")
def step_validate_prime(context):
    context["result"]=is_prime(context["number"])
    # raise NotImplementedError(u'STEP: When : validate prime')


@then("return true")
def step_return_impl(context):
    assert context["result"]==True
    # raise NotImplementedError(u'STEP: Then : return true')