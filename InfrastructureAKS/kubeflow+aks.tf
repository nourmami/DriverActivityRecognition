
/*data "azuread_client_config" "current" {}

resource "azuread_application" "app" {
  display_name = "PFA-app"
   owners = [
    data.azuread_client_config.current.object_id,
  ]
}
resource "azuread_service_principal" "ID" {
  application_id = azuread_application.app.application_id
  owners = [
    data.azuread_client_config.current.object_id,
  ]
}

resource "azuread_service_principal_password" "pwd" {
  service_principal_id = azuread_service_principal.ID.object_id
}*/

resource "azurerm_kubernetes_cluster" "aks_cluster" {
  name                = var.aks_cluster_name
  location            = var.location
  resource_group_name = var.resource_group_name
  dns_prefix          = var.aks_dns_prefix

  default_node_pool {
    name            = "default"
    node_count      = 2
    vm_size         = "Standard_B2s"
    os_disk_size_gb = 30
  }

  service_principal {
    client_id     = var.appId
    client_secret = var.password
  }

  tags = {
    Environment = "dev"
  }
}

resource "kubernetes_namespace" "kubeflow" {
  metadata {
    name = "kubeflow"
  }
}

resource "kubectl_manifest" "kubeflow_operator" {
  depends_on = [kubernetes_namespace.kubeflow]
  manifest   = templatefile("${path.module}/kubeflow-operator.yaml", {
    namespace = kubernetes_namespace.kubeflow.metadata[0]
  })
}

resource "kubectl_manifest" "kubeflow_ui" {
  depends_on = [kubernetes_namespace.kubeflow]
  manifest   = templatefile("${path.module}/kubeflow-ui.yaml", {
    namespace = kubernetes_namespace.kubeflow.metadata[0]
  })
}