# About Github PRs

This project is a ligtweight Fast API application intended for calculating basic statistics and fetching file info from a database that was created on top of a dump grabbed via Github API (Apache Airflow repo).
It comprises two parts:

* Web app container
* Postgesql container

## Data flow

### Step 1. 
Before finding its way into the dockerized Postgresql DB the dump was downloaded with the help of Jupyter notebook script (/db/GithubPRs.py). Several iterations were needed to complete downloading due to GithubAPI restrictions.

### Step 2.
The dumps were then pushed into the Postgresql container (/db/Dockerfile).

### Step 3.
The init script was run to migrate data into a separate schema in github_prs_dev DB (/db/scripts/init/create.sql).

### Step 4.
Data models were populated with the consumed data (app/db.py)
