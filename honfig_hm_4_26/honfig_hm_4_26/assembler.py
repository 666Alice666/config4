# assembler.py

def assembler(input_file, output_binary, output_log):
    # Для хранения бинарных команд и логов
    binary_code = []
    log_lines = []

    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Перебираем каждую строку программы
    for line in lines:
        parts = line.split()
        if len(parts) != 4:
            continue  # Пропускаем строку, если она не имеет правильного количества частей

        # Разбираем команду на 4 части
        command = int(parts[0])  # Код операции (например, 0 - операция взятия остатка)
        operand1 = int(parts[1])  # Первый операнд (число из vector1)
        operand2 = int(parts[2])  # Второй операнд (число из vector2)
        address = int(parts[3])  # Адрес, куда будет записан результат в памяти (индекс vector2)

        # Преобразуем команду в бинарный код
        binary_code.append((command, operand1, operand2, address))
        log_lines.append(f"Команда: A={command}, B={operand1}, C={operand2}, D={address}")

    # Запись бинарного файла
    with open(output_binary, 'wb') as f:
        for command, operand1, operand2, address in binary_code:
            f.write(command.to_bytes(1, byteorder='little'))  # Код команды (1 байт)
            f.write(operand1.to_bytes(1, byteorder='little'))  # Операнд 1 (1 байт)
            f.write(operand2.to_bytes(1, byteorder='little'))  # Операнд 2 (1 байт)
            f.write(address.to_bytes(2, byteorder='little'))  # Адрес (2 байта)

    # Запись логов в файл
    with open(output_log, 'w') as f:
        for log in log_lines:
            f.write(log + '\n')

    # Вывод логов в консоль
    print("Ассемблер лог:")
    for log in log_lines:
        print(log)


if __name__ == "__main__":
    import argparse

    # Создание парсера аргументов
    parser = argparse.ArgumentParser(description="Ассемблер для УВМ.")
    parser.add_argument("--input", required=True, help="Входной текстовый файл")
    parser.add_argument("--output", required=True, help="Выходной бинарный файл")
    parser.add_argument("--log", required=True, help="Выходной лог файл")

    args = parser.parse_args()

    # Вызов функции ассемблера
    assembler(args.input, args.output, args.log)
