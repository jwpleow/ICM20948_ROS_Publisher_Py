# ICM20948 ROS (python) publisher
## Setup
install this to your catkin workspace src/   

install the Qwiic_I2C_Py and Qwiic_9DoF_IMU_ICM20948_Py libraries following the instructions in their folders   
(change the i2c bus in Qwiic_I2C_Py/qwiic_i2c/linux_i2c.py, line 63, as needed)   
(these are not pure copies of the original libraries - the IMU library has been modified to return the scaled IMU readings, and I've changed the default i2c bus in Qwiic_I2C_Py)   
```
chmod +x src/ros_imu_publisher.py
```

## Run
In the root of the catkin workspace
```
catkin_make
source devel/setup.bash
rosrun ros_icm20948_publisher ros_imu_publisher.py
```


