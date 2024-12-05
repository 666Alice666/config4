# test_program.py

from assembler import assembler
from interpreter import interpreter


def test_vector_mod():
    # Путь к файлам
    input_program = "test_program.txt"
    output_binary = "output.bin"
    output_log = "output_log.csv"
    output_csv = "memory_output.csv"
    memory = [0, 1023]

    assembler(input_program, output_binary, output_log)
    interpreter(output_binary, output_csv, memory)


if __name__ == "__main__":
    test_vector_mod()
