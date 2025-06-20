import pytest
from src.triangle import Triangle


@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c", "area"),
    [
        (10, 15, 20, 72.6184),
        (10.1, 15.1, 20.1, 73.9775)
    ],
    ids=[
        "integer",
        "float"
    ]
)
def test_triangle_area(side_a, side_b, side_c, area):
    t = Triangle(side_a, side_b, side_c)
    assert t.area == pytest.approx(area, rel=1e-4), \
        f"Area for triangle with sides {side_a}, {side_b} and {side_c} should be approximately {area}"


@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c", "error"),
    [
        (0, 10, 15, "Triangle sides can't be less than 0"),
        (-10, -15, -20, "Triangle sides can't be less than 0"),
        (1, 2, 3, "Triangle doesn't exist")
    ],
    ids=[
        "zero side",
        "negative sides",
        "non-existent triangle"
    ]
)
def test_triangle_area_negative(side_a, side_b, side_c, error):
    with pytest.raises(ValueError, match=error):
        Triangle(side_a, side_b, side_c)
