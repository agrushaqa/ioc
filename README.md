Домашнее задание

Реализация IoC контейнера
Цель:

Цель: Реализовать IoC контейнер, устойчивый к изменению требований.
В результате выполнения домашнего задания Вы получите IoC, который можно будет использовать в своих проектах.

Описание/Пошаговая инструкция выполнения домашнего задания:

В игре Космичекий бой есть набор операций над игровыми объектами: движение по прямой, поворот, выстрел. При этом содержание этих команд может отличаться для разных игр, в зависимости от того, какие правила игры были выбраны пользователями. Например, пользователи могут ограничить запас ход каждого корабля некоторым количеством топлива, а другой игре запретить поворачиваться кораблям по часовой стрелке и т.д.
IoC может помочь в этом случае, скрыв детали в стратегии разрешения зависимости.
Например,
IoC.Resolve("двигаться прямо", obj);
Возвращает команду, которая чаще всего является макрокомандой и осуществляет один шаг движения по прямой.
Реализовать IoC контейнер, который:

    Разрешает зависимости с помощью метода, со следующей сигнатурой:
    T IoC.Resolve(string key, params object[] args);
    Регистрация зависимостей также происходит с помощью метода Resolve
    IoC.Resolve("IoC.Register", "aaa", (args) => new A()).Execute();
    Зависимости можно регистрировать в разных "скоупах"
    IoC.Resolve("Scopes.New", "scopeId").Execute();
    IoC.Resolve("Scopes.Current", "scopeId").Exceute();
    Указание: Для работы со скоупами используйте ThreadLocal контейнер.


Критерии оценки:

    Интерфейс IoC устойчив к изменению требований. Оценка: 0 - 3 балла (0 - совсем не устойчив, 3 - преподаватель не смог построить ни одного контрпримера)
    IoC предоставляет ровно один метод для всех операций. 1 балл
    IoC предоставляет работу со скоупами для предотвращения сильной связности. 2 балла.
    Реализованы модульные тесты. 2 балла
    Реализованы многопоточные тесты. 2 балла
    Максимальная оценка 10 баллов.
    Задание принято, если будет набрано не менее 7 баллов.

# requirements.txt
## create
pip freeze > requirements.txt
## use
pip install -r requirements.txt

# code style
## isort
python -m pip install isort
### run 
isort .
## mypy
python -m pip install mypy
### run 
mypy .
## flake8
python -m pip install flake8
### run
flake8 --exclude venv,docs
## code coverage
pip install coverage
### run
coverage run C:\Users\agrusha\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\behave\__main__.py
в файле .coveragerc нужно указать исходники

# Pytest - Run Tests in Parallel
## install
```pip install pytest-xdist```

also:
https://pypi.org/project/pytest-parallel/
## run
```pytest -n 2 test_common.py```


