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
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Go To Main Page
    Go To  ${HOME URL}

Main Page Should Be Open
    Title Should Be  My tips - Reading Tips

Tip Form Page Should Be Open 
    Title Should Be  Add new tip - Reading Tips
