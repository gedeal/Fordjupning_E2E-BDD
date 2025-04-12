
Feature: Add a new friend with error
    *****  User add a new friend with error  ******

    Scenario: User adds a friend name - email with error
        Given User chooses to add a friend name
        When  User adds a name
        And   User do not add an email
        Then  System shows error message (name)

    Scenario: User adds a friend email - name with error
        Given User chooses to add a friend email
        When  User do not add a name
        And   User adds a email
        Then  System shows error message (email)
