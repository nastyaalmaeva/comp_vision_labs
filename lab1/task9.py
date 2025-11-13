import cv2

def task9():
    # Указываем IP-адрес и порт сервера, с которого будет идти видеопоток
    ip_address = '10.88.165.226'
    port = '8080'

    # Инициализируем захват видео с заданного URL-адреса
    video = cv2.VideoCapture(f"http://{ip_address}:{port}/video")
    while True:
        # Читаем кадр из видеопотока
        ret, frame = video.read()
        # Если кадр не был успешно получен или нажата клавиша "Esc" (код 27), выходим из цикла
        if not ret or cv2.waitKey(1) & 0xFF == 27:
            break
        cv2.imshow(f'Video stream from {ip_address}:{port}', frame)
    video.release()
    cv2.destroyAllWindows()

task9()