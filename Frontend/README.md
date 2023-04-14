Frontend README

This is the README for Frontend folder

We have a list of folders and files:
1. admin 
    - Includes interview documents, meeting seconds, High and Low fedality prototypes
2. API_testing
    - For testing API 
3. assets
    - Includes bootstrap css file to standardise the theme of the dash website
4. files
    - Includes files that are necessary for dash website content such as css and xlsx files
5. Pages
    - Includes every page that the dash website will need, using dash we were able to register each page in order for app.py to access them via the pages folder easily
6. testing pages
    - Intermediate pages while building the website
7. w2v 
    - world to vector files
8. App.py
    - Runs the code that allows the dash website to run locally
9. Docker-cmpose.yml
    - To connect frontend and backend containers
10. Dockerfile
    - To create docker image
11. README.md
    - Explaining each file's use case
12. requirements.txt
    - Ensures that anyone running the code is able to download all necessary packages before app.py is run


To run the app.py file, run: 'python app.py' in terminal
To run Dockerized website, run: 1. 'docker compose build' 2. 'docker compose up -d'