from azure.cosmos import CosmosClient
import os

os.environ['ACCOUNT_URI']="https://acc1031.documents.azure.com:443/"
os.environ['ACCOUNT_KEY']="W4r57wzXqX10Dt0s8i8McSMuDDuPCsO4rxsiUi3Xj5vtzpzYO1H9VxTwoQ5M3yldjuaUGAckvLOFMXxIzm6hIQ=="

url = os.environ['ACCOUNT_URI']
key = os.environ['ACCOUNT_KEY']
client = CosmosClient(url, credential=key)
database_name = 'testDatabase'
database = client.get_database_client(database_name)
container_name = 'smhproducts'
container = database.get_container_client(container_name)

# Enumerate the returned items
import json
for item in container.query_items(
        query='SELECT * FROM smhproducts r WHERE r.id="item3"',
        enable_cross_partition_query=True):
    print(json.dumps(item, indent=True))