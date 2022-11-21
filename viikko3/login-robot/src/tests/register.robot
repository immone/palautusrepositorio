*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Keywords ***
Input New Command And Create User
    Input New Command  eka  satan666

*** Test Cases ***
Register With Valid Username And Password
    Input New Command  eka  satan666

Register With Already Taken Username And Valid Password
    Input New Command  eka  satan6666
    Output Should Contain  User with username eka already exists

Register With Too Short Username And Valid Password
    Input New Command  ek  satan666
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input New Command  kolmevittu  sat
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command  toka2  satansatan
