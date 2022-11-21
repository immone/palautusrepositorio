*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Login Page

*** Test Cases ***
Register With Valid Username And Password
   Create User  kalle  kalle123
   Inside Page Should Be Open

Register With Too Short Username And Valid Password
   Create User  kal  kalle123
   Login Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
   Create User  kalle  kallekalle
   Login Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
   Create User  kalle  kallekalle sa123
   Login Should Fail With Message  Password's don't match

*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

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
    Create User  kalle  kalle123
    Go To Login Page
    Login Page Should Be Open


