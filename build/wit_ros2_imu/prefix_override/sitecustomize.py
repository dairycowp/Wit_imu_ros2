import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/hu/ros2_ws/wit_imu_ros2/install/wit_ros2_imu'
