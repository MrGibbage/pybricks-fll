from base_robot import *

# This is a mission program. You will have one of these for each "mission"
# Normally a mission is one run from base, but there are ways to do more than
# that if needed.

def Run(br: BaseRobot):
    br.moveLeftAttachmentMotorForMillis(millis=500, speed=250)
    br.driveForDistance (600)

if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
