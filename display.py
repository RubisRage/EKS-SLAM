import cv2
import numpy as np
from slam_types import Laser
from utils import cartesian_coords
import config


def to_display_space(p):
    return (int(p[0]*config.meters_to_px_ratio + config.meters_to_px_ratio),
            int(p[1]*config.meters_to_px_ratio) + config.frame_height // 2)


def display_raw_points(frame: np.array, X: np.array, laser: Laser):

    cv2.circle(frame, (int(config.meters_to_px_ratio),
                       config.frame_height // 2), 5, (0, 0, 255), cv2.FILLED)

    for p in cartesian_coords(laser):

        cv2.circle(frame, to_display_space(p), 2, (0, 0, 0), cv2.FILLED)


counter = 0


def display_extracted_lines(frame: np.array, X: np.array, lines, z):
    global counter

    print("Scan no: %d" % counter)

    for line in lines:
        m, b, associated, associatedCount = line

        internal_counter = 0

        print("Associated count no %d: %d" %
              (internal_counter, associatedCount))

        internal_counter += 1

        p1 = to_display_space(associated[0])
        p2 = to_display_space(associated[associatedCount-1])
        cv2.line(frame, p1, p2, (0, 0, 255), 2)

    counter += 1