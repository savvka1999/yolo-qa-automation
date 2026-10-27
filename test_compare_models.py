import subprocess
import json
import sys
from test_iou_math import calculate_iou


def test_compare_all_boxes():
    video = "car_driving.mp4"
    nano_json = "nano_output.json"
    small_json = "small_output.json"

    print("\n[СРАВНЕНИЕ] Запускаю легкую модель (yolo11n)...")
    subprocess.run([sys.executable, "real_model.py", "yolo11n.pt", nano_json, video], check=True)

    print("\n[СРАВНЕНИЕ] Запускаю тяжелую модель (yolo11s)...")
    subprocess.run([sys.executable, "real_model.py", "yolo11s.pt", small_json, video], check=True)

    with open(nano_json, "r", encoding="utf-8") as f:
        nano_dets = json.load(f)
    with open(small_json, "r", encoding="utf-8") as f:
        small_dets = json.load(f)

    if not nano_dets or not small_dets:
        print("Одна из моделей ничего не нашла.")
        return

    # Считаем TP/FP/FN
    matched_nano = set()
    matched_small = set()
    tp = 0

    for i, n_det in enumerate(nano_dets):
        best_iou = 0
        best_j = -1
        for j, s_det in enumerate(small_dets):
            if j in matched_small:
                continue
            iou = calculate_iou(n_det["bbox"], s_det["bbox"])
            if iou > best_iou:
                best_iou = iou
                best_j = j

        if best_iou > 0.5 and best_j != -1:
            tp += 1
            matched_nano.add(i)
            matched_small.add(best_j)

    fp = len(nano_dets) - tp
    fn = len(small_dets) - tp

    # --- СЧИТАЕМ МЕТРИКИ ---
    precision = tp / len(nano_dets) if len(nano_dets) > 0 else 0
    # Recall: какую долю от всех объектов тяжелой модели нашла легкая?
    recall = tp / len(small_dets) if len(small_dets) > 0 else 0

    print(f"\n[РЕЗУЛЬТАТ] TP: {tp}, FP: {fp}, FN: {fn}")
    print(f"[РЕЗУЛЬТАТ] Precision (Точность): {precision:.2%}")
    print(f"[РЕЗУЛЬТАТ] Recall (Полнота): {recall:.2%}")

    # --- ПРОВЕРКИ ---
    # 1. Точность не должна падать ниже 70%
    assert precision > 0.7, f"ОШИБКА: Низкая точность! Precision = {precision:.2%}"

    # 2. Полнота не должна падать ниже 50% (иначе модель пропускает половину машин)
    assert recall > 0.5, f"ОШИБКА: Низкая полнота! Recall = {recall:.2%}. Легкая модель слишком много пропускает!"


if __name__ == "__main__":
    test_compare_all_boxes()