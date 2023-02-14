"""
Анонимные функции, которые создаются в цикле for,
все ссылаются на один и тот же шаг переменной закрытия,
поэтому все они будут иметь одинаковое значение при выполнении.
Когда вызывается функция execute_handlers и выполняются обработчики,
каждый обработчик возвращает одно и то же значение.
"""


def create_handlers(callback):
    handlers = []
    for step in range(5):
        """
        handlers.append(lambda: callback(step))
        Это можно исправить, используя аргумент по умолчанию для анонимных функций, 
        который создает новую переменную для каждой итерации цикла for.
        """
        handlers.append(lambda x=step: callback(x))
    return handlers


def execute_handlers(handlers):
    for handler in handlers:
        handler()


