#!/home/faizal/miniconda3/envs/ros/bin/python

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, CameraInfo, Imu
import os
import time

import cv2
from cv_bridge import CvBridge
from rclpy.qos import qos_profile_sensor_data
import numpy as np
import matplotlib.pyplot as plt
from rotation_utils import get_R

IMG_SAVE_PATH='./data/images/'
os.makedirs(IMG_SAVE_PATH, exist_ok=True)

print("cwd:", os.getcwd())
print("Image save path:", IMG_SAVE_PATH)


class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('image_subscriber_node')
        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.image_callback,
            qos_profile=qos_profile_sensor_data
        )
        
        self.imu_subscriber = self.create_subscription(
            Imu,
            '/camera/imu',
            self.imu_callback,
            qos_profile=qos_profile_sensor_data
        )
        self.cv_bridge = CvBridge()
        self.image_counter = 0
        
        self.image_info = self.create_subscription(
            CameraInfo,
            '/camera/camera_info',
            self.image_info_callback,
            qos_profile=qos_profile_sensor_data
        )
        
        self.roll, self.pitch, self.yaw = None, None, None
        self.R_camera = None

    def imu_callback(self, msg):
        self.linear_acc = np.array([msg.linear_acceleration.x, msg.linear_acceleration.y, msg.linear_acceleration.z])
        x, y, z = self.linear_acc
        self.pitch = -np.degrees(np.arctan(x/np.sqrt(y ** 2 + z **2)))
        self.roll = -np.degrees(np.arctan(y/np.sqrt(x ** 2 + z ** 2)))
        self.yaw = np.degrees(np.arctan(z/np.sqrt(x ** 2 + z ** 2)))
        self.R_imu = get_R(self.roll, self.pitch, self.yaw)
        
        self.get_logger().info(f"Roll:{self.roll:.3f} Pitch:{self.pitch:.3f} Yaw:{self.yaw:.3f}")
        
    def image_info_callback(self, msg):
        self.K = np.array(msg.k).reshape(3, 3)
        # This R is camera with world
        self.R_camera = np.array(msg.r).reshape(3, 3)
        
        self.get_logger().info(f'K:{self.K}')
        self.get_logger().info(f"R:{self.R_camera}")
        
        # find the relative rotation between camera and IMU
        if self.R_camera is not None and self.roll is not None and self.pitch is not None and self.yaw is not None:
            self.R_imu_wrt_camera = self.R_imu.T @ self.R_camera
    
    def image_callback(self, msg):
        h, w = msg.height, msg.width
        data = np.array(msg.data, dtype=np.uint8)
        data = data.reshape(h, w, 3)
        # data = cv2.cvtColor(data, cv2.COLOR_BGR2RGB)
        filepath = os.path.join(IMG_SAVE_PATH, f"{self.image_counter}.jpg")
        plt.imsave(filepath, data)
        
        self.get_logger().info(f"Image saved at {filepath}")
        self.image_counter += 1

        
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


