import argparse
import open3d as o3d

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Kinect Fusion')
    parser.add_argument('--config', type=str, help='input json kinect config')

    args = parser.parse_args()    
    if args.config is not None:
        config = o3d.io.read_azure_kinect_sensor_config(args.config)
    else:
        config = o3d.io.AzureKinectSensorConfig()

    sensor = o3d.io.AzureKinectSensor(config)
    if not sensor.connect(0):
        raise RuntimeError('Failed to connect to sensor')

    #TODO: Retrieve Calibrarion: https://github.com/microsoft/Azure-Kinect-Samples/blob/edb6c364eb7fb86638327c7a1b3da1833b85d9a0/opencv-kinfu-samples/main.cpp#L432
    #TODO: Start Camera
    #TODO: Generate a pinhole model for depth camera
    #TODO: Retrieve calibration parameters (and width and height)
    #TODO: Initialize Kinfu parameters
    #TODO: Initialize Distortion coefficients
    #TODO: Create KinectFusion Module Instance
    #TODO: LoopOver
        #TODO: Read depth frame and depth image
        #TODO: Update KinectFusion
        #TODO: Retrieve rendered TSDF
        #TODO: Retrieve fused point cloud and normals
        #TODO: Show TSDF rendering
        #TODO: show fused point cloud and normals
        



