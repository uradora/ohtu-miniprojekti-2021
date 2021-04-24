*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  %{BROWSER=chrome}
${DELAY}  %{DELAY=0.5 seconds}
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

Create Tips
    Create and Login Default User
    Click Link  Add new
    Input Text  title  testi1
    Input Text  link  www.testi1.fi
    Input Text  tags  tag1, tag2
    Click Button  Add new tip
    Click Link  Add new
    Input Text  title  testi2
    Input Text  link  www.testi2.fi
    Input Text  tags  tag2, tag3
    Click Button  Add new tip
    Click Link  Add new
    Input Text  title  testi3
    Input Text  link  www.testi3.fi
    Input Text  tags  tag3
    Click Button  Add new tip


