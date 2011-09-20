#!/usr/bin/env python
"""
filename    : refrection_service.py
author      : Yuki Suga (ysuga@ysuga.net)
date        : 2011/09/07
language    : python
description : This service allows the service client to know 
              the detail information of the service and topic
              provided. The aim of this service is to provide
              refrection service for the remote PCs that have
              no ROS filesystem.
"""
import roslib; roslib.load_manifest('refrection_service')

from refrection_service.srv import *
import rospy

import subprocess

def handle_refrection(req):
    """
    Currently, this service allows commands below:
    A: command = srv (rossrv)
        option = show --- return the detail information of arg 
        option = md5  --- return md5sum of arg
    B: command = msg (rosmsg)
        option = show --- return the detail information of arg
        option = md5  --- return md5sum of arg

    Memo: using this framework, ros service can allow any kinds
          of command-line execution, so I will be a very strong
          tool but dangerous... That's why I just allow the service
          client to use two commands 'srv' and 'msg'.
    """

    """
    Pattern check
    """
    availableCommands = (('srv', 'msg'), ('service', 'topic'))
    availableOptions  = (('md5', 'show'), ('type'))

    for ac, ao in zip(availableCommands, availableOptions):
        if req.command in ac and req.option in ao:
            stringList = []
            stringList.append('ros')
            stringList.append(req.command)
            stringList.append(' ')
            stringList.append(req.option)
            stringList.append(' ')
            stringList.append(req.arg)
            cmd = ''.join(stringList)
            output = subprocess.check_output(cmd, shell=True)
            return RefrectionResponse(output)
    return RefrectionResponse('unsupported command')

def refrection_server():
    rospy.init_node('refrection_service_node')
    s = rospy.Service('refrection', Refrection, handle_refrection)
    print "Ready"
    rospy.spin()

if __name__ == '__main__':
    refrection_server()
