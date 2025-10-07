import numpy as np

def Rx(theta) -> np.array:
    return np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta), np.cos(theta)]
    ])

def Ry(theta) -> np.array:
    return np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])

def Rz(theta) -> np.array:
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])

def get_R(alpha=0, beta=0, gamma=0) -> np.array:
    return Rx(gamma) @ Ry(beta) @ Rz(alpha)

def get_T(theta, translation):
    R = get_R(*theta)
    translation = np.array(translation)
    T = np.zeros((4,4))
    T[0:3, 0:3] = R
    T[:3, 3] = translation
    T[3, 3] = 1
    return T