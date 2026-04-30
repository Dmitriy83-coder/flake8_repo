## Установка и запуск


### 1. Установка зависимостей
``bash
pip install -r requirements.txt


### 2.Запуск тестов с генерацией Allure результатов


# Сгенерировать отчет
allure generate ./allure-results -o ./allure-report --clean


# Открыть отчет
allure open ./allure-report


### 3. Просмотр Allure отчета
 Вариант 1: Через allure 
       # Сгенерировать отчет
 allure generate ./allure-results -o ./allure-report --clean


  # Открыть отчет
 allure open ./allure-report


  Вариант 2: Через Docker 
 # Сгенерировать и открыть отчет
   docker run --rm -v ${PWD}:/app -p 8080:8080 \
    allure-framework/allure:latest \
     allure open /app/allure-report


# Или только сгенерировать
   docker run --rm -v ${PWD}:/app \
   allure-framework/allure:latest \
   allure generate /app/allure-results -o /app/allure-report --clean

