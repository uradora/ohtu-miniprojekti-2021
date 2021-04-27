*** Settings ***
Resource  resource.robot
Suite Setup  Run Keywords  Open And Configure Browser  Create and Login Default User
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Test Cases ***
Add A Tip Succesfully
    Click Link  Add new
    Set Title and Link  testi  www.addingtesti.fi
    Click Button  Add new tip
    Adding Should Succeed With  www.addingtesti.fi

Adding A Tip With The Same Name
    Click Link  Add new
    Set Title and Link  testi  www.addingtesti.fi
    Click Button  Add new tip
    Adding Should Fail With Message  Tips already contains tip with title testi

Remove Tip
    Click Link  Remove
    Page Should Not Contain  www.addingtesti.fi

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
