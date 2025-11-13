import cv2
import time

def video_copy():
    video = cv2.VideoCapture(0)
    ret, frame = video.read()

    w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # устанавливаем кодек для сжатия видео в формате XVID
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    # cоздаем объект для записи видео в файл с параметрами (имя, кодек, fps, разрешение)
    video_writer = cv2.VideoWriter("output_video.mp4", fourcc, 25, (w, h))

    while (True):
        # читаем видео разбивая его на картинки
        ret, frame = video.read()
        # отображаем видео покадрово в окне
        cv2.imshow('video', frame)
        # записываем текущий кадр в выходной видеофайл
        video_writer.write(frame)

        # меняем кадр через 1 милисекунду, после нажатия esc отображение кадров прекращается
        if cv2.waitKey(1) & 0xFF == 27:
            break

    video.release()
    video_writer.release()
    cv2.destroyAllWindows()

    time.sleep(10)

    video_open = cv2.VideoCapture('output_t7.mp4', cv2.CAP_ANY)

    while (True):
        ret, frame = video_open.read()
        if not (ret):
            break

        cv2.imshow('Video', frame)

        # меняем кадр через 1 милисекунду, после нажатия exc(код 27) отображение кадров прекращается
        if cv2.waitKey(1) & 0xFF == 27:
            break

    video_open.release()
    cv2.destroyAllWindows()

video_copy()