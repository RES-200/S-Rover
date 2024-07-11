#  S-Rover (सरोवर) - Subterranean Rover 🤖

## 🚀 Overview

Explore the "S-Rover (सरोवर)" project – a fusion of computer vision, image processing, and Google Cloud Platform integration. This collaborative effort by our fantastic team results in captivating color maps generated from video frames. S-Rover (Sarovar) integrates cutting-edge sensors and navigation algorithms to autonomously explore and map unknown terrains. By capturing sequential images and stitching them in real-time, S-rover offers a versatile solution for enhanced exploration in inaccessible or hazardous environments.

## ✨ Features

- *Dynamic Source Handling:* Intelligently switches between live streams and local video files.
- *Frame Extravaganza:* Captures frames at regular intervals for further processing.
- *Circular Magic:* Utilizes OpenCV wizardry to extract annular strips from images.
- *Color Symphony:* Creates lively color maps using various OpenCV techniques.
- *Google Cloud Platform:* Seamlessly uploads processed files to designated Google Drive folders.

## 🛠 Usage

### Prerequisites

```
- Python 3.x
- OpenCV (pip install opencv-python)
- Google API Python Client (pip install google-api-python-client)
```

### Setup

1. *Clone the repository:*

   ```
   git clone https://github.com/RES-200/s-rover.git
   cd s-rover
   ```
   
2. *Install dependencies:*

```
pip install -r requirements.txt
Update service_account.json:
```

3. *Replace the placeholder service_account.json with your Google Drive API credentials.*

### 🧑🏻‍💻 Running the Code - 
```
python main_script.py
📁 File Structure
arduino
📦 s-rover
 ┣ 📂 Landing Page
 ┃ ┣ ... (Image_Processing)
 ┣ 📜 Aurdino_control
 ┗ 📜 service_account.json
📜 readme.md
📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

```
![image](https://github.com/RES-200/S-Rover/assets/110082422/d7bc1a14-d69a-4c87-846d-7696b8afa751)

## 🤔 Research Survey -

1. OpenROV: Open-source underwater drone with cameras and sonar for cost-effective underwater mapping. (existing)

2. ANYmal: Quadrupedal robot with LiDAR, cameras, and IMU sensors for agile navigation in disaster zones. (existing)

** **Differentiator**: S-Rover (Sarovar) offers real-time mapping using a simple camera, providing a cost-effective and versatile solution for autonomous terrain mapping.

## 🤝 **Contribution** - 

Feel free to contribute! Check out the Contribution Guidelines for more information.

## 👥 Team - 

1. [ShekharShwetank](https://github.com/ShekharShwetank) - **Team Lead**
2. [harshitsinghcode](https://github.com/harshitsinghcode)
3. [Shashwat Mishra](https://github.com/Shashwatm74)
4. [Utkarsh Rounak](https://github.com/utkxrsx)

**S-Rover** is more than just a project, it addresses the critical need for reliable mapping in environments where human access is limited or unsafe, offering a solution that minimizes reliance on human intervention. 

Happy Coding peeps ✈️!!
