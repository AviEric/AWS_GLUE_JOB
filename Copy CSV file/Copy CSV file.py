import boto3
import pandas as pd

s3 = boto3.client('s3')

bucket_name = "aws-glue-assets-471112911887-us-east-1"
file_key = "scripts/source/shopping_trends1.csv"

response = s3.get_object(
    Bucket=bucket_name,
    Key=file_key
)

df = pd.read_csv(response['Body'])

print(df.head())
print(f"Rows: {len(df)}")