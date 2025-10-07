import numpy as np
import cv2
import os
from scipy.spatial.transform import Rotation
from rotation_utils import get_R
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

K_true = np.array([[378.46, 0, 322.5703430175781], [0, 378.0471496582031, 242.00010681152344], [0, 0, 1]])

def mse(a, b):
    return np.mean((a - b) ** 2)

def calibrate_camera(images, pattern_size, square_size):
    # Prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    objp = np.zeros((pattern_size[0] * pattern_size[1], 3), np.float32)
    objp[:, :2] = np.mgrid[0:pattern_size[0], 0:pattern_size[1]].T.reshape(-1, 2) * square_size

    # Arrays to store object points and image points from all the images
    objpoints = []  # 3D points in real world space
    imgpoints = []  # 2D points in image plane

    for image_path in images:
        img = cv2.imread(image_path)[:, :, :3]
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Find the chessboard corners
        ret, corners = cv2.findChessboardCorners(gray, pattern_size, None)
        
        # If corners are found, add object points, image points
        if ret:
            objpoints.append(objp)
            imgpoints.append(corners)

            # Draw and display the corners
            cv2.drawChessboardCorners(img, pattern_size, corners, ret)
            plt.imsave(f'./checkerboard-corners/{image_path.split("/")[-1]}', img)
          
    # Calibrate the camera
    ret, K, dist_coeff, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

    return K, rvecs, tvecs

# Example usage
# calibration_images = ["./data_realsense/1380.jpg"]
files = [os.path.join('./data_imu_and_image', i) for i in sorted(os.listdir('./data_imu_and_image/'))]
calibration_images, R_imu, angles_imu = [], [], []


for f in files:
    if f.split('.')[-1] == 'png':
        calibration_images.append(f)
    else:
        with open(f) as txt_file:
            data = txt_file.read().split('\n')
            data = [float(d) for d in data[:-1]]
            R = get_R(np.radians(data[0]), np.radians(data[1]), 0)
            angles_imu.append([data[0] % 360, data[1] % 360, 0])
            R_imu.append(R)    
            
            
def solver(x, target):
    R = get_R(x[0], x[1], x[2])
    return np.linalg.norm(R - target, axis=-1)

def get_angles_using_fsolve(target_R):
    initial = np.random.uniform(-np.pi/2, np.pi/2, (3, ))
    solution = fsolve(solver, initial, args=(target_R, ))
    return [np.degrees(i) % 360 for i in solution]

def main():
    # calibration_images = ['./data_realsense/checkerboard.png']
    checkerboard_pattern_size = (8, 6)  # Change this to the size of your checkerboard pattern
    square_size = 8.5  # Change this to the size of each square in your checkerboard in any unit

    camera_matrix, rotation_vectors, translation_vectors = calibrate_camera(calibration_images, checkerboard_pattern_size, square_size)

    print("Predicted Camera Matrix:")
    print(camera_matrix)
    print("True Camera Matrix:")
    print(K_true)
    print(f"Error: {mse(K_true, camera_matrix)}")
    print("=" * 100)

    for i in range(len(rotation_vectors)):
        print(f"\nPose {i + 1}:")
        print("Rotation Matrix (Camera wrt World using camera calibration):")
        rotation_matrix, _ = cv2.Rodrigues(rotation_vectors[i])
        print(rotation_matrix)  
        print("Rotation Matrix (IMU wrt World from IMU Data):")
        print(R_imu[i])
        print("Rotation Matrix (IMU wrt Camera):")
        print((R_imu[i].T @ rotation_matrix))
        print(f"True angles: {angles_imu[i]}")
        print(f"Predicted angles: {get_angles_using_fsolve(rotation_matrix)}")
        print(f"Error: {mse(rotation_matrix, R_imu[i])}")
    
        print("=" * 100)
        
if __name__ == "__main__":
    main()