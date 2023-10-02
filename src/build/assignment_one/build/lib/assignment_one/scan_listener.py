import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class ScanListener(Node):

    def __init__(self):
        super().__init__('scan_listener')
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.listener_callback,
            10
        )
        self.subscription

    # def listener_callback(self, msg):
    #     # You can process the LaserScan message here.
    #     # For simplicity, I'm just printing the first range measurement.
    #     self.get_logger().info(f'First range measurement: {msg.ranges[0]}')
    def listener_callback(self, msg):
        self.get_logger().info('Received a scan message.')
        
def main(args=None):
    rclpy.init(args=args)

    node = ScanListener()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
