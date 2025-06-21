Feature: 계산기
  Scenario: 더하기
    Given 두 숫자가 주어진다
    When 주어진 숫자를 더한다
    Then 주어진 두 숫자의 합이 일치한다.

    @success
    Scenario: A rule for valid cases
      Given 2 and 5
      When I add given numbers
      Then return 7