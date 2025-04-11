
Feature: Change a friend's information
    *****  User can change the friends name & epost  ******

    Scenario: User has a friend in list
        Given User chooses to change friend's info
        When  User changes the friend's name and epost
        Then  user saves changes to the list
        And   user see friend's changes in the list
