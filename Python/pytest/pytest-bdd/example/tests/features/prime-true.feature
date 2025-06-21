# Created by wlals at 25. 5. 27.
Feature: validate prime
  Scenario: Validate
    Given take 2
    When validate prime
    Then return true