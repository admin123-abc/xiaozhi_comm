#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def talker():
    # 初始化节点，名字叫 sensor_node
    rospy.init_node('sensor_node', anonymous=True)
    
    # 创建一个发布者，话题叫 'chatter'，消息类型是 String
    pub = rospy.Publisher('chatter', String, queue_size=10)
    
    # 设置循环频率，1秒钟发10次
    rate = rospy.Rate(10) 
    
    while not rospy.is_shutdown():
        hello_str = "机器人 Xiao 正在发送数据 %s" % rospy.get_time()
        rospy.loginfo(hello_str) # 在终端打印日志
        pub.publish(hello_str)   # 真正把消息发出去
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
