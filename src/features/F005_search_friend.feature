
Feature: Search a friend
    *****  User can search for a friend in the list  ******

    Scenario: User has a friend name
        Given User want to see a friend name in the list
        When  User search for a friend by name
        Then  user finds a friend

    Scenario: User has a friend's email
        Given User has a friend email in the list
        When  User search for a friend by email
        Then  user finds a friend email