*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  chrome
${DELAY}  0.5 seconds
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
