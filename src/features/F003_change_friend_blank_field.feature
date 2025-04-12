
Feature: Change a friend's information - error message
    *****  If User changes friends name & epost but leave one blank an error message shows ******

    Scenario: User has a friend name in list
        Given User chooses to change friend name
        When  User erases the friend name
        Then  system shows error message - name

    Scenario: User has a friend email in list
        Given User chooses to change friend email
        When  User erases the friend email
        Then  system shows error message - email