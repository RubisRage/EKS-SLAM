import numpy as np
from math import pi

log = "medium_nd_5.log"

dt = 0.1  # seconds

# State matrix X
X = np.zeros((3,))

# Covariance matrix
P = np.zeros((3, 3))

# Prediction model noise
sigmaV = 0.3        # m/s
sigmaG = 3.*pi/180  # radians

Q = 0.3
# Q = np.array([
# [sigmaV**2, 0],
# [0, sigmaG**2]
# ])

# Observe model noise
sigmaR = 0.1        # meters
sigmaB = 1.*pi/180  # radians

R = np.array([
    [sigmaR**2, 0],
    [0, sigmaB**2]
])

INNER_GATE = 4.0
OUTER_GATE = 25.0