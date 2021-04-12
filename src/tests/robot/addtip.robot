*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Test Cases ***
Add A Tip Succesfully
    Click Button  Luo uusi vinkki
    Set Title  testi
    Set Link  www.testi.fi
    Submit Tip
    Adding Should Succeed With  www.testi.fi

Adding A Tip With The Same Name
    Click Button  Luo uusi vinkki
    Set Title  testi
    Set Link  www.testi.fi
    Submit Tip
    Adding Should Fail With Message  Tips already contains tip with title Testi

*** Keywords ***
Adding Should Succeed
    [Arguments] ${link}
    Main Page Should Be Open
    Page Should Contain  ${link}

Adding Should Fail With Message
    [Arguments] ${message}
    Form Page Should Be Open
    Page Should Contain  ${message}

Submit Tip
    Click Button  Lähetä

Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Link
    [Arguments]  ${link}
    Input Text  link  ${link}






    