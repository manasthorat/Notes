Feature: Calculator operations using Scenario Outline
  Verify add and multiply with multiple input rows

  Scenario Outline: Add and multiply two numbers
    Given the calculator has numbers <a> and <b>
    When I add them
    Then the addition result should be <sum>

    When I multiply them
    Then the multiplication result should be <product>

  Examples:
    | a  | b  | sum | product |
    | 2  | 3  | 5   | 6       |
    | 10 | 5  | 15  | 50      |
    | -1 | 4  | 3   | -4      |