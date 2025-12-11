Feature: Calculator
  Verify basic arithmetic operations

  Scenario: Add two numbers
    Given the calculator has numbers 3 and 5
    When I add them
    Then the result should be 8

