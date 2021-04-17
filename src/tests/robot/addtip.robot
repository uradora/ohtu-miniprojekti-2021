*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Test Cases ***
Add A Tip Succesfully
    Click Link  Add new
    Set Title and Link  testi  www.testi.fi
    Click Button  Add new tip
    Adding Should Succeed With  www.testi.fi

Adding A Tip With The Same Name
    Click Link  Add new
    Set Title and Link  testi  www.testi.fi
    Click Button  Add new tip
    Adding Should Fail With Message  Tips already contains tip with title testi

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