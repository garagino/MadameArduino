import cv2
from random import randrange

video = [r'videos/APERTA A.mp4', r'videos/SIM.mp4', r'videos/NAO.mp4', r'videos/TALVEZ.mp4']


def loop(video):
    cap = cv2.VideoCapture(video)

    cv2.namedWindow('Aperte A', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('Aperte A', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


    while True:
        ret, frame = cap.read()

        if not ret:
            cap = cv2.VideoCapture(video)
            continue

        cv2.imshow('Aperte A', frame)

        if cv2.waitKey(25) & 0xFF == ord('a'):
            cap.release()
            cv2.destroyAllWindows()
            break
    
    return randrange(1, 4)

def play_video(video):

    cap = cv2.VideoCapture(video)

    cv2.namedWindow('Video', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('Video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while True:
        ret, frame = cap.read()

        if not ret:
            cap.release()
            cv2.destroyAllWindows()
            return True
        
        cv2.imshow('Video', frame)
        cv2.waitKey(25)

cond = True
while True:
    try:
        if (cond):
            ale = loop(video[0])
        cond = False
        print(ale)
        cond = play_video(video[ale])

    except KeyboardInterrupt:

        cv2.destroyAllWindows()
        print('Nos vemos na proxima sorte!')
        break
