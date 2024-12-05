# interpreter.py
import struct

# interpreter.py

import struct


def interpreter(input_binary, output_csv, memory_range):
    memory = [0] * 1024  # Простая память (1024 ячейки)

    with open(input_binary, 'rb') as binary_file:
        commands = binary_file.read()

    i = 0
    while i < len(commands):
        # Чтение 5 байт для каждой команды: 1 байт на код, 1 на operand1, 1 на operand2, 2 на address
        command = struct.unpack('B', commands[i:i + 1])[0]
        operand1 = struct.unpack('B', commands[i + 1:i + 2])[0]
        operand2 = struct.unpack('B', commands[i + 2:i + 3])[0]
        address = struct.unpack('H', commands[i + 3:i + 5])[0]  # Адрес теперь 2 байта (unsigned short)

        print(f"Выполнение команды: A={command}, B={operand1}, C={operand2}, D={address}")

        # Обработка команды
        if command == 217:  # Загрузка константы
            memory[operand1] = operand2  # Запись константы в память по адресу B

        elif command == 178:  # Чтение из памяти
            value = memory[operand2]  # Чтение значения из памяти по адресу C
            memory[operand1] = value  # Запись в память по адресу B

        elif command == 110:  # Запись в память
            value = memory[operand1]  # Чтение значения из регистра по адресу B
            memory[address] = value  # Запись в память по адресу D (без смещения)

        elif command == 131:  # Операция взятия остатка
            value1 = memory[operand1]  # Значение из памяти по адресу B
            value2 = memory[operand2]  # Значение из памяти по адресу C
            if value2 == 0:  # Проверка деления на ноль
                print(f"Ошибка: деление на ноль по адресу {operand2}")
                memory[operand1] = 0
            else:
                memory[operand1] = value1 % value2  # Запись остатка в память по адресу B

        i += 5  # Переход к следующей команде (5 байт на команду)

    # Запись результатов работы программы в CSV
    start, end = memory_range
    with open(output_csv, 'w') as f:
        f.write("Адрес,Значение\n")
        for i in range(start, end + 1):
            f.write(f"{i},{memory[i]}\n")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Интерпретатор для УВМ.")
    parser.add_argument("--input", required=True, help="Входной бинарный файл")
    parser.add_argument("--output", required=True, help="Файл с результатами работы")
    parser.add_argument("--memory", nargs=2, type=int, required=True, help="Диапазон памяти (начало и конец)")
    args = parser.parse_args()
    interpreter(args.input, args.output, tuple(args.memory))
