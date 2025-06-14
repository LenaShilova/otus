import pytest
from src.circle import Circle
from src.rectangle import Rectangle


@pytest.mark.parametrize(
    "first_figure, second_figure",
    [
        (Circle(2), Rectangle(2, 4)),
        (Circle(4), Circle(5)),
        (Rectangle(4, 5), Rectangle(6, 7))
    ],
    ids=[
        "area circle + area rectangle",
        "area circle + area circle",
        "area rectangle + area rectangle"
    ]
)
def test_add_area_positive(first_figure, second_figure):
    assert first_figure.add_area(second_figure) == first_figure.area + second_figure.area


@pytest.mark.parametrize(
    "invalid_value",
    [
        "abc",
        123
    ],
    ids=[
        "add area with figure 'abc'",
        "add area with figure '123'",
    ]
)
def test_add_area_negative(invalid_value):
    with pytest.raises(ValueError, match="Should be a Figure"):
        Circle(2).add_area(invalid_value)
