# Этот тест проверяет лог-файл, имитируя твою ручную работу

def test_model_loaded():
    # 1. Открываем файл лога для чтения
    with open("software.log", "r", encoding="utf-8") as file:
        log_content = file.read()

    # 2. Проверяем, что в логе есть строка об успешной загрузке модели
    assert "Model loaded successfully" in log_content, "ОШИБКА: В логах нет записи о загрузке модели!"


def test_low_fps_warning():
    # 1. Читаем лог
    with open("software.log", "r", encoding="utf-8") as file:
        log_content = file.read()

    # 2. Ищем предупреждение о низком FPS
    assert  "Low FPS" in log_content, "ОШИБКА: В логах нет предупреждения о низком FPS"
    print("\n[INFO] Предупреждение о низком FPS найдено! Модель работает медленно.")