*** Settings ***
Resource  resource.robot
Suite Setup  Run Keywords  Open And Configure Browser  Create Tips
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Test Cases ***
Filter Tips Succesfully
    Click Button  Filter
    Click Button  tag1
    Page Should Contain  testi1
    Page Should Not Contain  testi2
    Page Should Not Contain  testi3
    Click Button  Filter by: tag1
    Click Button  tag3
    Page Should Not Contain  testi1
    Page Should Contain  testi2
    Page Should Contain  testi3
    Click Button  Filter by: tag3
    Click Button  Disable
    Page Should Contain  testi1
    Page Should Contain  testi2
    Page Should Contain  testi3


*** Keywords ***
Adding Should Succeed With
    [Arguments]  ${link}
    Main Page Should Be Open
    Page Should Contain  ${link}

Adding Should Fail With Message
    [Arguments]  ${message}
    Tip Form Page Should Be Open
    Page Should Contain  ${message}

Set Title And Link
    [Arguments]  ${title}  ${link}
    Input Text  title  ${title}
    Input Text  link  ${link}   
