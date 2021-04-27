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
    Main Page Open With Flash  Registration successful

Login Successfully
    Click Link  Login
    Set Username and Password  maija  Oupi0Vea
    Click Button  Login
    Main Page Open With Flash  Login successful

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
    Main Page Open With Flash  Login failed

Register Existing Username
    Click Link  Register
    Set Username and Password  maija  salasana123
    Click Button  Register
    Main Page Open With Flash  Register failed

*** Keywords ***
Main Page Open With Flash
    [Arguments]  ${text}
    Main Page Should Be Open
    Page Should Contain  ${text}

