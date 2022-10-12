import pytest
import main

FIXTURES = [
    ('Новая папка', 201),
    ('Новая папка', 409),
    (None, 400)
]


@pytest.mark.parametrize("folder, exp_result", FIXTURES)
def test_add_folder(folder, exp_result):
    result = main.add_folder(folder)
    assert exp_result == result
