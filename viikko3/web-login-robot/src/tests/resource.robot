*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:8000
${BROWSER}  headlesschrome
${DELAY}  0.0 seconds
${HOME URL}  http://${SERVER}
${LOGIN URL}  http://${SERVER}/login
${REGISTER URL}  http://${SERVER}/register

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Login Page Should Be Open
    Title Should Be  Login

Main Page Should Be Open
    Title Should Be  Ohtu Application main page

Inside Page Should Be Open
    Title Should Be  Welcome to Ohtu Application!

Go To Login Page
    Go To  ${LOGIN URL}

Go To Home Page
    Go To  ${HOME URL}

Register Page Should Be Open
    Title Should Be  Register

Register User
   [Arguments]  ${username}  ${pwo}  ${pwtkk}
   Go To  ${REGISTER URL}
   Input Text  username  ${username}
   Input Password  password  ${pwo}
   Input Password  password_confirmation  ${pwtkk}
   Click Button  Register
