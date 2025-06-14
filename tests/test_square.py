import pytest
from src.square import Square


@pytest.mark.parametrize(
    "side_type",
    [
        "integer",
        "float"
    ]
)
def test_rectangle_area(get_square_side, side_type):
    side_a, area = get_square_side(side_type=side_type)

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
