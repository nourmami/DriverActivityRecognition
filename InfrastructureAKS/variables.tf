# Define variables for the existing resource names
variable "resource_group_name" {
  type = string
  default = "PFA-rg"
}

variable "storage_account_name" {
  type = string
  default = "storage1account1pfa"
}

variable "workspace_name" {
  type = string
  default = "PFA-workspace"
}

variable "aks_cluster_name" {
  type        = string
  description = "The name of the AKS cluster"
  default     = "PFA-aks-cluster"
}  
variable "location" {
  type        = string
  default     = "westeurope"
}


variable "aks_dns_prefix" {
  type        = string
  description = "The DNS prefix for the AKS cluster"
  default     = "aks-cluster"
}

variable "aks_kubernetes_version" {
  type        = string
  description = "The version of Kubernetes that is installed on the AKS cluster"
  default     = "1.25.5"
}



    variable "appId" {
  type        = string
  default     = ""
}

variable "password" {
  type        = string
  default     = ""
}
