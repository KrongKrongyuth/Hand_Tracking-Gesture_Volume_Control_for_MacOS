# Hand Tracking: Gesture Volume Control for MacOS

This project utilizes `cvzone.HandTrackingModule` to control the volume on MacOS using hand gestures. You can run this code and use your index finger and thumb to adjust the volume.

## Requirements
- Python 3
- OpenCV
- cvzone (install using `pip install cvzone`)

## Usage
1. Ensure you have a webcam connected to your MacOS system.
2. Run the Python script provided (`hand_tracking_volume_control.py`).
3. Use your index finger and thumb to control the volume:
   - Move your hand closer together to decrease the volume.
   - Move your hand further apart to increase the volume.

## Implementation Details
- The code utilizes `cv2.VideoCapture` to capture the webcam feed.
- `cvzone.HandDetector` is used to detect and track hands in the video feed.
- Hand gestures are interpreted to control the volume:
  - For a single hand:
    - Pinch your index finger and thumb together to decrease the volume.
    - Spread your index finger and thumb apart to increase the volume.
  - For two hands (optional, not fully implemented):
    - You can add custom functionality for controlling volume using two hands.

## Notes
- You may need to adjust the `detectionCon` parameter in `HandDetector` instantiation based on your environment.
- Ensure that the `osascript` command works on your MacOS system for volume control.

## Troubleshooting
- If you encounter issues with hand detection, try adjusting the `detectionCon` parameter in the code.
- Make sure your webcam is properly connected and accessible by the script.

Feel free to contribute to this project and extend its functionality further!
