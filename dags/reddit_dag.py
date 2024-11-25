import os
import sys
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.aws_s3_pipeline import upload_s3_pipeline
from pipelines.reddit_pipeline import reddit_pipeline


default_args = {
    'owner': 'AADD',
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),

}
file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(

    "reddit_data_pipeline",  # DAG name
    default_args=default_args,
    description="A DAG to collect Reddit data periodically and save to CSV",
    schedule_interval=timedelta(minutes=1),  # Adjust the schedule (e.g., every 1 minutes)
    start_date=datetime(2024, 11, 16),  # Correctly specify the start date
    catchup=False,  # Skip catching up on missed runs
)


extract = PythonOperator(
    task_id='reddit_extraction',
    python_callable=reddit_pipeline,
    op_kwargs={
        'file_name': f'reddit_data_{datetime.now().strftime("%Y%m%d_%H%M")}',
        'subreddit': 'dataengineering',
        'time_filter': 'day',
        'limit': 100
    },
    dag=dag

)


# upload to s3
upload_s3 = PythonOperator(
    task_id='s3_upload',
    python_callable=upload_s3_pipeline,
    dag=dag
)

extract >> upload_s3