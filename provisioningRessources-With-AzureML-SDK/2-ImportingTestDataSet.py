#pip install -r requirements.txt
from dotenv import load_dotenv
import os
from azureml.core import Workspace
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient ,models
from azure.storage.blob import BlobServiceClient
from datetime import datetime, timedelta
from azure.storage.blob import ContainerSasPermissions

# Load environment variables from .env file
load_dotenv()

#ws = Workspace.from_config()

# Authenticate with Azure using a DefaultAzureCredential object
credential = DefaultAzureCredential()

# Get the Azure subscription ID from environment variables
subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
resource_group_name = os.getenv("RESOURCE_GROUP")

storage_client = StorageManagementClient(credential, subscription_id)


# Set the storage account name and container name
account_name = os.getenv("STORAGE_ACCOUNT_NAME")
container_name1 = "test-container"




#Retrieve the account's primary access key and generate a connection string.
storage_keys = storage_client.storage_accounts.list_keys(resource_group_name, account_name)

# Set the connection string to the new storage account
connect_str = f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={storage_keys.keys[0].value};EndpointSuffix=core.windows.net"

# Create a BlobServiceClient object
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# Create a new container for the images
container_client = blob_service_client.create_container(container_name1)

# Set the path to the train folder
test_folder_path = "/home/nour/Projects/PFA/imgs/test"

# Loop through each subfolder in the "train" folder and upload each image to the container

for image_name in os.listdir(test_folder_path):
    image_path = os.path.join(test_folder_path, image_name)
    #print(image_name,image_path)
    # Upload the image to the container
    blob_name = f"test/{image_name}"
    blob_client = blob_service_client.get_blob_client(container=container_name1, blob=blob_name)
    with open(image_path, "rb") as data:
        blob_client.upload_blob(data,overwrite=True)
        



# Set the SAS expiry time (e.g. 1 hour from now)
expiry_time = datetime.utcnow() + timedelta(days=30)

# Set the container SAS permissions
container_sas_permissions = ContainerSasPermissions(read=True, write=True, delete=True)

# Create the SAS token for the container
sas_token = container_client.generate_container_sas(expiry_time, container_sas_permissions)

# Generate the SAS URL for the container
sas_url = f"https://{account_name}.blob.core.windows.net/{container_name1}?{sas_token}"

print(sas_url)