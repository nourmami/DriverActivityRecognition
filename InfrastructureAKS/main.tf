# Get the details of the existing resource group
data "azurerm_resource_group" "rg" {
  name = var.resource_group_name
}

# Get the details of the existing storage account
data "azurerm_storage_account" "storage_account" {
  name                = var.storage_account_name
  resource_group_name = var.resource_group_name
}

resource "azurerm_application_insights" "AInsights" {
  name                = "workspace-ai"
  location            = data.azurerm_resource_group.rg.location
  resource_group_name = data.azurerm_resource_group.rg.name
  application_type = "other"
}

resource "azurerm_key_vault" "key_vault" {
  name                = "workspacekeyvault1"
  location            = data.azurerm_resource_group.rg.location
  resource_group_name = data.azurerm_resource_group.rg.name
  tenant_id           = data.azurerm_client_config.current.tenant_id
  sku_name            = "premium"
}

resource "azurerm_machine_learning_workspace" "PFA_workspace" {
  name                    = var.workspace_name
  location                = data.azurerm_resource_group.rg.location
  resource_group_name     = data.azurerm_resource_group.rg.name
  application_insights_id = azurerm_application_insights.AInsights.id
  key_vault_id            = azurerm_key_vault.key_vault.id
  storage_account_id      = data.azurerm_storage_account.storage_account.id
  identity {
    type = "SystemAssigned"
  }
}

# Output the workspace ID and URL
output "workspace_id" {
  value = azurerm_machine_learning_workspace.PFA_workspace.id

}
