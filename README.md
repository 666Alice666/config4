# config4
<h1 align="center">Домашняя работа №1 - Разработать ассемблер и интерпретатор для учебной виртуальной машины</a> 
<h3 align="center">Постановка задачи</h3>
  
Разработать ассемблер и интерпретатор для учебной виртуальной машины
(УВМ). Система команд УВМ представлена далее.

Для ассемблера необходимо разработать читаемое представление команд
УВМ. Ассемблер принимает на вход файл с текстом исходной программы, путь к
которой задается из командной строки. Результатом работы ассемблера является
бинарный файл в виде последовательности байт, путь к которому задается из
командной строки. Дополнительный ключ командной строки задает путь к файлулогу, в котором хранятся ассемблированные инструкции в духе списков
“ключ=значение”, как в приведенных далее тестах.

Интерпретатор принимает на вход бинарный файл, выполняет команды УВМ
и сохраняет в файле-результате значения из диапазона памяти УВМ. Диапазон
также указывается из командной строки.

Форматом для файла-лога и файла-результата является csv.

Необходимо реализовать приведенные тесты для всех команд, а также
написать и отладить тестовую программу.

![image](https://github.com/user-attachments/assets/0a35f57f-32b1-4706-b160-6c1b8631675d)

![image](https://github.com/user-attachments/assets/ffd72ac9-0b69-4b8c-ae55-d3e8d01a0ffd)

![image](https://github.com/user-attachments/assets/0cb93d17-a6fb-4a8d-82d3-313a599bec86)

### Тестовая программа

Выполнить поэлементно операцию взятие остатка над двумя векторами
длины 5. Результат записать во второй вектор.



### Запуск программы
```bash
cd config\honfig_hm_4_26\honfig_hm_4_26
.venv\Scripts\activate
python assembler.py --input test_program.txt --output program.bin --log output_log.txt
python interpreter.py --input program.bin --output memory_output.csv --memory 0 15
```


### Скрины работы программы
- Файл ``test_program.txt``
  
![image](https://github.com/user-attachments/assets/5cb9d0b3-e7b9-4158-99d7-e1cab1d4bdf6)



- Файл ``memory_output.csv``

![image](https://github.com/user-attachments/assets/bd2d490a-3ac1-4efb-b120-ebef25af9dbf)





### Результаты тестов

![image](https://github.com/user-attachments/assets/0b9deea7-0f8e-4e4a-9a9f-9cd0c7c11b27)



### Логи

![image](https://github.com/user-attachments/assets/fe2d94d9-964c-4b6b-8577-be4b87d7f722)

