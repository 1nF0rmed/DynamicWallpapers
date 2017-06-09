import cv2

def extract(path):
    cap = cv2.VideoCapture(path)
    success, image = cap.read()
    count = 0
    success = True

    while success:
        success, image = cap.read()
        print("Reading New Frame Status: ", success)
        cv2.imwrite("img\\frame%d.jpg" % count, image)
        count += 1

extract("Path to the video file")
