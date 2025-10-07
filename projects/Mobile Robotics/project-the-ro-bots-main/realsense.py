import numpy as np
import cv2
import pyrealsense2 as rs
import matplotlib.pyplot as plt

pipe = rs.pipeline()
cfg = rs.config()

print("cfg created")

cfg.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 100)
cfg.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 100)

cfg.enable_stream(rs.stream.gyro, rs.format.motion_xyz32f, 200)
cfg.enable_stream(rs.stream.accel, rs.format.motion_xyz32f, 63)


pipe.start(cfg)
print("pipe started")

counter = 0

while True:
    frame = pipe.wait_for_frames()
    depth = frame.get_depth_frame()
    color = frame.get_color_frame()
    
    accel_frame = frame.first_or_default(rs.stream.accel)
    gyro_frame = frame.first_or_default(rs.stream.gyro)
    
    depth_image = np.asanyarray(depth.get_data())
    color_image = np.asanyarray(color.get_data())
    
    if counter % 30 == 0:
        plt.imsave(f'./data_realsense/{counter}.jpg', color_image)
    
    counter += 1    
    
    cv2.imshow('rgb', color_image)
    
    # ic(accel_frame)
    # ic(gyro_frame)    
    # cv2.imshow('rgb', color_image)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
    
    

pipe.stop()


# roslaunch realsense2_camera rs_camera.launch enable_gyro:=true enable_accel:=true unite_imu_method:=2-linear_interpolation
# rostopic echo /camera/accel/sample
# rostopic echo /camera/gyro/smaple
    
    
    
# height: 720
# width: 1280
# distortion_model: plumb_bob
# d:
# - -0.054603107273578644
# - 0.06334752589464188
# - 0.00022518340847454965
# - 0.0002921034465543926
# - -0.020296046510338783
# k:
# - 642.8469848632812
# - 0.0
# - 646.7113037109375
# - 0.0
# - 641.3025512695312
# - 362.441162109375
# - 0.0
# - 0.0
# - 1.0
# r:
# - 1.0
# - 0.0
# - 0.0
# - 0.0
# - 1.0
# - 0.0
# - 0.0
# - 0.0
# - 1.0
# p:
# - 642.8469848632812
# - 0.0
# - 646.7113037109375
# - 0.0
# - 0.0
# - 641.3025512695312
# - 362.441162109375
# - 0.0
# - 0.0
# - 0.0
# - 1.0
# - 0.0
