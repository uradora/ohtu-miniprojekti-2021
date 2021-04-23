*** Settings ***
Resource  resource.robot
Suite Setup  Run Keywords  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Test Cases ***
Edit Tip Succesfully
    Create User And Login  tip_editor  tip_editor

    Click Link  Add new
    Set Title And Link  changethis  www.changethis.fi
    Click Button  Add new tip

    Click Link  Edit
    Set Title and Link  changedtip  www.changed.fi
    Click Button  Submit changes
    
    Editing Should Succeed With  Tip edited successfully
    Page Should Contain  changedtip

*** Keywords ***
Create User And Login
    [Arguments]  ${username}  ${password}
    Go To Main Page
    Click Link  Register
    Set Username and Password  ${username}  ${password}
    Click Button  Register
    Click Link  Login
    Set Username and Password  ${username}  ${password}
    Click Button  Login

Set Title And Link
    [Arguments]  ${title}  ${link}
    Input Text  title  ${title}
    Input Text  link  ${link} 
 
Editing Should Succeed With
    [Arguments]  ${text}
    Main Page Should Be Open
    Page Should Contain  ${text}