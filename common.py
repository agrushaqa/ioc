import executor


class IoC:
    def __init__(self, list_functions={}):
        self.methods = list_functions
        self.add_method("IoC.register", self.register)

    def add_method(self, name, method):
        self.methods[name] = method

    def resolve(self, key: str, *argv, **kwargs):
        '''
        отдаёт зависимость
        :param key: - название зависимости
        :param args:
        :return:
        '''
        return executor.Executor(self.methods[key], *argv, **kwargs)

    def register(self, registered_name, called_method):
        self.add_method(registered_name, called_method)
