# Define variables for the existing resource names
variable "resource_group_name" {
  type = string
  default = ""
}

variable "storage_account_name" {
  type = string
  default = ""
}

variable "workspace_name" {
  type = string
  default = ""
}

variable "aks_cluster_name" {
  type        = string
  description = "The name of the AKS cluster"
  default     = ""
}  
variable "location" {
  type        = string
  default     = ""
}


variable "aks_dns_prefix" {
  type        = string
  description = "The DNS prefix for the AKS cluster"
  default     = ""
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
