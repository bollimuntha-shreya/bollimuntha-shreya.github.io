#!/home/faizal/miniconda3/envs/ros/bin/python

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
import os
import time

import cv2
from cv_bridge import CvBridge
from rclpy.qos import qos_profile_sensor_data
import numpy as np
import matplotlib.pyplot as plt
from icecream import ic
from sensor_msgs.msg import Image


SAVE_PATH='./data_imu_and_image/'
os.makedirs(SAVE_PATH, exist_ok=True)

print("cwd:", os.getcwd())
print("Imu data save path:", SAVE_PATH)



class IMUSubscriber(Node):
    def __init__(self):
        super().__init__('imu_subscriber_node')
        self.counter1, self.counter2 = 0, 0
        self.accel_subscription = self.create_subscription(
            Imu,
            '/camera/accel/sample',
            self.accel_callback,
            qos_profile=qos_profile_sensor_data,
        )
        
        self.img_subscriber = self.create_subscription(
            Image,
            '/camera/color/image_raw',
            self.image_callback,
            qos_profile=qos_profile_sensor_data
        )
        
        # self.gyro_subscription = self.create_subscription(
        #     Imu,
        #     '/camera/gyro/sample',
        #     self.gyro_callback,
        #     qos_profile=qos_profile_sensor_data
        # )
        
        self.linear_acc = np.zeros(3)
        self.position = np.zeros(3)
        self.velocity = np.zeros(3)
        self.orientation = np.zeros(3)
        self.dt = 1e-2
        self.image = np.zeros((640, 480, 3))
        
        self.roll, self.pitch, self.yaw = 0, 0, 0
        self.prev_time = 0
        
        print("IMU node started")
        print('='*50)
        
    def image_callback(self, msg):
        h, w = msg.height, msg.width
        self.image = np.array(msg.data, dtype=np.uint8)
        self.image = self.image.reshape(h, w, 3)
        self.get_logger().info("Loaded image")
        
    def accel_callback(self, msg):
        self.linear_acc = np.array([msg.linear_acceleration.x, msg.linear_acceleration.y, msg.linear_acceleration.z])
        x, y, z = self.linear_acc
        self.pitch = -np.degrees(np.arctan(x/np.sqrt(y ** 2 + z **2)))
        self.roll = -np.degrees(np.arctan(y/np.sqrt(x ** 2 + z ** 2)))
        self.yaw = np.degrees(np.arctan(z/np.sqrt(x ** 2 + z ** 2)))
        # self.roll = 90 - np.abs(np.degrees(np.arctan(y/z)))
        # self.pitch = np.degrees(np.arctan(y/np.sqrt(x ** 2 + z ** 2)))
        
        if self.counter1 % 100 == 0:
            self.get_logger().info(f"Linear acc: {self.linear_acc}")
            self.get_logger().info(f"roll:{self.roll:.3f} pitch:{self.pitch:.3f} yaw:{self.yaw:.3f}")
            print('='* 50)
            print('='* 50)   
            
        self.counter1 += 1
        
        # self.get_logger().info(f"Linear acc: {self.linear_acc}")
        # self.get_logger().info(f"roll:{self.roll:.3f} pitch:{self.pitch:.3f} yaw:{self.yaw:.3f}")
        # print('='* 50)
        # print('='* 50)   
            
    def on_key_press(self):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        imu_filename = f"{SAVE_PATH}/imu_data_{timestamp}.txt"  
        image_filename = f"{SAVE_PATH}/image_{timestamp}.png"

        # Save IMU data to a text file
        angles = np.array([self.roll, self.pitch, self.yaw])
        np.savetxt(imu_filename, angles)

        # Save image
        # self.get_logger().info(f"{self.image.shape}")
        # cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        cv2.imwrite(image_filename, self.image)
        self.get_logger().info(f"Angles:{angles}")
        self.get_logger().info(f"IMU data and image saved: {imu_filename}, {image_filename}")
        
    def gyro_callback(self, msg):
        self.angular_vel = np.array([msg.angular_velocity.x, msg.angular_velocity.y, msg.angular_velocity.z])
        
        if self.counter2 % 200 == 0:
            
            dt = 1 # replace with the actual time difference between messages
            self.roll += dt * self.angular_vel[0]
            self.pitch += dt * self.angular_vel[1]
            self.yaw += dt * self.angular_vel[2]
            
            roll_acc = np.arctan2(self.linear_acc[1], self.linear_acc[2])
            pitch_acc = np.arctan2(-self.linear_acc[0], np.sqrt(self.linear_acc[1]**2 + self.linear_acc[2]**2))

            alpha = 0.98  # adjust this value based on your requirements
            self.roll = alpha * self.roll + (1 - alpha) * roll_acc
            self.pitch = alpha * self.pitch + (1 - alpha) * pitch_acc
            
            self.get_logger().info(f"Angular vel: {self.angular_vel}")
            self.get_logger().info(f"roll:{np.degrees(self.roll):.3f} pitch:{np.degrees(self.pitch):.3f} yaw:{np.degrees(self.yaw):.3f} dt:{dt}")
            
            print('='* 50)    
            self.prev_time = float(msg.header.stamp.sec)
    
        self.counter2 += 1
        

        
    def getR(self):
        return self.position

def main(args=None):
    rclpy.init(args=args)
    imu_subscriber = IMUSubscriber()
    
    # try:
    #     rclpy.spin(imu_subscriber)
    # except KeyboardInterrupt:
    #     pass
    
    while True:
        key = input()
        if key == 'q':
            print(f"{key} pressed")            
            try:
                rclpy.spin_once(imu_subscriber)
                imu_subscriber.on_key_press()
            except KeyboardInterrupt:
                pass
        elif key == 'w':
            break
        
    imu_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


