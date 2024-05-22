from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
import scipy
import math
from random import randint


def get_nonzero(image: ndarray) -> ndarray:
    nonzero_x = np.nonzero(255 - image)[0]
    nonzero_y = np.nonzero(255 - image)[1]
    pairs = np.vstack((nonzero_x, nonzero_y)).T
    return pairs

def choice(pixels: ndarray)-> tuple:
    n = len(pixels)
    idx1 = randint(0, n - 1)
    pixel1 = pixels[idx1]
    idx2 = randint(0, n - 1)
    if (idx2 == idx2):
        idx2 = (idx2 + 1) % n
    pixel2 = pixels[idx2]
    return (pixel1, pixel2)

def random_radon_transformation(image: ndarray, rho_steps: int = 220, theta_steps: int = 440, n_iter: int = int(1e5)):

    nonzero_pixels = get_nonzero(image)

    a = image.shape[1]
    b = image.shape[0]

    n_rhos = 2 * rho_steps
    n_thetas = theta_steps

    rho_max = np.sqrt(a ** 2 + b ** 2)
    rho_step = rho_max / rho_steps
    theta_step = np.pi / n_thetas
    
    R = np.zeros((n_rhos, n_thetas), dtype='float64')
    for i in range(n_iter):
        pixel1, pixel2 = choice(nonzero_pixels)

        x_1 = pixel1[0]
        y_1 = pixel1[1]
        x_2 = pixel2[0]
        y_2 = pixel2[1]

        theta = np.pi / 2
        if (y_1 != y_2):
            theta = np.arctan((x_2 - x_1) / (y_1 - y_2))
        if (theta < 0):
            theta = np.pi + theta
        rho = x_1 * np.cos(theta) + y_1 * np.sin(theta)

        rho += rho_max 

        theta_int = int(theta / theta_step)
        rho_int = int(rho / rho_step)
        R[rho_int][theta_int] += 1

    m = np.max(np.unique(R))
    R *= (255/m)
    return R


