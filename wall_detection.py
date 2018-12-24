#! /usr/bin/env python
 
import rospy
from sensor_msgs.msg import LaserScan
 
THRESHOLD = 50 # 危険領域内に50個以上の点があったら壁の近くとする
wall_is_near_flag = False
pub = rospy.Publisher('wall_is_near', Bool)

def callback(msg):
    print len(msg.ranges)
    angle_min = msg.angle_min
    angle_max = msg.angle_max
    angle_increment = msg.angle_increment
    n = 0
    counter = 0
    for r in msg.ranges:
    	theta = angle_min + n * angle_increment
    	if  (-2.4908916 <= theta <= -0.480175) or (0.480175 <= theta <= 2.4908916): # 左右
    		if r <= 0.3:
    			counter = counter + 1
    			if THRESHOLD <= counter:
    				wall_is_near_flag = True
    				print "detected wall on left or right"
    				return
    		n = n + 1
    		continue
    	elif -0.480175 < theta < 0.480175: # 前
    		if r < 0.4:
    			counter = counter + 1
    			if THRESHOLD <= counter:
    				wall_is_near_flag = True
    				print "detected wall ahead"
    				return
    		n = n + 1
    		continue
    	else: # 後ろ
    		if r < 0.2:
    			counter = counter + 1
    			if THRESHOLD <= counter:
    				wall_is_near_flag = True
    				print "detected wall aback"
    				return
    		n = n + 1
    		continue

def wall_detection():
	rospy.init_node('wall_detection')
	sub = rospy.Subscriber('pc2', LaserScan, callback)
	pub.publish(wall_is_near_flag)
	rospy.spin()

if __name__ == '__main__':
	try:
		wall_detection()
	except rospy.ROSInterruptException: 
		pass
