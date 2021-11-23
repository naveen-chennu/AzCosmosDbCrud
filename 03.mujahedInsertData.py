from azure.cosmos import CosmosClient
import os

os.environ['ACCOUNT_URI']="https://acc1031.documents.azure.com:443/"
os.environ['ACCOUNT_KEY']="W4r57wzXqX10Dt0s8i8McSMuDDuPCsO4rxsiUi3Xj5vtzpzYO1H9VxTwoQ5M3yldjuaUGAckvLOFMXxIzm6hIQ=="

url = os.environ['ACCOUNT_URI']
key = os.environ['ACCOUNT_KEY']
client = CosmosClient(url, credential=key)

database_name = 'testDatabase'
container_name="smhproducts"

database = client.get_database_client(database_name)
container=database.get_container_client(container_name)

for i in range(1,11):
    container.upsert_item({
        "id":"item{0}".format(i),
        "productName":"Watch{0}".format(i),
        "productModel":"Model{0}".format(i)
        })
