output "vpc_id" {
  value = "${aws_vpc.bridge.id}"
}

output "gate_id" {
  value = "${aws_internet_gateway.clamp.id}"
}
