#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def callback(data):
    # 只要收到消息，这个函数就会被触发
    rospy.loginfo("控制中心收到数据: %s", data.data)

def listener():
    # 初始化节点，名字叫 control_node
    rospy.init_node('control_node', anonymous=True)
    
    # 订阅 'chatter' 话题，收到消息就去跑 callback 函数
    rospy.Subscriber("chatter", String, callback)
    
    # 保持程序运行，别断开
    rospy.spin()

if __name__ == '__main__':
    listener()
