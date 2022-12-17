# import allure
import pytest
import common
import test_scope

class TestCommon:
    def test_resolve(self, capsys):
        list_functions = {}
        list_functions["TestScope.current"] = test_scope.TestScope.current
        ioc = common.IoC(list_functions)
        ioc.resolve("TestScope.current", test_scope.TestScope, "34", 88).execute()
        captured = capsys.readouterr()
        assert captured.out == "34\n88\n"

    def test_call_method_with_class_in_attrib(self, capsys):
        test_scope.TestScope.current(test_scope.TestScope, "34", 88)
        captured = capsys.readouterr()
        assert captured.out == "34\n88\n"

    def test_ioc_register(self, capsys):
        list_functions = {}
        ioc = common.IoC(list_functions)
        a = test_scope.TestScope()
        ioc.resolve(key="IoC.register", registered_name="MyScope",
                    called_method=a.current).execute()
        ioc.resolve("MyScope", "34", 88).execute()
        captured = capsys.readouterr()
        assert captured.out == "34\n88\n"