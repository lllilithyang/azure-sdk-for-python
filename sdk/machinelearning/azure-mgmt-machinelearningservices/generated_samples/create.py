# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.machinelearningservices import MachineLearningServicesMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-machinelearningservices
# USAGE
    python create.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = MachineLearningServicesMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-1111-2222-3333-444444444444",
    )

    response = client.workspaces.begin_create_or_update(
        resource_group_name="workspace-1234",
        workspace_name="testworkspace",
        parameters={
            "identity": {
                "type": "SystemAssigned,UserAssigned",
                "userAssignedIdentities": {
                    "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/workspace-1234/providers/Microsoft.ManagedIdentity/userAssignedIdentities/testuai": {}
                },
            },
            "location": "eastus2euap",
            "properties": {
                "applicationInsights": "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/workspace-1234/providers/microsoft.insights/components/testinsights",
                "containerRegistry": "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/workspace-1234/providers/Microsoft.ContainerRegistry/registries/testRegistry",
                "description": "test description",
                "encryption": {
                    "identity": {
                        "userAssignedIdentity": "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/workspace-1234/providers/Microsoft.ManagedIdentity/userAssignedIdentities/testuai"
                    },
                    "keyVaultProperties": {
                        "identityClientId": "",
                        "keyIdentifier": "https://testkv.vault.azure.net/keys/testkey/aabbccddee112233445566778899aabb",
                        "keyVaultArmId": "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/workspace-1234/providers/Microsoft.KeyVault/vaults/testkv",
                    },
                    "status": "Enabled",
                },
                "friendlyName": "HelloName",
                "hbiWorkspace": False,
                "keyVault": "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/workspace-1234/providers/Microsoft.KeyVault/vaults/testkv",
                "sharedPrivateLinkResources": [
                    {
                        "name": "testdbresource",
                        "properties": {
                            "groupId": "Sql",
                            "privateLinkResourceId": "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/workspace-1234/providers/Microsoft.DocumentDB/databaseAccounts/testdbresource/privateLinkResources/Sql",
                            "requestMessage": "Please approve",
                            "status": "Approved",
                        },
                    }
                ],
                "storageAccount": "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/accountcrud-1234/providers/Microsoft.Storage/storageAccounts/testStorageAccount",
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/stable/2022-10-01/examples/Workspace/create.json
if __name__ == "__main__":
    main()
