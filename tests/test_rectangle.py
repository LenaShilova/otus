import pytest
from src.rectangle import Rectangle


@pytest.mark.parametrize(
    "sides_type",
    [
        "integer",
        "float"
    ]
)
def test_rectangle_area(get_rectangle_sides, sides_type):
    side_a, side_b, area = get_rectangle_sides(sides_type=sides_type)

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
