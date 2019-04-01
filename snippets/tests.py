from unittest import TestCase


def myfunc():
    return 3

class Foo:
    def mymeth(self):
        return 3

foo = Foo()

def bar():
    return foo.mymeth()

# Create your tests here.
from unittest.mock import patch

class MyTest(TestCase):

    def test_t(self):
        import os
        print(os.getcwd())

    @patch('tests.foo.mymeth')
    def test_this(self, p):
        print(dir(p))
