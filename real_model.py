import json
import sys
from ultralytics import YOLO


def run_real_inference(video_path="car_driving.mp4", model_name="yolo11n.pt",
                       output_file="real_model_output.json"):
    print(f"[MODEL] Запускаю модель {model_name} на файле: {video_path}...")

    model = YOLO(model_name)

    # Ищем только людей (класс 0)
    results = model(video_path, stream=True, verbose=False, classes=[2], conf=0.4)

    all_detections = []
    for frame_result in results:
        boxes = frame_result.boxes
        if boxes is not None:
            for box in boxes:
                cls_id = int(box.cls[0])
                class_name = model.names[cls_id]
                confidence = float(box.conf[0])
                bbox = box.xyxy[0].tolist()

                all_detections.append({
                    "class": class_name,
                    "confidence": round(confidence, 2),
                    "bbox": [round(coord, 1) for coord in bbox]
                })

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_detections, f, indent=4)

    print(f"[MODEL {model_name}] Обработка завершена! Найдено объектов: {len(all_detections)}")
    print(f"[MODEL {model_name}] Результат сохранён в {output_file}\n")
    return output_file


if __name__ == "__main__":
    # Если скрипт запускают из командной строки с аргументами
    if len(sys.argv) > 1:
        model_to_run = sys.argv[1]
        out_file = sys.argv[2] if len(sys.argv) > 2 else "output.json"
        run_real_inference(model_name=model_to_run, output_file=out_file)
    else:
        # Если запускают просто так (без аргументов) — запускаем nano
        run_real_inference()