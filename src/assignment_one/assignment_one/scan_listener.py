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
        # Initialize a variable to keep track of the status
        is_obstacle_present = False
        
        # Iterate over all range readings
        for distance in msg.ranges:
            # Check if the distance is between 0 and 1 (change 1 to the desired threshold)
            if 0 < distance < .3:
                is_obstacle_present = True
                break  # exit the loop early if an obstacle is found
        
        # Check the status and print the appropriate message
        if is_obstacle_present:
            print('Obstacle')
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
