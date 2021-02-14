FROM postgres:13.1-alpine

ADD ./dumps/airflow/prs.tar.gz /tmp
ADD ./dumps/airflow/files.tar.gz /tmp
ADD ./scripts/init/create.sql /docker-entrypoint-initdb.d
