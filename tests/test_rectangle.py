import pytest
from src.rectangle import Rectangle


@pytest.mark.parametrize(
    ("side_a", "side_b", "area"),
    [
        (2, 4, 8),
        (2.1, 4.1, 8.61)
    ],
    ids=[
        "integer",
        "float"
    ]
)
def test_rectangle_area(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.area == area, f"Area for rectangle with sides {side_a} and {side_b} should be {area}"


@pytest.mark.parametrize(
    ("side_a", "side_b"),
    [
        (0, 4),
        (-2, -4)
    ],
    ids=[
        "zero side",
        "negative sides"
    ]
)
def test_rectangle_area_negative(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)
