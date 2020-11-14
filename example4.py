from abc import ABCMeta, abstractmethod


class Example4(metaclass=ABCMeta):
    @abstractmethod
    def one_abstract_method():
        ...

class TestExample4(Example4):

    def test():
        print('only a test')

    def one_abstract_method():
        print('one abstract method')

test_example_4 = TestExample4
test_example_4.test()
test_example_4.one_abstract_method()
