def test_int_float():
    assert 1 == 1.0


class TestNumbers:
    def test_int_foat(self):
        assert 1 == 1.0

    def test_int_not_str(self):
        assert 1 != "1"


def setup_module(module):
    print(f"Setting up module {module.__name__}")


def teardown_module(module):
    print(f"Tearing down module {module.__name__}")


def test_a_function():
    print("Runng test function")


class BaseTest:
    def setup_class(cls):
        print("setting up CLASS {0}".format(cls.__name__))
    def teardown_class(cls):
        print("tearing down CLASS {0}\n".format(cls.__name__))
    def setup_method(self, method):
        print("setting up METHOD {0}".format(method.__name__))
    def teardown_method(self, method):
        print("tearing down METHOD {0}".format(method.__name__))


class TestClass1(BaseTest):
    def test_method_1(self):
        print("RUNNING METHOD 1-1")
    def test_method_2(self):
        print("RUNNING METHOD 1-2")


class TestClass2(BaseTest):
    def test_method_1(self):
        print("RUNNING METHOD 2-1")
    def test_method_2(self):
        print("RUNNING METHOD 2-2")


import pytest
import tempfile
import shutil
import os.path


@pytest.fixture
def temp_dir(request):
    dir = tempfile.mkdtemp()
    print(dir)
    yield dir
    shutil.rmtree(dir)


def test_osfiles(temp_dir):
    os.mkdir(os.path.join(temp_dir, "a"))
    os.mkdir(os.path.join(temp_dir, "b"))
    dir_contents = os.listdir(temp_dir)
    assert len(dir_contents) == 2
    assert "a" in dir_contents
    assert "b" in dir_contents
