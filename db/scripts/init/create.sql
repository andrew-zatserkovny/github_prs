CREATE SCHEMA airflow;

CREATE TABLE airflow.pull_requests (
  number INTEGER,
  title VARCHAR(250),
  url VARCHAR(100),
  created_at TIMESTAMP,
  merged_at TIMESTAMP,
  state VARCHAR(20),
  PRIMARY KEY(number)
);

CREATE TABLE airflow.files (
  id SERIAL,
  pr_number INTEGER,
  filename VARCHAR(250),
  raw_url VARCHAR(250),
  PRIMARY KEY (id),
  CONSTRAINT pr_number_fkey
    FOREIGN KEY(pr_number)
      REFERENCES airflow.pull_requests(number)
);

COPY airflow.pull_requests(number, title, url, created_at, merged_at, state)
FROM '/tmp/pr_df.csv'
DELIMITER ','
CSV HEADER;

COPY airflow.files(pr_number, filename, raw_url)
FROM '/tmp/file_df.csv'
DELIMITER ','
CSV HEADER;

CREATE DATABASE github_prs_test;
