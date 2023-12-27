import numpy as np
import cv2
from PIL import Image

def get_limits(color):
    """Função que retorna o limite de cores, no caso o amarelo

    Args:
        color (list): Lista que contem as cores da imagem

    Returns:
        _type_: retorna um array numpy que corresponde ao intervalo de cores
    """
    c = np.uint8([[color]])  # BGR values
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    hue = hsvC[0][0][0]  # Get the hue value

    # Handle red hue wrap-around
    if hue >= 165:  # Upper limit for divided red hue
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([180, 255, 255], dtype=np.uint8)
    elif hue <= 15:  # Lower limit for divided red hue
        lowerLimit = np.array([0, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)
    else:
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit

def get_color(frame, color):
    """Get the frame color

    Args:
        frame (opencv): The frame captured from the webcam
        color (list): A list corresponding to the color you want to detect

    Returns:
        _type_: bbox of detected color
    """
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lowerLimit, upperLimit = get_limits(color=color)
    
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
    
    mask_ = Image.fromarray(mask)
    
    # Return cords of object from the image
    bbox = mask_.getbbox()
    
    # Draw a rectangle
    
    if bbox is not None:
        return bbox