#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TalkerSubscriber(Node):
    def __init__(self):
        super().__init__('talker_subscriber_node')
        self.subscription = self.create_subscription(
            String,
            '/chatter',
            self.talker_callback,
            10
        )

    def talker_callback(self, msg):
        self.get_logger().info(msg.data)
        
        
def main(args=None):
    rclpy.init(args=args)
    talker_subscriber = TalkerSubscriber()

    try:
        rclpy.spin(talker_subscriber)
    except KeyboardInterrupt:
        pass
    
    talker_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()