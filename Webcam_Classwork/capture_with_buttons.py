import cv2
import os

def main():
    # The argument to VideoCapture is the camera index.
    cap = cv2.VideoCapture(0)

   # Define the directories to save frames
    desktop = os.path.expanduser("~/Desktop")  # adjust as needed
    directory1 = os.path.join(desktop, "images/DF1")
    directory2 = os.path.join(desktop, "images/DF2")


    # Create the directories if they don't exist
    if not os.path.exists(directory1):
        os.makedirs(directory1)
    if not os.path.exists(directory2):
        os.makedirs(directory2)

    frame_counter1 = 0
    frame_counter2 = 0

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame")
            break

        # Draw text on the frame
        cv2.putText(frame, "Press 'c' to capture to DF1", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, "Press 'v' to capture to DF2", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, "Press 'q' to quit", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Webcam Feed', frame)

        key = cv2.waitKey(1)

        # If 'c' is pressed on the keyboard, save the frame in directory1
        if key & 0xFF == ord('c'):
            frame_path = os.path.join(directory1, f'frame_{frame_counter1}.png')
            cv2.imwrite(frame_path, frame)
            print(f'{frame_path} saved!')
            frame_counter1 += 1

        # If 'v' is pressed on the keyboard, save the frame in directory2
        elif key & 0xFF == ord('v'):
            frame_path = os.path.join(directory2, f'frame_{frame_counter2}.png')
            cv2.imwrite(frame_path, frame)
            print(f'{frame_path} saved!')
            frame_counter2 += 1

        # If 'q' is pressed on the keyboard, break the loop and close the application
        elif key & 0xFF == ord('q'):
            break

    # After the loop release the capture
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

