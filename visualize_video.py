import cv2
from ultralytics import YOLO


def visualize_detection(video_path="people_walking.mp4"):
    print(f"[VISUAL] Открываю видео: {video_path}...")

    # Загружаем модель
    model = YOLO("yolo11n.pt")

    # Открываем видео для покадрового чтения
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"ОШИБКА: Не удалось открыть видео {video_path}. Проверь путь к файлу.")
        return

    # Получаем FPS видео, чтобы показывать его с нормальной скоростью
    fps = cap.get(cv2.CAP_PROP_FPS)
    # Задержка между кадрами в миллисекундах
    delay = int(1000 / fps) if fps > 0 else 30

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[VISUAL] Видео закончилось.")
            break

        # Запускаем модель на текущем кадре
        # classes=[0] — ищем только людей. conf=0.4 — порог уверенности
        results = model(frame, verbose=False, classes=[0], conf=0.4)

        # Рисуем рамки на кадре
        annotated_frame = results[0].plot()

        # Показываем в окне
        cv2.imshow("YOLO Detection - Press 'q' to quit", annotated_frame)

        # Ждем нужное время. Если нажать 'q', выходим
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            print("[VISUAL] Выход по нажатию 'q'.")
            break

    # Очищаем ресурсы
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Здесь ты можешь поменять имя файла на любое другое
    visualize_detection("people_walking.mp4")