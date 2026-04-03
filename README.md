# multi_environment_isaac_sim_Script

[![IsaacSim](https://img.shields.io/badge/IsaacSim-5.1.0-b.svg)](https://docs.isaacsim.omniverse.nvidia.com/5.1.0/index.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository provides multiple complex simulation scenarios for **NVIDIA Isaac Sim**.  
All scenes are built with **Isaac Sim native assets** and can be directly imported into Isaac Sim through the **Script Editor** or executed as standalone Python scene scripts.

The repository includes both:

- **single scenario scripts**
- **multi-environment scene generation scripts**

These scenes are designed for robotics research, embodied AI experiments, navigation, manipulation, multi-robot coordination, warehouse automation, hospital service simulation, and quadruped mobility testing.

---

# Script Editor

You can use the **Script Editor** in Isaac Sim to directly import and generate scenes, or you can run the provided Python scripts to load the environments automatically.

<p align="center">
  <img src="https://github.com/user-attachments/assets/f1f82c7a-f63c-4d7d-9402-72617e2e1c71" alt="Isaac Sim Script Editor" />
</p>

Typical usage:

1. Open **Isaac Sim**
2. Open **Window → Script Editor**
3. Copy one of the scene scripts into the editor
4. Run the script
5. The corresponding scenario will be generated under `/World/...`

---

# Environment

## Recommended Environment

This project is recommended to run under the following environment:

- **NVIDIA Isaac Sim 5.1.0**
- **Python environment bundled with Isaac Sim**
- **Isaac Sim Script Editor** or standalone Isaac Sim Python execution
- NVIDIA GPU with proper Omniverse / Isaac Sim support
- Linux or Windows with Isaac Sim correctly installed

## Asset Dependency

All scenes are built using **Isaac Sim built-in / NVIDIA official asset libraries**.  
The scripts use native asset loading methods and are intended to work directly inside Isaac Sim without requiring third-party USD scene packages.

## Supported Use Cases

These scenarios can be used for:

- robot navigation
- autonomous inspection
- warehouse logistics simulation
- mobile manipulation
- service robotics
- multi-robot cooperation
- quadruped locomotion testing
- embodied AI data generation
- task planning and policy evaluation
- sim-to-real pipeline prototyping

---

# Scene List

This repository currently contains the following six complex scenarios.

---

## 1. Warehouse Mixed Fleet Complex

**Script:** `warehouse_mixed_fleet_complex.py`

### Overview
This scene simulates a complex warehouse environment with a mixed robotic fleet.  
It combines mobile robots, forklifts, manipulators, pallets, cargo obstacles, and narrow transport corridors to create a realistic logistics setting.

### Included Elements

- warehouse-style environment
- Nova Carter mobile robot
- Forklift platform
- Franka robotic arm
- pallets and cargo stacks
- narrow aisles
- box obstacles
- loading and transport zones


---

## 2. Dual Arm Sorting Cell Complex

**Script:** `dual_arm_sorting_cell_complex.py`

### Overview
This scene represents a dual-arm industrial sorting workstation.  
It is designed for robotic manipulation, pick-and-place research, conveyor-based item handling, and coordination between robotic arms and mobile units.

### Included Elements

- industrial workstation layout
- dual Franka robotic arms
- sorting tables
- conveyor structure
- bins / sorting containers
- object placement areas
- support mobile robot platform
- cluttered manipulation workspace



---

## 3. Hospital Inspection And Service Complex

**Script:** `hospital_inspection_and_service_complex.py`

### Overview
This scene simulates a hospital or indoor medical service environment.  
It is suitable for service robots, inspection robots, indoor navigation research, and mobile assistance tasks in narrow and partially cluttered spaces.

### Included Elements

- hospital-like indoor environment
- service corridors
- room-like partitions
- mobile service robot
- inspection robot
- robotic arm station
- medical bed / ward-like areas
- scattered medical supply obstacles



---

## 4. Office Delivery Multi Robot Complex

**Script:** `office_delivery_multi_robot_complex.py`

### Overview
This scene builds a multi-robot office environment for service and delivery tasks.  
It contains several mobile robots, office-style clutter, desks, pathways, and distributed task regions.

### Included Elements

- office-style environment
- desks and work areas
- multiple mobile robots
- package / object drop locations
- indoor corridors
- cluttered obstacles
- delivery points
- navigation lanes


---

## 5. Quadruped Maze And Ramp Challenge

**Script:** `quadruped_maze_and_ramp_challenge.py`

### Overview
This scene is designed for quadruped robot locomotion in challenging terrain.  
It contains maze-like walls, ramps, elevated platforms, and irregular obstacles to test mobility, control robustness, and terrain adaptation.

### Included Elements

- challenging locomotion field
- maze walls
- ramps
- elevated platforms
- uneven obstacle layout
- multiple quadruped robots
- narrow movement passages
- traversal challenge regions


---

## 6. Warehouse Digital Twin Loading Zone Complex

**Script:** `warehouse_digital_twin_loading_zone_complex.py`

### Overview
This scene focuses on a warehouse loading and unloading zone in a digital twin style.  
It combines forklift operation areas, loading points, mobile platforms, manipulators, and transfer zones for end-to-end logistics simulation.

### Included Elements

- digital twin warehouse zone
- loading / unloading platform
- forklift robot
- mobile robot platforms
- robotic arm station
- pallet storage area
- cargo transfer corridor
- conveyor / transfer structure
- inbound and outbound logistics areas


# License

This project is released under the MIT License.
