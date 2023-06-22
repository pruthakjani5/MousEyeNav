# MousEyeNav

MousEyeNav is a Python program that enables hands-free mouse control using facial landmarks and hand gestures. This project utilizes computer vision and automation technologies to provide an alternative method for interacting with computers, particularly beneficial for individuals with motor impairments or disabilities.

## Features

- Control the mouse cursor using facial landmarks and eye movements.
- Perform left-click and right-click actions based on hand gestures.
- Real-time visualization of facial landmarks and mouse control.

## Technologies Used

MousEyeNav utilizes the following libraries and technologies:

- **OpenCV**: OpenCV is a powerful computer vision library for capturing video from the webcam, processing frames, and performing image-related tasks.

- **Mediapipe**: Mediapipe is an open-source framework developed by Google that provides a collection of pre-built models and tools for building multimodal applications. In this project, the FaceMesh model from Mediapipe is used for real-time facial landmark detection.

- **PyAutoGUI**: PyAutoGUI is a cross-platform library that allows the automation of mouse and keyboard control. It is used in MousEyeNav to control the mouse cursor and simulate mouse clicks.

## Installation

To install and run MousEyeNav on your system, follow these steps:

1. Ensure that Python 3.x is installed on your machine.

2. Clone the repository to your local system:
   ```
   git clone https://github.com/pruthakjani5/MousEyeNav.git
   ```

3. Navigate to the project directory:
   ```
   cd MousEyeNav
   ```

4. Install the required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

5. Connect a webcam to your computer.

6. Run the MousEyeNav program:
   ```
   python main.py
   ```

7. The webcam feed will open, and you will see the visualization of facial landmarks and mouse control. Use your facial movements and hand gestures to control the mouse cursor.

8. Press 'Ctrl+C' in the terminal to exit the program.

## Usage

1. Once you have run the program, the webcam feed will open, displaying your face.

2. Make sure your face is well-lit and centred within the frame for accurate facial landmark detection.

3. Look straight ahead to position the mouse cursor in the center of the screen.

4. Move your eyes in the desired direction to move the mouse cursor accordingly.

5. To perform a left-click action, blink your left eye.

6. To perform a right-click action, blink your right eye.
 
7. Users can adjust the eye blinking threshold by checking the log from the terminal to give the best experience as per their eye.
 
8. The program will respond to your facial movements and hand gestures in real-time, controlling the mouse cursor and executing the corresponding actions.

## Contributions

Contributions to MousEyeNav are welcome! If you have any ideas, suggestions, or bug fixes, please submit them as issues or pull requests in the project repository.


## Acknowledgements

This project was made possible by the contributions of various open-source libraries and frameworks, including OpenCV, Mediapipe, and PyAutoGUI. We extend our gratitude to their respective developers and communities.

## Disclaimer

MousEyeNav is an experimental project and should not be used as a primary means of computer interaction. Use it responsibly and be aware of any limitations or potential inaccuracies in facial landmark detection and random clicks due to normal blinking. The project developers are not liable for any damages or consequences arising from using MousEyeNav.

**Note:** This project is intended for educational and demonstration purposes only.
