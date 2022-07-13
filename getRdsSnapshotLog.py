import boto3
import time
import json

# 서울 리전
region = 'ap-northeast-2'

# rds snapshot logs to s3 Access Key
ACCESS_KEY = 'YOUR ACCESS KEY'
SECRET_KEY = 'YOUR SECRET KEY'

def lambda_handler(event, context):

    rds_client = boto3.client(
        'rds',
        region_name=region,
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY
    )

    snapshot_list = rds_client.describe_db_cluster_snapshots(
        # DBClusterIdentifier='',
        # DBClusterSnapshotIdentifier=''
    )

    s3_client = boto3.client(
        's3',
        region_name=region,
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY
    )
    s3_client.put_object(Bucket='rds-logs', Key='snapshots/' + time.strftime('snapshots' + '_' + '%Y%m%d') + '.txt', Body=json.dumps(snapshot_list, indent=4, default=str))
