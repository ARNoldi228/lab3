#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Int16MultiArray
rospy.init_node('summing')
def callback(msg):
  array = msg.data
  rospy.loginfo('Summing hears %s', array)
  sumofel = sum(array)
  sum_msg = Int16()
  sum_msg.data = sumofel
  rospy.loginfo('Summing sends %s', sum_msg.data)
  pub.publish(sum_msg)  
pub = rospy.Publisher('sumreq', Int16, queue_size=10)
rospy.Subscriber('polysum', Int16MultiArray, callback, queue_size=10)
rospy.spin()
