from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.python import BranchPythonOperator
from airflow.operators.bash import BashOperator

from datetime import date
from datetime import datetime
from datetime import timedelta

import pandas as pd
import requests
import boto3
import psycopg2
import logging
import os

start_date = datetime(2024, 3, 4)

# Get the directory path for reference
dir_path = os.getcwd()

default_args = {
    'owner' : 'airflow',
    'start_date' : start_date,    # Don't forget to change the date
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}

streaming_dag = DAG(
    "streaming_dag",
    default_args = default_args,
    description = "",
    schedule = "@daily",
    catchup = False
)

download_data = BashOperator(
    task_id = "download_data",
    bash_command = "wget -O C:\\Users\\Nikit\\Documents\\GitHub\\streaming_movies_data\\datasets\\movies.zip https://github.com/nikitgoku/datasets/blob/main/movie_dataset/movies_small.zip",
    retries = 1,
    retry_delay = timedelta(seconds=15)
)

unzip_data = BashOperator(
    task_id = "unzip_data",
    bash_command = "unzip C:\\Users\\Nikit\\Documents\\GitHub\\streaming_movies_data\\datasets\\movies.zip -d C:\\Users\\Nikit\\Documents\\GitHub\\streaming_movies_data\\datasets\\",
    retries = 1,
    retry_delay = timedelta(seconds=15)
)


download_data >> unzip_data

