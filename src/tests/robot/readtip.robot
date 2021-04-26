*** Settings ***
Library  DateTime
Resource  resource.robot
Suite Setup  Run Keywords  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page


*** Test Cases ***
Mark Tip As Read Succesfully
    ${date}  Get Current Date  result_format=%d/%m/%Y

    Create User And Login  tip_reader  tip_reader
    Add New Tip  readthis  www.readthis.fi
    Marking Tip Should Succeed With Current Date  ${date}


*** Keywords ***
Create User And Login
    [Arguments]  ${username}  ${password}
    Click Link  Register
    Set Username and Password  ${username}  ${password}
    Click Button  Register
    Click Link  Login
    Set Username and Password  ${username}  ${password}
    Click Button  Login

Add New Tip
    [Arguments]  ${title}  ${link}
    Click Link  Add new
    Input Text  title  ${title}
    Input Text  link  ${link}
    Click Button  Add new tip

Marking Tip Should Succeed With Current Date
    [Arguments]  ${date} 
    Click Link  Mark as read
    Main Page Should Be Open
    Page Should Contain  ${date}