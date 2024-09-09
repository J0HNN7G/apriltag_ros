from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([
        # Declare the launch arguments
        DeclareLaunchArgument(
            'image_rect',
            default_value='/image_raw',
            description='Topic for rectified image'
        ),
        DeclareLaunchArgument(
            'camera_info',
            default_value='/camera_info',
            description='Topic for camera info'
        ),
        DeclareLaunchArgument(
            'namespace',
            default_value='apriltag',
            description='Namespace for the node'
        ),
        DeclareLaunchArgument(
            'params_file',
            default_value='',
            description='Path to the parameters YAML file'
        ),
        
        # Node for the AprilTag detection
        Node(
            package='apriltag_ros',
            executable='apriltag_node',
            name='apriltag',
            namespace=LaunchConfiguration('namespace'),
            remappings=[
                ('/apriltag/image_rect', LaunchConfiguration('image_rect')),
                ('/apriltag/camera_info', LaunchConfiguration('camera_info'))
            ],
            parameters=[LaunchConfiguration('params_file')],
            output='screen'
        ),
    ])

