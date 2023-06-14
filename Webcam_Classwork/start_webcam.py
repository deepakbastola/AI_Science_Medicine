import cv2

def main():
    # The argument to VideoCapture is the camera index. 
    # Usually 0 will be the built-in webcam, and additional USB cameras will 
    # start at index 1. You may need to change this depending on your setup.
    cap = cv2.VideoCapture(0) 

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame")
            break

        # Display the resulting frame
        cv2.imshow('Webcam Feed', frame)

        # If 'q' is pressed on the keyboard, break the loop and close the application
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the capture
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
