
Feature: Search a friend
    *****  User can search for a friend in the list  ******

    Scenario: User has a friend's name
        Given User has a friend in the list
        When  User search for a friend by name
        Then  user finds a friend

    Scenario: User has a friend's email
        Given User has a friend in the list
        When  User search for a friend by email
        Then  user finds a friend