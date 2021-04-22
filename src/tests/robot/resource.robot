*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  %{BROWSER=chrome}
${DELAY}  %{DELAY=1 seconds}
${HOME URL}  http://${SERVER}


*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Set Window Size  1400  600
    Set Selenium Speed  ${DELAY}

Go To Main Page
    Go To  ${HOME URL}

Main Page Should Be Open
    Title Should Be  My tips - Reading Tips

Tip Form Page Should Be Open 
    Title Should Be  Add new tip - Reading Tips

Set Username and Password
    [Arguments]  ${username}  ${password}
    Input Text  username  ${username}
    Input Text  password  ${password}

Create and Login Default User
    Go To Main Page
    Click Link  Register
    Set Username and Password  default_user  default_password
    Click Button  Register
    Click Link  Login
    Set Username and Password  default_user  default_password
    Click Button  Login

