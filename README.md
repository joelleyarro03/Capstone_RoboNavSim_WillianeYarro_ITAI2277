Badge Block

![WillianeYarro](https://img.shields.io/badge/Author-Willianeyarro-pink)
![Course: ITAI-2277](https://img.shields.io/badge/Course-ITAI%202277-blueviolet)
![Final-Capstone](https://img.shields.io/badge/Capstone-Fall%202025-green)
![RoboNavSim](https://img.shields.io/badge/RoboNavSim-3D%20Navigation%20Simulator-purple)
![Python-Version](https://img.shields.io/badge/Python-3.10%2B-blue)
![AI Robotics-Paths](https://img.shields.io/badge/AI-Robotics-orange)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)


# 🚀 RoboNavSim – 3D Robotic Navigation Simulation

A Capstone Project for ITAI 2277 – Applied AI & Robotics
👤 Author: Williane Yarro
Capstone Project – Fall 2025
Houston Community College (HCC)
 Project Overview

RoboNavSim is a 3D robotic navigation simulation that demonstrates the
use of multiple artificial intelligence techniques for autonomous robotic movement.
Built entirely in Google Colab, this project integrates:

3D environment visualization

Local obstacle-aware navigation

Global A* pathfinding

Reinforcement Learning (Q-learning)

LIDAR-style sensing visualization

Value function & policy interpretation tools

This capstone project highlights the differences between planning-based, rule-based, 
and learning-based AI navigation methods  all using a custom-coded simulator.

🧠 Key Features
Level 1: 3D Environment + Robot

3D grid simulated using matplotlib

Robot represented as a cube

Static 3D obstacles + goal marker

Level 2: Greedy Navigation

Robot moves toward goal using simple distance minimization

Level 3: Sensor-Based Navigation

Robot senses obstacles within a radius

Avoids unsafe moves

Adds Gaussian movement noise

Level 4: A* Global Path Planning

Efficient pathfinding using classical AI

Visual comparison with local navigation

LIDAR-style rays showing sensed obstacles

Level 5: Reinforcement Learning (Q-Learning)

Robot learns optimal policy through experience

Reward shaping:

+100 (goal)

–10 (obstacle)

–5 (boundary)

–1 (time)

ε-greedy exploration

Visualized reward curve

Level 6: Policy & Value Visualization

Heatmap of state-value function

Arrow map illustrating learned policy

Deep interpretation of RL behavior
Project Overview

RoboNavSim is a 3D robotic navigation simulation that showcases the application of
various artificial intelligence techniques for autonomous robotic movement. 
Developed entirely within Google Colab, this project encompasses:

3D environment visualization

Local obstacle-aware navigation

Global A* pathfinding

Reinforcement Learning (Q-learning)

LIDAR-style sensing visualization

Value function & policy interpretation tools

🗂 Project Structure
RoboNavSim/
│── RoboNavSim.ipynb         # Main Colab notebook with all levels
│── README.md                # Project documentation
│── LICENSE                  # MIT License
└── figures/                 

How to Execute the Project
Recommended: Google Colab (No Installation Required)

Access RoboNavSim.ipynb in Google Colab

Select Runtime → Run all

Explore:

3D robotic movement

A* pathfinding

Q-learning training

Sensor + LIDAR visualization

Value/Policy interpretation graphs

Run Locally

Prerequisites:pip install numpy matplotlib
| Method          | Uses Map? | Learns? | Strength               | Weakness       |
| --------------- | --------- | ------- | ---------------------- | -------------- |
| Greedy          | ❌ No     | ❌ No  | Simple & fast          | Gets stuck     |
| Sensor-Based    | ❌ No     | ❌ No  | Avoids obstacles       | Not optimal    |
| A* Planner      | ✔ Yes     | ❌ No  | Optimal global path    | Needs full map |
| Q-Learning (RL) | ❌ No     | ✔ Yes  | Learns from experience | Training time  |

Results Overview

The robot effectively maneuvers through the 3D environment in various modes.

A* algorithm generates the most efficient path when the map is available.

Q-learning develops a strong navigation strategy even in the absence of a map.

Visualizations of value and policy illustrate the reasoning process of the RL agent.

LIDAR simulation showcases perception based on sensor data.

Contact:
Email: joelleyarro@gmail.com
Repo: https://github.com/joelleyarro03/Capstone_RoboNavSim_WillianeYarro_ITAI2277/
