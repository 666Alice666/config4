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
python interpreter.py --input program.bin --output memory_output.csv --memory 0 1023
```


### Скрины работы программы
- Комманда ``ls``
  
![image](https://github.com/user-attachments/assets/0b6c3c56-b466-4332-8f07-937806bb0c1a)



- Комманда ``cd``

![image](https://github.com/user-attachments/assets/3b5f1243-ac0b-4fe1-a110-9540963df162)



- Комманда ``date``

![image](https://github.com/user-attachments/assets/87253ac6-209f-4662-8815-c070ba416c5c)



- Комманда ``touch``

![image](https://github.com/user-attachments/assets/7db1a20c-5f08-4be6-a01a-e25b7c20a9ef)



- Комманда ``exit``

![image](https://github.com/user-attachments/assets/36ce3e15-3e37-48a8-acae-b7846d66781e)



### Результаты тестов

![image](https://github.com/user-attachments/assets/c6a9cc05-af4b-41f4-8b53-41e93f4de6ac)


### Логи

![image](https://github.com/user-attachments/assets/6dc079c5-2b07-4c63-b8d7-5d75a91b1d04)
