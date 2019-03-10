provider "aws" {
  region = "us-east-1"
}

module "vpc" {
  source = "../modules/vpc"
  vpc_cidr = "10.0.0.0/16"
  vpc_tenancy = "default"
  subnet_count = 2
  vpc_id = "${module.vpc.vpc_id}"
  gate_id = "${module.vpc.gate_id}"
}
