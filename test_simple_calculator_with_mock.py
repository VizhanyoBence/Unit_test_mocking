import pytest
from simple_calculator import SimpleCaculator
from unittest.mock import Mock

def test_add_with_mock_history_service():
mock_history = Mock()
calc = SimpleCaculator(history_service=mock_history)
result = calc.add()
assert result == 8
mock_history.save_operation.assert_called_once()
mock_history.save_operation.assert_called_with("add", 5, 3, 8)

def test_multiply_with_multiple_mocks():
    

def test_get_history_count_with_mock():
    pass