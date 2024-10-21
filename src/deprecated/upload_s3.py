import os
import boto3
from botocore.exceptions import NoCredentialsError
from config import AWSSettings

def upload_image(client, file_name, bucket):
    """Upload de um arquivo para um bucket S3"""
    
    try:
        client.upload_file(
            os.path.join("csv",file_name), 
                    bucket, file_name)
        
        print(f"Upload bem-sucedido de {file_name} para o bucket {bucket}")
    except FileNotFoundError:
        print(f"O arquivo {file_name} não foi encontrado.")
    except NoCredentialsError:
        print("Credenciais não encontradas.")
    except Exception as e:
        print(f"Erro ao fazer upload: {e}")

def list_objects(client, bucket):
    """Listar todos os objetos em um bucket"""
    try:
        response = client.list_objects_v2(Bucket=bucket)
        if 'Contents' in response:
            return response['Contents']
        else:
            print("Nenhum objeto encontrado no bucket.")
    except Exception as e:
        print(f"Erro ao listar objetos: {e}")

def init_client():

    aws_key = AWSSettings() 
    s3 = boto3.client('s3',
        aws_access_key_id = aws_key.AWS_ACCESS_KEY,
        aws_secret_access_key = aws_key.AWS_SECRET_KEY)
         
    return s3

def upload_files():

    bucket = "dengue-cases"
    csv_files = [csv for csv in os.listdir("csv") if csv not in list_objects(s3, bucket)]
    s3 = init_client()

    for csv in csv_files:
        upload_image(s3, csv, bucket)

