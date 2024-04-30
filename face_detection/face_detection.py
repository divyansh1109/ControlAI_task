import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_faces_img(image):

    image = cv2.resize(image, (450, 450))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=9, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return image


def detect_faces_vid(video_path):

    cap = cv2.VideoCapture(video_path)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, (450, 450))
        faces_detected_frame = detect_faces_img(frame)
        cv2.imshow('Detected Faces', faces_detected_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def main():

    input_path = 'img_3.jpeg'
    if input_path.endswith('.jpg') or input_path.endswith('.jpeg') or input_path.endswith('.png'):
        image = cv2.imread(input_path)
        faces_detected_image = detect_faces_img(image)
        cv2.imshow('Detected Faces', faces_detected_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif input_path.endswith('.mp4') or input_path.endswith('.avi') or input_path.endswith('.mov'):
        detect_faces_vid(input_path)

if __name__ == "__main__":
    main()
