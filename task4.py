import cv2

def readIPWriteTOFile():
    video = cv2.VideoCapture(r'C:/Users/nastya/Desktop/video/WIN_20251008_16_41_03_Pro.mp4', cv2.CAP_ANY)
    if not video.isOpened():
        print("Ошибка: Не удалось открыть видеофайл")
        print("Убедитесь, что файл './source/video.mp4' существует")
        return
    ok, vid = video.read()
    if not ok:
        print("Ошибка: Не удалось прочитать видео")
        video.release()
        return

    w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter("C:/Users/nastya/Desktop/video/newvideo.mp4", fourcc, 25, (w, h))

    while (True):
        ok, vid = video.read()

        cv2.imshow('Video', vid)
        video_writer.write(vid)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    video_writer.release()
    cv2.destroyAllWindows()

readIPWriteTOFile()