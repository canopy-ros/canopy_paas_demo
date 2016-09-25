#!/usr/bin/env python

import roslib
import rospy
from std_msgs.msg import Int32

class Leaflet(object):
    def __init__(self):
        self.pub = rospy.Publisher('/result', Int32,
            queue_size=10)
        self.sub = rospy.Subscriber('/client/input', Int32, self.callback)

    def callback(self, data):
        self.pub.publish(data * 2)

if __name__ == "__main__":
    rospy.init_node("leaflet", anonymous=False)
    l = Leaflet()
    rospy.spin()
