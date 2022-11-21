*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Register With Valid Username And Password
   Register User  kallekallekalle123ds  kalle123  kalle123
   Register Page Should Be Open

Register With Too Short Username And Valid Password
   Register User  kj  kalle123  kalle123
   Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
   Register User  kalle  kall  kall
   Register Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
   Register User  kalleabjsjsnb  kallekalle  sa123asd31
   Register Should Fail With Message  Passwords don't match

Login After Successful Registration
   Register User  kallex  kallex111  kallex111
   Go To Login Page
   Set Username  kallex
   Set Password  kallex111
   Submit Credentials
   Login Should Succeed

Login After Failed Registration
   Register User  kallekallekalle2  ka  ka
   Register Page Should Be Open
   Go To Login Page
   Set Username  kallekallekalle2
   Set Password  ka
   Submit Credentials
   Login Should Fail With Message  Invalid username or password


*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Create User And Go To Login Page
    Register User  kalle  kalle123  kalle123
    Go To Login Page
    Login Page Should Be Open

