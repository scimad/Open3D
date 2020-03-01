import argparse
import open3d as o3d

class FrameGen(object):
    def __init__(self, config, source):
        self.n_frames = 0
        self.source = source
        self.sensor = o3d.io.AzureKinectSensor(config)
        self.flag_completed = False

        if self.source == 'kinect':
            if not self.sensor.connect(0):
                raise RuntimeError('Failed to connect to sensor')
        else:
            video_path = self.source
            print ("I am going to read rgbd frames from this video")
            self.reader = o3d.io.AzureKinectMKVReader()
            self.reader.open(video_path)
            self.metadata = self.reader.get_metadata()
            if not self.reader.is_opened():
                raise RuntimeError("Not a valid source: {}".format(video_path))

    def get_next_frame(self):
        if self.source == 'kinect':
            print ("lolo")
            while not self.flag_completed:
                rgbd = self.sensor.capture_frame(align_depth_to_color=True)
                if rgbd is None:
                    continue
                print ("New frame is read from sensor!")
                self.n_frames += 1
                yield rgbd, self.n_frames
        else:
            while not self.reader.is_eof() and not self.flag_completed:
                rgbd = self.reader.next_frame()
                if rgbd is None:
                    continue
                print ("New frame is read from file!")
                self.n_frames += 1
                print ("------------------- rgbd:", rgbd)
                yield (rgbd)
            self.reader.close()

class KinectFusionConfig(object):
    def __init__(self):
        self.camera_intrinsic = o3d.io.read_pinhole_camera_intrinsic('/home/scimad/EK/Work/VR360/Open3D/examples/Python/Advanced/scratch/intrinsic_config.json')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Kinect Fusion')
    parser.add_argument('--config', type=str, help='config for kinect camera (mode, FPS, width / height & so on)')
    parser.add_argument('--source', type=str, help='whether to use kinect or a video file')
    args = parser.parse_args()    
    if args.config is not None:
        config = o3d.io.read_azure_kinect_sensor_config(args.config)
    else:
        config = o3d.io.AzureKinectSensorConfig()

    frame_gen = FrameGen(config, args.source)

    my_kinfu_config = KinectFusionConfig()
    
    #TODO: Retrieve Calibrarion: https://github.com/microsoft/Azure-Kinect-Samples/blob/edb6c364eb7fb86638327c7a1b3da1833b85d9a0/opencv-kinfu-samples/main.cpp#L432
    #TODO: Start Cameras
    #TODO: Initialize Kinfu parameters
    #TODO: Initialize Distortion coefficients
    #TODO: Create KinectFusion Module Instance
    #TODO: LoopOver
    frame = frame_gen.get_next_frame()
    vis = o3d.visualization.VisualizerWithKeyCallback()
    # vis.register_key_callback(glfw_key_escape, self.escape_callback)
    vis.create_window('viewer', 1920, 540)
    while True:
        rgbd = next(frame)
        vis_geometry_added = False
        if rgbd is None:
            continue

        if not vis_geometry_added:
            vis.add_geometry(rgbd)
            vis_geometry_added = True

        vis.update_geometry(rgbd)
        vis.poll_events()
        vis.update_renderer()


        #TODO: Read depth frame and depth image
        #TODO: Update KinectFusion
        #TODO: Retrieve rendered TSDF
        #TODO: Retrieve fused point cloud and normals
        #TODO: Show TSDF rendering
        #TODO: show fused point cloud and normals
        



