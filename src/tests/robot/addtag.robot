*** Settings ***
Resource  resource.robot
Suite Setup  Run Keywords  Open And Configure Browser  Create and Login Default User
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Test Cases ***
Add Tags Succesfully
    Click Link  Add new
    Set Title Link and Tag  taginLisäämisTesti  www.taginLisäämisTesti.fi  tag1, tag2
    Click Button  Add new tip
    Adding Should Succeed With  www.taginLisäämisTesti.fi

*** Keywords ***
Adding Should Succeed With
    [Arguments]  ${link}
    Main Page Should Be Open
    Page Should Contain  ${link}
    Click Button  Filter
    Click Button  tag2
    Click Link  Remove

Set Title Link and Tag
    [Arguments]  ${title}  ${link}  ${tags}
    Input Text  title  ${title}
    Input Text  link  ${link}
    Input Text  tags  ${tags}
