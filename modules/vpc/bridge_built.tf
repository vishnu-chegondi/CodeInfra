resource "aws_vpc" "bridge" {
    cidr_block = "${var.vpc_cidr}"
    instance_tenancy = "${var.vpc_tenancy}"

    tags {
        Name = "cargo_bridge"
    }

}

resource "aws_subnet" "holds" {
    vpc_id = "${var.vpc_id}"
    cidr_block = "${var.subnet_cidr}"
    availability_zone = "${var.subnet_zone}"
    count = "${var.subnet_count}"
    tags {
        Name = "cargo_holds"
    }

}

resource "aws_security_group" "lasher" {
    name = "lasher"
    vpc_id = "${var.vpc_id}"
    description = "allow ssh connection and web ports for requests"

    ingress {
        description = "allow ssh connection"
        from_port = 22
        to_port = 22
        cidr_blocks = ["0.0.0.0/0"]
        protocol = "tcp"
    }

    ingress{
        description = "Allow http requests"
        from_port = 80
        to_port = 80
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    egress {
        description = "allow all"
        from_port = 0
        to_port = 0
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    tags {
        name = "lasher"
    }
}

resource "aws_internet_gateway" "clamp" {
    vpc_id = "${var.vpc_id}"

    tags {
        name = "clamp"
    }
}

resource "aws_route_table" "passageway" {
    vpc_id = "${aws_vpc.bridge.id}"

    route {
        cidr_block = "0.0.0.0/0"
        gateway_id = "${var.gate_id}"
    }

    tags {
        name = "passageway"
    }

}
