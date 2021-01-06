#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32


def cb(message):
    rospy.loginfo(message.data)
    if message.data%2==0:
        print('2')
    if message.data%3==0:
        print('3')
    if message.data%5==0:
        print('5')
    if message.data%7==0:
        print('7')

rospy.init_node('twice')
sub = rospy.Subscriber('count_up' , Int32, cb)
rospy.spin()
