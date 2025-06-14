import pytest
from src.square import Square


@pytest.mark.parametrize(
    ("side_a", "area"),
    [
        (2, 4),
        (2.1, 4.41)
    ],
    ids=[
        "integer",
        "float"
    ]
)
def test_rectangle_area(side_a, area):
    s = Square(side_a)
    assert s.area == area, f"Area for square with side {side_a} should be {area}"


@pytest.mark.parametrize(
    ("side_a",),
    [
        (0,),
        (-2,)
    ],
    ids=[
        "zero side",
        "negative sides"
    ]
)
def test_rectangle_area_negative(side_a):
    with pytest.raises(ValueError):
        Square(side_a)
