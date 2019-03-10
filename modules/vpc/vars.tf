# VPC variables

variable "vpc_cidr" {
    default = "10.0.0.0/16"
}

variable "vpc_tenancy" {}

# Subnet variables

variable "vpc_id" {}

variable "subnet_count" {
  default = 1
}

variable "subnet_cidr" {
  default = "10.0.0.0/24"
}

variable "subnet_zone" {
  default = "us-east-1a"
}

variable "gate_id" {}

