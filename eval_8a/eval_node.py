#Commented
import sys

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node

from std_msgs.msg import String

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('pubroot')
        self.publisher_ = self.create_publisher(String, 'jagveer', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'I have completed evaluation 8a: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

def main(args=None):
    rclpy.init()

    try:
        minimal_publisher = MinimalPublisher()

        rclpy.spin(minimal_publisher)
    except KeyboardInterrupt:
        pass
    except ExternalShutdownException:
        sys.exit(1)

if __name__ == '__main__':
    main()
