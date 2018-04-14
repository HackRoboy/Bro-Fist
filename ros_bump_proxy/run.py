
#! /usr/bin/env python

from __future__ import print_function
import rospy
import actionlib
from roboy_communication_control.msg import PerformMovementAction

def makeFistbump():
    client = actionlib.SimpleActionClient(
        'shoulder_left_movements_server',
        PerformMovementAction)
    print("Waiting for Server")
    client.wait_for_server()
    bumpAction = PerformMovementAction()
    bumpAction.action = "shoulder_left_gogogo"
    client.send_goal(bumpAction)
    client.wait_for_result()
    return client.get_result()

if __name__ == '__main__':
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('fistbump_client_py')
        result = makeFistbump()
        print("Result:", ', '.join([str(n) for n in result.sequence]))
    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)

