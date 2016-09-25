#!/usr/bin/env python

import roslib
import rospy
from std_msgs.msg import Int32

class Client(object):
    def __init__(self):
        self.pub = rospy.Publisher('/input', Int32,
                                   queue_size=10)
        r = rospy.Rate(5)
        i = 0
        while not rospy.is_shutdown():
            self.pub.publish(i)
            i += 1
            r.sleep()

if __name__ == "__main__":
    rospy.init_node("client", anonymous=False)
    c = Client()
