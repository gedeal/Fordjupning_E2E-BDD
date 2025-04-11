
Feature: Add a new friend
    *****  User can add a new friend in the list  ******

    Scenario: User adds a friend
        Given User chooses to add a friend
        When  User adds a friend and epost
        Then  user saves friend to the list
        And   user see friend name in the list
