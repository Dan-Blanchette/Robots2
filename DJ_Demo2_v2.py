#!/usr/bin/env python3
# Author: Dan Blanchette
# Date: 9-27-23
# Robotics Systems 2
# FanucAPI EthernetIP Python Program
# **********************************************************
# *                                                        *
# *  This program routine has our CRX10 robots pick up     *
# * a dice, place it on a conveyor, retrieve the dice,     *
# * rotate the payload 90 degrees, and then return it to   *
# * its original position.                                 *
# *                                                        *
# **********************************************************

import sys
import time
import random
"""Robot Contoller FanucAPI package: https://github.com/UofI-CDACS/FANUC-Ethernet_IP_Drivers"""
from robot_controller import robot


drive_path = '129.101.98.215' # DJ


def main():
   """! Main program entry"""

   # Create new robot object
   crx10_dj = robot(drive_path)

   # Set robot speed
   # crx10_dj.set_speed(300)
   # crx10_dj.set_pose([0,0,0,0,0,0])
   # crx10_dj.start_robot()
   # time.sleep(1)g
   pose1 = [1.0013892650604248,0.9951468110084534,0.9946738481521606,0.9981666207313538,0.9928029179573059,1.0037530660629272]
   pose2 = [12.108741760253906,25.120281219482422,-49.760894775390625,-5.92402458190918,-44.596282958984375,19.498767852783203]
   pose3 = [13.92887020111084,5.505075454711914,-0.20440399646759033,-1.389697790145874,-92.76795196533203,18.254972457885742]
   pose4 = [50.81012725830078,33.33863067626953,-7.299388885498047,0.4909592866897583,-78.49491119384766,-22.270231246948242]
   pose5 = [50.15641403198242,35.75321578979492,-16.515947341918945,0.13363459706306458,-71.42423248291016,-19.843734741210938]
   pose6 = [50.156917572021484,32.048431396484375,0.7313774824142456,0.1617249846458435,-91.14254760742188,-19.84313201904297]
   pose7 = [101.30995178222656,4.898548126220703,-6.724443435668945,-1.1304157972335815,-81.4480972290039,17.219463348388672]
   pose8 = [100.26691436767578,13.57114028930664,-30.30735969543457,-0.16435888409614563,-63.54471206665039,17.235164642333984]
   pose9 = [103.54271697998047,6.595066070556641,-4.173022270202637,1.406548023223877,-87.15010833740234,-1.3322210311889648]
   pose10 = [15.010419845581055,6.595056056976318,-4.173073768615723,1.4033803939819336,-87.15095520019531,17.059005737304688]
   pose11 = [14.409381866455078,22.351255416870117,-53.66278839111328,-0.6160216927528381,-35.430442810058594,17.05632972717285]
   
   # Reset the gripper and stop conveyor before moves
   crx10_dj.conveyor("stop")
   crx10_dj.gripper("open")
   time.sleep(1.5)

   # Home position
   crx10_dj.set_pose(pose1)
   crx10_dj.start_robot()
   time.sleep(1)

   # Approach dice target
   crx10_dj.set_pose(pose2)
   crx10_dj.start_robot()
   time.sleep(1)
   
   # Close Schunk gripper
   crx10_dj.gripper('close')
   time.sleep(1)

   # Retract arm to carry payload above conveyor 
   crx10_dj.set_pose(pose3)
   crx10_dj.start_robot()
   time.sleep(1)

   # Start the conveyor
   crx10_dj.conveyor('forward')

   # Move to place dice on conveyor
   crx10_dj.set_pose(pose4) 
   crx10_dj.start_robot()
   time.sleep(1)

   # Lower and set dice on conveyor
   crx10_dj.set_pose(pose5)
   crx10_dj.start_robot()
   time.sleep(1)

   # Open gripper
   crx10_dj.gripper('open')

   # Move linearly toward the back of the conveyor
   crx10_dj.set_pose(pose6)
   crx10_dj.start_robot()
   time.sleep(0.5)

   # Position arm over dice and rotate J6 90 Degrees
   crx10_dj.set_pose(pose7)
   crx10_dj.start_robot()
   time.sleep(1)
   
   # while the left sensor is not tripped, keep running
   while (crx10_dj.conveyor_proximity_sensor("left") == 0):
      pass
   # When the while loop is false(left sensor set to high(1)), stop the conveyor
   crx10_dj.conveyor("stop") # turn conveyor off

   # Approach dice
   crx10_dj.set_pose(pose8)
   crx10_dj.start_robot()
   time.sleep(1)

   # Close the gripper
   crx10_dj.gripper("close")
   time.sleep(0.5)
   
   # Retract arm to clear conveyor
   crx10_dj.set_pose(pose9)
   crx10_dj.start_robot()
   time.sleep(1)

   # J1 rotation back to dice start position 
   crx10_dj.set_pose(pose10)
   crx10_dj.start_robot()
   time.sleep(1)

   # Move down to deposit dice
   crx10_dj.set_pose(pose11)
   crx10_dj.start_robot()
   time.sleep(1)

   # Open gripper
   crx10_dj.gripper("open")
   time.sleep(1)

   # Return to home position
   crx10_dj.set_pose(pose1)
   crx10_dj.start_robot()
   time.sleep(1)

   # Ensure conveyor is stopped
   crx10_dj.conveyor("stop")

if __name__=="__main__":
    main()  