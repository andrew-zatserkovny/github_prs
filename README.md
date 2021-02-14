# About Github PRs

This project is a ligtweight Fast API application intended for calculating basic statistics and fetching file info from a database that was created on top of a dump grabbed via Github API (Apache Airflow repo).
It comprises two parts:

* Web app container
* PostgeSQL container

# Application overview

## Technologies used

* Fast API
* PostgreSQL + Tortoise ORM

## Data flow

### Step 1. 
Before finding its way into the dockerized Postgresql DB the dump (`/db/dumps/airflow/*`) was downloaded with the help of Jupyter notebook script (`/db/GithubPRs.py`). Several iterations were needed to complete downloading due to GithubAPI restrictions.

### Step 2.
The dumps were then pushed into the PostgreSQL container (`/db/Dockerfile`).

### Step 3.
The init script was run to migrate data into a separate schema in github_prs_dev DB (`/db/scripts/init/create.sql`).

### Step 4.
Data models were populated with the consumed data (`/app/db.py`)

## Step 5
Data is now ready for querying via API endoints.

## Using the application

The application is started by running `docker-compose up`. After starting the project you should be able to access these API endpoints:

* http://localhost:8004/top (Top three most changed files in the current repo). You should see the following response:
```
[
  {
    "filename": "setup.py",
    "total_count": 879
  },
  {
    "filename": "airflow/www/views.py",
    "total_count": 738
  },
  {
    "filename": "airflow/models.py",
    "total_count": 707
  }
]
```
* http://localhost:8004/stats (Min, Max, Avg durations calculated as time from creating a PR to merging it). The below response will be displayed:
```
[
  {
    "min": 2,
    "max": 50607153,
    "avg": 630001.4701330437
  }
]
```
* http://localhost:8004/docs (Contains Swagger docs)
