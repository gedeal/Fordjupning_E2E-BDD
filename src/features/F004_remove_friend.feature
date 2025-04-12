
Feature: Remove a friend
    *****  User can remove a friend in the list  ******

    Scenario: User has a friend in the list and removes it
        Given User has a friend in the list
        When  User removes the friend
        Then  friend name is not in the list
