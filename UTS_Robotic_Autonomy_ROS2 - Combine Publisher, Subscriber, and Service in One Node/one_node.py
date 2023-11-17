#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from example_interfaces.msg import Float64
from example_interfaces.srv import SetBool

class MyNode(Node):
    def __init__(self):
        super().__init__("my_node")
        self.pub_ = self.create_publisher(String, "Apasaja", 10)
        self.timer_ = self.create_timer(0.1, self.publish_text)
        self.create_subscription(Float64, "Angka", self.Angka_callback, 10)
        self.create_service(SetBool, "mulai_robot",)

    def publish_text(self):
        msg = String()
        msg.data = str(self.angka_)
        self.pub_.publish(msg)

    def Angka_callback(self, msg:Float64):
        self.get_logger().info(str(msg.data))
        self.angka_ = msg.data

    def mulai_robot_callback(self, request: SetBool.Request, response: SetBool.Response):
        if request.data:
            self.get_logger().info("nyalakan robotnya")
        else:
            self.get_logger().info("berhentikan robotnya")
        response.success = True
        return response


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()