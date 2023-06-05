# Import the required packages
import os
from dotenv import load_dotenv
from azureml.core import Workspace
from azure.mgmt.resource import ResourceManagementClient
from azureml.core import Environment
from azureml.core.compute import ComputeTarget, AmlCompute,ComputeInstance
from azureml.exceptions import ComputeTargetException
from azure.identity import DefaultAzureCredential

# Load environment variables from .env file
load_dotenv()

# Get the Azure subscription ID from environment variables
subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
resource_group_name = os.getenv("RESOURCE_GROUP")

# Authenticate with Azure using a DefaultAzureCredential object
credential = DefaultAzureCredential()

# Create a ResourceManagementClient and StorageManagementClient object
resource_client = ResourceManagementClient(credential, subscription_id)
# Create a new resource group
rg_result=resource_client.resource_groups.create_or_update(resource_group_name, {"location": "westeurope"})
print(f"Provisioned resource group {rg_result.name}")

# Defining AzureML workspace details
ws = Workspace.create(name='PFA-workspace', subscription_id='f0aab5c4-5117-4406-8a16-8d58d23c78fa',resource_group='PFA-rg',location='West Europe' )

#Defining AzureML environment details
myenv = Environment.from_conda_specification(name='training_environment',
                                           file_path='./conda.yml')
myenv.register(workspace=ws)


# Define compute instance configuration
compute_name = 'PFA-compute-instance'
compute_config = ComputeInstance.provisioning_configuration(vm_size='Standard_DS12_v2',
                                                            ssh_public_access=True)

# Create the compute instance
try:
    compute_instance = ComputeTarget(ws, compute_name)
    print('Found existing cluster.')
    
except ComputeTargetException as e:
    compute_instance = ComputeTarget.create(ws, compute_name, compute_config)
    compute_instance.wait_for_completion(show_output=True)




