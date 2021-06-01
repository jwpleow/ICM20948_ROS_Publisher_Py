#!/usr/bin/env python3

import rospy
import time
import sys
from sensor_msgs.msg import MagneticField, Imu
from std_msgs.msg import Float64
import qwiic_icm20948


def icm20948_node():
    # Initialize ROS node
    raw_pub = rospy.Publisher('imu/data_temp', Imu, queue_size=10)
    mag_pub = rospy.Publisher('imu/mag', MagneticField, queue_size=10)
    rospy.init_node('icm20948')

    rate = rospy.Rate(100)
    rospy.loginfo("ICM20948 IMU publisher node launched. Publishing to /imu/data_temp and /imu/mag.")

    IMU = qwiic_icm20948.QwiicIcm20948()

    while IMU.connected == False:
        message = "The Qwiic ICM20948 device cannot be found. Check your connection or i2c bus number specified in Qwiic_I2C."
        rospy.loginfo(message)

    IMU.begin()

    while not rospy.is_shutdown():
        if IMU.dataReady():
            timestamp = rospy.Time.now()
            IMU.getCorrectedAgmt()
            raw_msg = Imu()
            raw_msg.header.stamp = timestamp
            raw_msg.header.frame_id = "imu_link"
            
            raw_msg.linear_acceleration.x = IMU.ax
            raw_msg.linear_acceleration.y = IMU.ay
            raw_msg.linear_acceleration.z = IMU.az

            raw_msg.angular_velocity.x = IMU.gx
            raw_msg.angular_velocity.y = IMU.gy
            raw_msg.angular_velocity.z = IMU.gz

            raw_msg.orientation_covariance[0] = -1
            raw_msg.linear_acceleration_covariance[0] = -1
            raw_msg.angular_velocity_covariance[0] = -1

            raw_pub.publish(raw_msg)

            mag_msg = MagneticField()
            mag_msg.header.stamp = timestamp
            mag_msg.header.frame_id = "imu_link"
            mag_msg.magnetic_field.x = IMU.mx
            mag_msg.magnetic_field.y = IMU.my
            mag_msg.magnetic_field.z = IMU.mz
            mag_msg.magnetic_field_covariance[0] = -1
            mag_pub.publish(mag_msg)

        rate.sleep()

    rospy.loginfo("ICM20948 publisher node closing")


if __name__ == '__main__':
    try:
        icm20948_node()
    except rospy.ROSInterruptException:
        rospy.loginfo(rospy.get_caller_id() +
                      "  icm20948 node exited with exception.")
