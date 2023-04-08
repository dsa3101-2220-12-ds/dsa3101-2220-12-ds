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
1. Run docker build --no-cache -t py_mock_api . to create image 
2. Run docker run --name api -d -p 9001:5000 py_mock_api to create container 
3. Now if you go to http://localhost:9001/api?input=hello, you should be able to see a series of output, this is what the mock_API.py return, and this is where the industry_link2.py will send request on. 
4. Now go back to your terminal and run python industry_link2.py, and go to http://127.0.0.1:8050/ (or wherever your terminal tell you), you will see the industry_link page. It has been designed in a sense that whatever the user key in, it will generate a ranking for you. This is also based on my understanding to how the backend team model is working. 
5. Click on any of the 6 buttons, you will see a popup window with the following info: 
    - Header called "How does the ranking work?"
    - A static description about how to elaborate the ranking. This part the context can be edited later. 
    - An inner html that shows exactly same content as the user input. This is an inner html so later on can replace with whatever html output backend team has. 
    - A list of skill: mod + score particularly for that school. 

# Others
This version of industry_link page has not been updated onto the official web that run with app.py. Hence, you will only see the older version there. Please only test the mock API with this version and let us know if you have any question! :) 

# Update as of 1 Apr 2023 8:22pm by Ernest:
I have updated the mock_API.py and Dockerfile, as well as put the NER and Word2Vec models into this directory. Do not remove or rename them. Everything works fine now, except the fact that the result takes 1-2 minutes to load and the webpage should reflect some sort of "loading" state. 

To my backend team:
For anyone who will want to make further changes in the future, if you only want to make minor changes to the scripts in the container, no need to keep rebuilding the image like I did initially. It takes 15 minutes to `docker build` every time. Consider installing a text editor within the container by:
`docker exec -it bash api`
`apt update`
`apt install vim`
Then make your changes to the scripts.

Then to start the flask app from within the container, just run `python -u -m flask run --host=0.0.0.0`
Once everything works, you can get your updated changes by copying the files from within the `/app` directory in the container to your local directory using `docker cp`.