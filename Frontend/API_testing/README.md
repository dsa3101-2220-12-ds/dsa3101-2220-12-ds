# Testing of Interaction with mock API

This folder contains the following files for testing purpose: 
1. industry_link2.py, this is the latest version of the industry_link page, with all the api request command implemented and all 6 buttons able to work. 
2. mock_API.py, this is a mock API to simulate what kind of output to expect from backend team. In particular this file will return: 
    - A html which is exactly the same as user output 
    - A dictionary in {school:score} format called score. For simplicity, score is randomly generated. 
    - A dictionary output in {skill:{school:(mod,score)}} format called reco. For simplicity, score is randomly generated. 

    It would be recommened if backend team can simulate this when you are compiling and generaing API so as to minimise the change made to the webpage. However, if we really cannot stick to this format, please let me know. 
3. A dockerfile and a requirement.txt. This is to containerise the mock_API.py, as the API has to become a server first before the web can sned request and receive output. 
4. A readme to explain all things. 

# How to use 
1. Run docker build -t py_mock_api . to create image 
2. Run docker --name api -d -p 9001:5000 py_mock_api to create container 
3. Now if you go to http://localhost:9001/api?input=hello, you should be able to see a series of output, this is what the mock_API.py return, and this is where the industry_link2.py will send request on. 
4. Now go back to your terminal and run python industry_link2.py, and go to http://127.0.0.1:8050/ (or wherever your terminal tell you), you will see the industry_link page. It has been designed in a sense that whatever the user key in, it will generate a ranking for you. This is also based on my understanding to how the backend team model is working. 
5. Click on any of the 6 buttons, you will see a popup window with the following info: 
    - Header called "How does the ranking work?"
    - A static description about how to elaborate the ranking. This part the context can be edited later. 
    - An inner html that shows exactly same content as the user input. This is an inner html so later on can replace with whatever html output backend team has. 
    - A list of skill: mod + score particularly for that school. 

# Others
This version of industry_link page has not been updated onto the official web that run with app.py. Hence, you will only see the older version there. Please only test the mock API with this version and let us know if you have any question! :) 
