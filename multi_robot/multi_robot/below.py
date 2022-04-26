import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

from math import pi
def talker ():
    pub = rospy.Publisher('/below/cmd_vel', Twist , queue_size =10)
    rospy.init_node("below", anonymous=True)
    rate = rospy.Rate (1) # 10hz
   
    while not rospy.is_shutdown ():
        message = Twist()
        message.linear.x = 0.7
        message.linear.y = 0
        pub.publish(message)
        
if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass