#!/home/faizal/miniconda3/envs/ros/bin/python

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

import cv2
from cv_bridge import CvBridge
from rclpy.qos import qos_profile_sensor_data
import numpy as np

class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('image_subscriber_node')
        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.image_callback,
            qos_profile=qos_profile_sensor_data
        )
        self.cv_bridge = CvBridge()

    def image_callback(self, msg):
        h, w = msg.height, msg.width
        data = np.array(msg.data, dtype=np.uint8)
        data = data.reshape(h, w, 3)
        data = cv2.cvtColor(data, cv2.COLOR_BGR2RGB)
        cv2.imwrite('image.jpg', data)
        
        self.get_logger().info("Image saved")


        
def main(args=None):
    rclpy.init(args=args)
    image_subscriber = ImageSubscriber()

    try:
        rclpy.spin(image_subscriber)
    except KeyboardInterrupt:
        pass

    image_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
