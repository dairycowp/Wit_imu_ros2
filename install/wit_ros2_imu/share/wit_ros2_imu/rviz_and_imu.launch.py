from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    rviz_and_imu_node = Node(
        package='wit_ros2_imu',
        executable='wit_ros2_imu',
        name='imu',
        remappings=[('/wit/imu', '/imu/data')],
        parameters=[{'port': '/dev/ttyUSB0'},
                    {"baud": 115200}],
        output="screen"
    )

    rviz_display_node = Node(
        package='rviz2',
        executable="rviz2",
        output="screen"
    )

    return LaunchDescription(
        [
            rviz_and_imu_node,
            rviz_display_node  # 取消注释以启动 RViz 节点
        ]
    )