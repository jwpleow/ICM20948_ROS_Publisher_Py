# ICM20948 ROS (python) publisher
## setup
install this to your catkin workspace src/   

install the qwiic_i2c and qwiic_9dof_imu libraries following the instructions in their folders   
(change the i2c bus in Qwiic_I2C_Py/qwiic_i2c/linux_i2c.py, line 63, as needed)   

```
chmod +x src/ros_imu_publisher.py
```

## catkin make and stuff
In the root of the catkin workspace
```
catkin_make
source devel/setup.bash
rosrun ros_icm20948_publisher ros_imu_publisher.py
```


