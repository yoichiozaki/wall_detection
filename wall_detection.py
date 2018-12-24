#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Bool

THRESHOLD = 10
pub = rospy.Publisher('wall_is_near', Bool, queue_size = 1)

def callback(msg):
    angle_min = msg.angle_min
    angle_max = msg.angle_max
    angle_increment = msg.angle_increment
    n = 0
    counter = 0
    for r in msg.ranges:
        theta = angle_min + n * angle_increment
        # print "theta = " + str(theta)
        if  (-2.4908916 <= theta <= -0.480175) or (0.480175 <= theta <= 2.4908916):
            if r <= 0.75: # 0.3
                counter = counter + 1
                if THRESHOLD <= counter:
                    print "detected wall on left or right"
                                pub.publish(True)
                    return
            n = n + 1
            continue
        elif -0.480175 < theta < 0.480175:
            if r < 1.0: # 0.4
                counter = counter + 1
                if THRESHOLD <= counter:
                    print "detected wall ahead"
                                pub.publish(True)
                    return
            n = n + 1
            continue
        else:
            if r < 0.75: # 0.2
                counter = counter + 1
                if THRESHOLD <= counter:
                    print "detected wall aback"
                                pub.publish(True)
                    return
            n = n + 1
            continue
    pub.publish(False)


def wall_detection():
    rospy.init_node('wall_detection')
    sub = rospy.Subscriber('scan', LaserScan, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        wall_detection()
    except rospy.ROSInterruptException:
        pass
