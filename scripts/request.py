#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Int16MultiArray
rospy.init_node('request')
pub = rospy.Publisher('reqpol', Int16MultiArray, queue_size=10)
rate = rospy.Rate(1)

def callback(msg):
  rospy.loginfo('Summing hears %s', msg.data)
  rospy.Subscriber('sumreq' , Int8, callback, queue_size=10)
def Req():
  poly_msg = Int16MultiArray()
  var = [2, 4, 5]
  while not rospy.is_shutdown():
   poly_msg.data = var
   rospy.loginfo('Request sends %s', poly_msg.data)
   pub.publish(poly_msg)
   rate.sleep()
try:
  Req()
except (rospy.ROSInterruptException, KeyboardInterrupt):
  rospy.logerr('Exception catched')
