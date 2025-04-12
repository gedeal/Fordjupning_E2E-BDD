# Fordjupning_E2E-BDD

Veckouppgift 6 -  Vecka 15

# Tips

### Usefull commands:

    clear | behave .\src

    clear | behave .\src\features\F001_login.feature 

    playwright codegen  https://forverkliga.se/JavaScript/my-contacts/#/

### Delay test

    from time import sleep
    .
    .
    sleep(0)

### choose between nth places
    context.page.get_by_role("textbox").nth(1).fill("EMAIL")
