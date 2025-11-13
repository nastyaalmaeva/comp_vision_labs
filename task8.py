import cv2

def colored_cross():
    # инициализация объекта захвата видео
    video = cv2.VideoCapture(0)

    # ширина и высота кадров видео
    w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # определяем координаты центра кадра
    center_x = w // 2
    center_y = h // 2

    # pассчитываем смещение для выравнивания прямоугольников по центру
    offw = (w - 260) // 2
    offh = (h - 280) // 2

    while True:
        # чтение кадра из видеопотока
        ret, frame = video.read()

        # получаем цвет пикселя в центре кадра
        center = frame[center_y][center_x]

        # Определяем цвет заливки для прямоугольников:
        # Если синий канал больше всех, цвет будет синим
        if (center[0] > center[1]) and (center[0] > center[2]):
            color = [255, 0, 0]
        # Если зеленый канал больше красного, цвет будет зеленым
        elif (center[1] > center[2]):
            color = [0, 255, 0]
        # Иначе цвет будет красным
        else:
            color = [0, 0, 255]

        # Рисуем три прямоугольника с выбранным цветом:
        # Верхний прямоугольник
        cv2.rectangle(frame, (0 + offw, 120 + offh), (260 + offw, 160 + offh), color, -1)
        cv2.rectangle(frame, (110 + offw, 0 + offh), (150 + offw, 120 + offh), color, -1)
        cv2.rectangle(frame, (110 + offw, 160 + offh), (150 + offw, 280 + offh), color, -1)

        cv2.imshow('frame', frame)
        # Если кадр не был успешно получен или нажата клавиша "Esc" (код 27), выходим из цикла
        if cv2.waitKey(1) & 0xFF == 27:
            break
    video.release()
    cv2.destroyAllWindows()
colored_cross()