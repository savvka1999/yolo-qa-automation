import subprocess
import json
import os
import sys


def test_real_yolo_detection():
    video_file = "test_video.mp4"

    # 1. Проверяем, что видео существует
    assert os.path.exists(video_file), f"ОШИБКА: Файл {video_file} не найден в папке проекта!"

    # 2. Запускаем модель
    print("\n[AUTOQA] Запускаю real_model.py...")
    process = subprocess.run(
        [sys.executable, "real_model.py"],
        capture_output=True,
        text=True,
    encoding="utf-8"
    )

    # 3. Проверяем, что модель не упала
    assert process.returncode == 0, f"ОШИБКА: Модель упала! Логи: {process.stderr}"
    print("[AUTOQA] Модель отработала без ошибок.")

    # 4. Проверяем, что файл с результатами создан
    output_file = "real_model_output.json"
    assert os.path.exists(output_file), f"ОШИБКА: Файл результатов {output_file} не создан!"

    # 5. Читаем и проверяем результаты
    with open(output_file, "r", encoding="utf-8") as f:
        detections = json.load(f)

    print(f"[AUTOQA] Модель нашла объектов: {len(detections)}")
    assert len(detections) > 0, "ОШИБКА: Модель ничего не нашла! (Возможно, видео пустое)"

    classes_found = [d["class"] for d in detections]
    print(f"[AUTOQA] Найденные классы: {set(classes_found)}")

    assert "car" in classes_found or "person" in classes_found, \
        f"ОШИБКА: Модель не нашла ни машин, ни людей. Найдено: {set(classes_found)}"

    print("[AUTOQA] Тест пройден! Модель корректно детектирует объекты.")