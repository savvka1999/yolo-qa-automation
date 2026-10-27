import csv


def test_metric_classes():
    # 1. Читаем эталон
    gt_objects = []
    with open("ground_truth.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            gt_objects.append(row["object"])

    # 2. Читаем предсказания
    pred_objects = []
    with open("predictions.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            pred_objects.append(row["object"])

    # 3. Ищем ошибки (сравниваем по индексу, так как id совпадают)
    errors = []

    for i in range(len(pred_objects)):
        if gt_objects[i] != pred_objects[i]:
            errors.append(f"Объект {i + 1}: ожидали '{gt_objects[i]}', а модель нашла '{pred_objects[i]}'")

    # Выводим ошибки, если они есть
    if errors:
        print("\n[ВНИМАНИЕ] Обнаружены ошибки классификации:")
        for err in errors:
            print(f" - {err}")

    # 4. Проверяем, что ошибок нет
    assert len(errors) == 0, f"ОШИБКА: Модель неправильно определила классы! Найдено ошибок: {len(errors)}"