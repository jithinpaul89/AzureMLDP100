# ------------------------------------------------------
# Attach the Databricks Cluster to the AzureML Workspace
# as an Attached Compute
# ------------------------------------------------------

import os
import azureml.core
from azureml.core import Workspace
from azureml.core.compute import DatabricksCompute, ComputeTarget
from azureml.exceptions import ComputeTargetException

# Check core SDK version number
print("SDK version:", azureml.core.VERSION)

# Access the Workspace
print("Accessing the AzureML workspace...")
ws = Workspace.from_config("./config")
print(ws.name, ws.resource_group, ws.location, ws.subscription_id, sep = '\n')


# Create the configuration information of the cluster
print("Initializing the parameters...")
db_resource_group     = "mlops-RG"
db_workspace_name     = "databricksWS001"
db_access_token       = "***************************"
db_compute_name       = "mydbcluster001"

db_compute_name=os.getenv("DATABRICKS_COMPUTE_NAME", db_compute_name) # Databricks compute name
db_resource_group=os.getenv("DATABRICKS_RESOURCE_GROUP", db_resource_group) # Databricks resource group
db_workspace_name=os.getenv("DATABRICKS_WORKSPACE_NAME", db_workspace_name) # Databricks workspace name
db_access_token=os.getenv("DATABRICKS_ACCESS_TOKEN", db_access_token) # Databricks access token

try:
    databricks_compute = DatabricksCompute(workspace=ws, name=db_compute_name)
    print('Compute target {} already exists'.format(db_compute_name))
except ComputeTargetException:
    print('Compute not found, will use below parameters to attach new one')
    print('db_compute_name {}'.format(db_compute_name))
    print('db_resource_group {}'.format(db_resource_group))
    print('db_workspace_name {}'.format(db_workspace_name))
    print('db_access_token {}'.format(db_access_token))
 
    config = DatabricksCompute.attach_configuration(
        resource_group = db_resource_group,
        workspace_name = db_workspace_name,
        access_token= db_access_token)
    databricks_compute=ComputeTarget.attach(ws, db_compute_name, config)
    databricks_compute.wait_for_completion(True)

















