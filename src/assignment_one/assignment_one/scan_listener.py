import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from sensor_msgs.msg import LaserScan

class ScanListener(Node):

    def __init__(self):
        super().__init__('scan_listener')

        # QoS settings
        qos = QoSProfile(depth=10, reliability=rclpy.qos.ReliabilityPolicy.BEST_EFFORT)

        # Create subscription with QoS settings
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.listener_callback,
            qos
        )
        self.subscription

    def listener_callback(self, msg: LaserScan):
        # Check the first range reading
        distance = msg.ranges[0]
        
        if 0 < distance < 1.0:
            self.get_logger().info('Obstacle')
        else:
            print('Free')

        # if 0 < distance < 1.0:
        #     self.get_logger().info('Obstacle')
        # else:
        #     self.get_logger().info('Free')


def main(args=None):
    rclpy.init(args=args)

    node = ScanListener()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()