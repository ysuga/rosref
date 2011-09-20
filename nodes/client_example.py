#!/usr/bin/env python

import roslib; roslib.load_manifest('refrection_service')

import sys

import rospy

from refrection_service.srv import *

def remote_command_client(x, y, z):
    rospy.wait_for_service('refrection')
    try:
        refrection = rospy.ServiceProxy('refrection', Refrection)
        resp1 = refrection(x, y, z)
        return resp1.ret
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

        
def usage():
    return '''
    Usage: client_example.py [x, y, z]
      x - msg, srv, topic, service
      y - md5, show (x = msg, srv)
          type      (y = topic, service)
      z - topic name or service name (x = msg, srv)
          topic type name or service type name (x = topic, service)
    '''


if __name__ == '__main__':
    if len(sys.argv) == 4:
        x = (sys.argv[1])
        y = (sys.argv[2])
        z = (sys.argv[3])
    else:
        print usage()
        sys.exit(1)

    print "ros%s %s %s = %s" % (x, y, z, remote_command_client(x, y, z))
       
