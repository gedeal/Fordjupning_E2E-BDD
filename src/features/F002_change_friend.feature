
Feature: Change a friend's information
    *****  User can change the friends name & epost  ******

    Scenario: User has a friend in list
        Given User chooses to change friends info
        When  User changes the friends name and epost
        Then  user saves changes to the list
        And   user see friends changes in the list
