import numpy as np
from styx_msgs.msg import TrafficLight
import cv2

class TLClassifier(object):
    def __init__(self):
        pass

    def get_classification(self, image):
        """Determines the color of the traffic light in the image
        Args:
            image (cv::Mat): image containing the traffic light
        Returns:
            int: ID of traffic light color (specified in styx_msgs/TrafficLight)
        """

        hsvIm = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        pixCount=50
        ###red light
        thdMin = np.array([0, 100, 100],np.uint8)
        thdMax = np.array([10, 255, 255],np.uint8)        
        binIm1 = cv2.inRange(hsvIm, thdMin, thdMax)

        thdMin = np.array([160, 100, 100],np.uint8)
        thdMax = np.array([180, 255, 255],np.uint8)
        binIm2 = cv2.inRange(hsvIm, thdMin, thdMax)
        pixSums=cv2.countNonZero(binIm1) + cv2.countNonZero(binIm2)
        if  pixSums > pixCount:
            return TrafficLight.RED
        ###Yellow light
        #thdMin = np.array([30, 100, 100],np.uint8)
        #thdMax = np.array([45, 255, 255],np.uint8)
        #binIm = cv2.inRange(hsvIm, thdMin, thdMax)
        #pixSums=cv2.countNonZero(binIm)
        #if  pixSums > pixCount:
        #    return TrafficLight.YELLOW
        ###green light
        #thdMin = np.array([64, 100, 100],np.uint8)
        #thdMax = np.array([100, 255, 255],np.uint8)
        #binIm = cv2.inRange(hsvIm, thdMin, thdMax)
        #pixSums=cv2.countNonZero(binIm)
        #if  pixSums > pixCount:
        #    return TrafficLight.GREEN

        return TrafficLight.UNKNOWN
