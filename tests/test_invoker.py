import pytest
from invoker import Invoker
from commands.basic import AddCommand

def test_register_and_execute_command():
    invoker = Invoker()
    invoker.register_command("add", AddCommand())

    result = invoker.execute_command("add", 3, 7)
    assert result == 10

def test_execute_unregistered_command():
    invoker = Invoker()

    with pytest.raises(KeyError):
        invoker.execute_command("subtract", 3, 2)
