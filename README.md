# Drone Headcount App

This project processes drone video footage to perform head counting, applying gender classification and age filtering, while also categorizing other objects found in the video. The application outputs the counts of each category detected in the video.

## Project Structure

```
drone-headcount-app
├── src
│   ├── main.py            # Entry point of the application
│   ├── detection.py       # Object detection functions using YOLO
│   ├── classification.py   # Functions for classifying age and gender
│   └── utils.py           # Utility functions for image processing and video management
├── requirements.txt       # List of dependencies
└── README.md              # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd drone-headcount-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Place your drone video file in the project directory.
2. Update the video path in `src/main.py` to point to your video file.
3. Run the application:
   ```
   python src/main.py
   ```

4. The output video will be saved as `output_demo.avi` in the project directory, and a summary of counts will be printed in the console.

## Functionality

- **Object Detection**: The application uses a pre-trained YOLO model to detect objects in each frame of the video.
- **Age and Gender Classification**: Detected faces are classified into categories: male kid, female kid, male adult, and female adult.
- **Counting**: The application maintains a count of each detected category and outputs the final summary after processing the video.

## Dependencies

- OpenCV
- YOLO (Ultralytics)
- DeepFace
- NumPy
- Collections

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.