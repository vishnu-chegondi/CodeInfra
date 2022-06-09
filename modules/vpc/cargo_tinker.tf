resource "aws_route_table_association" "public" {
    count = "${var.public_subnet_count}"
    subnet_id = "${element(aws_subnet.publicholds.*.id,count.index)}"
    route_table_id = "${aws_route_table.passageway.id}"
}

