import numpy as np
import cv2 
import os

def decompose_projection_matrix(P):
    # Intrinsic matrix K
    K = P[:, :3]
    K /= K[2, 2]  # Normalize K to have K[2, 2] = 1

    # Extrinsic matrix [R|t]
    K_inv = np.linalg.inv(K)
    R = np.dot(K_inv, P)[:, :3]
    t = np.dot(K_inv, P)[:, 3]

    return K, R, t

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

# Example usage
# Replace this with your actual projection matrix
P = np.array([[642.846, 0, 646.711, 0],
              [0, 641.3025, 362.441, 0],
              [0, 0, 1, 0]])

K, R, t = decompose_projection_matrix(P)

print(K)
print(R)
print(t)
