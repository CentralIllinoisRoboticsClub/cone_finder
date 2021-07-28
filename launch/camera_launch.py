from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            node_name='opencv_cam',
            package='opencv_cam',
            node_executable='opencv_cam_main',
            output='screen',
            parameters=[{
                'index': 2,
                #'fps': 256000,  # A3
                'camera_frame_id': 'laser',
                #'width': False,
                #'height': True,
            }],
            
            remappings=[('image_raw', 'camera/image_raw')]
        ),
    ])
