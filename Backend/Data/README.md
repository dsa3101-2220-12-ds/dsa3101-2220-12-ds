This repo/Backend/Data/ folder consists of data resources which are of relevance to the backend team only. Here is the breakdown of the folder:

jobs/: This folder consists of job description text data scraped from the internet. The data originated from two well-known job posting sites in Singapore - MyCareersFuture and JobStreet. The code for scraping these two sites reside in "repo/Backend/Code/Data Collection/". Within this jobs/ folder, you will find two types of files:
	1. .txt files: These files contain the URLs of specific job postings. The naming convention of these files are as follows:
		{jobsite}_job_url_query-{input_query}.txt
		E.g. If we search for "machine learning engineer" from JobStreet, then the file that contains the URLs of related job postings will be jobstreet_job_url_query-machine_learning_engineer.txt
	2. .csv files: These files contain the actual text data of each job within their respective URL files. It consists of four columns which represent the following information in order: Job Title, Company, Job Description, URL of job posting. The naming convention of these files are as follows:
		{jobsite}_query-{input_query}.csv
		E.g. If we search for "machine learning engineer" from JobStreet, then the file that contains the text information of related job postings will be jobstreet_query-machine_learning_engineer.csv

NER_annotated_data/: This folder consists of labelled data for training the Named Entity Recognition (NER) model. The breakdown of the files and folders is further elaborated upon in the README.md file within the NER_annotated_data/ directory.

modules/: This folder consists of a few cached resources with regards to the module information. In particular, it contains a file that acts as a cache that stores the result of running the NER model on the module descriptions.

skills/: This folder consists of text data about descriptions of skills. These descriptions are provided by an open-source database about skills from a company called Lightcast. The code to collect this data using the API provided by Lightcast resides in "repo/Backend/Code/Data Collection/Requests from Lightcast API.ipynb". It requires submitting a string of text as a query (E.g. "data"). As a result, a list of skills, along with the skills' descriptions will be returned (E.g. "Data Entry", "Database Management", "Java Database Connectivity", etc). This output is nicely formatted into the CSV file in the skills/ folder. We have performed five queries on the Lightcast database - "data", "analysis", "machine learning", "ML", "statistic". 
You can find more information about the dataset here: https://docs.lightcast.dev/apis/skills. 
