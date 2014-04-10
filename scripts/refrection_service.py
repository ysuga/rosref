#!/usr/bin/env python
from rosref.srv import *
#import roslib; roslib.load_manifest('rosref')
import rospy
import sys, traceback
import subprocess



def refrection_srv(cmd):
    cmd = ['ros'+cmd.command, cmd.option, cmd.arg]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    ret = p.wait()
    st = p.stdout.read()
    return st
   
def refrection_server():
    rospy.init_node('rosref')
    s = rospy.Service('refrection', Refrection, refrection_srv)
    print 'Ready'
    rospy.spin()


if __name__ == '__main__':
    try:
        print 'initializing'
        refrection_server()
    except:
        traceback.print_exc()
