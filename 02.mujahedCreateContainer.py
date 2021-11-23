from azure.cosmos import CosmosClient, exceptions,PartitionKey
import os

os.environ['ACCOUNT_URI']="https://acc1031.documents.azure.com:443/"
os.environ['ACCOUNT_KEY']="W4r57wzXqX10Dt0s8i8McSMuDDuPCsO4rxsiUi3Xj5vtzpzYO1H9VxTwoQ5M3yldjuaUGAckvLOFMXxIzm6hIQ=="

url = os.environ['ACCOUNT_URI']
key = os.environ['ACCOUNT_KEY']
client = CosmosClient(url, credential=key)
database_name = 'testDatabase'

try:
    database = client.create_database(database_name)
except exceptions.CosmosResourceExistsError:
    database = client.get_database_client(database_name)

container_name="smhproducts"
try:
	container=database.create_container(id=container_name, partition_key=PartitionKey(path="/productName"))
except exceptions.CosmosResourceExistsError:
	container=database.get_container_client(container_name)
except exceptions.CosmosHttpResponseError:
	raise
    
