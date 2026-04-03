# Sensor Examples

This folder provides a collection of **Isaac Sim sensor example scripts** for common embodied AI and robotics workflows.

## Included Examples

- `common.py`
  Shared helper utilities for stage setup, asset loading, and sensor attachment.
- `rgb_camera_example.py`
  Create an RGB camera and save rendered images.
- `depth_camera_example.py`
  Create a camera configured for depth output and show how to capture depth-related data.
- `lidar_example.py`
  Attach a LiDAR sensor to a robot or a fixed mount.
- `imu_example.py`
  Attach an IMU sensor and prepare it for motion-state reading.
- `semantic_segmentation_example.py`
  Example for semantic labeling and segmentation-oriented capture.
- `pointcloud_capture_example.py`
  Demonstrates a point-cloud style sensor setup workflow.
- `multi_sensor_robot_example.py`
  Attach multiple sensors to one mobile robot.
- `occupancy_map_export_example.py`
  A scaffold showing how occupancy-map workflows can be organized.
- `synthetic_data_writer_example.py`
  A scaffold for synthetic data generation and dataset writing.

## Notes

These scripts are written in **English** and follow a modular project style suitable for GitHub repositories.

Because Isaac Sim sensor APIs can vary across versions, these examples are designed as **clean repository-ready templates**.
You may need to slightly adapt API names or extensions depending on your Isaac Sim version.

## Typical Usage

1. Start Isaac Sim.
2. Open the **Script Editor**.
3. Copy one example file into the editor, or run it with your Isaac Sim Python environment.
4. Adjust asset paths, output paths, and sensor parameters as needed.
