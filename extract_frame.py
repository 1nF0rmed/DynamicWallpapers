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

extract("C:\\Users\\1nf0rmed\\Downloads\\PROJECT_KILL_IT\\videoplayback.mp4")
