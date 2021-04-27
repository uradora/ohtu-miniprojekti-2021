*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Test Cases ***
Register Successfully
    Click Link  Register
    Set Username and Password  maija  Oupi0Vea
    Click Button  Register
    Has Flash Message  Registration successful

Login Successfully
    Click Link  Login
    Set Username and Password  maija  Oupi0Vea
    Click Button  Login
    Has Flash Message  Login successful

User Can Only See Own Tips
    Click Link  Register
    Set Username and Password  new_user  new_password
    Click Button  Register
    Click Link  Login
    Set Username and Password  new_user  new_password
    Click Button  Login
    Page Should Not Contain  www.testi.fi
    
Login Incorrect Password
    Click Link  Login
    Set Username and Password  maija  Oupi0Veaa
    Click Button  Login
    Has Flash Message  Login failed

Register Existing Username
    Click Link  Register
    Set Username and Password  maija  salasana123
    Click Button  Register
    Has Flash Message  Username is taken

*** Keywords ***
Has Flash Message
    [Arguments]  ${text}
    Page Should Contain  ${text}

