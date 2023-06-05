# Import the required packages
import os
from azureml.core import Workspace, Dataset, ScriptRunConfig,Experiment,Datastore
from azureml.core import Environment
from azureml.data.datapath import DataPath
from azureml.core.compute import ComputeTarget, AmlCompute
from azureml.core.compute_target import ComputeTargetException
from azureml.exceptions import UserErrorException

# Defining AzureML workspace details
ws = Workspace.from_config()



# choose a name for your cluster
cluster_name = "gpu-cluster"

try:
    compute_target = ComputeTarget(workspace=ws, name=cluster_name)
    print('Found existing compute target')
except ComputeTargetException:
    print('Creating a new compute target...')
    compute_config = AmlCompute.provisioning_configuration(vm_size='STANDARD_NC6', 
                                                           max_nodes=4)

    # create the cluster
    compute_target = ComputeTarget.create(ws, cluster_name, compute_config)

    # can poll for a minimum number of nodes and for a specific timeout. 
    # if no min node count is provided it uses the scale settings for the cluster
    compute_target.wait_for_completion(show_output=True, min_node_count=None, timeout_in_minutes=20)

# use get_status() to get a detailed status for the current cluster. 
print(compute_target.get_status().serialize())




blob_datastore_name='MyBlobDatastore'
account_name=os.getenv("STORAGE_ACCOUNT_NAME") # Storage account name
container_name=os.getenv("BLOB_CONTAINER_62", "<my-container-name>") # Name of Azure blob container
account_key=os.getenv("BLOB_ACCOUNT_KEY_62", "<my-account-key>") # Storage account key

try:
    blob_datastore = Datastore.get(ws, blob_datastore_name)
    print("Found Blob Datastore with name: %s" % blob_datastore_name)
except UserErrorException:
       blob_datastore = Datastore.register_azure_blob_container(
           workspace=ws,
           datastore_name=blob_datastore_name,
           account_name=account_name, # Storage account name
           container_name=container_name, # Name of Azure blob container
           account_key=account_key) # Storage account key
       print("Registered blob datastore with name: %s" % blob_datastore_name)

blob_data_ref = DataReference(
       datastore=blob_datastore,
       data_reference_name="blob_test_data",
       path_on_datastore="testdata")