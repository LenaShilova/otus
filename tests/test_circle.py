import pytest
from src.circle import Circle


@pytest.mark.parametrize(
    ("radius", "area"),
    [
        (2, 12.56),
        (2.1, 13.8474)
    ],
    ids=[
        "integer",
        "float"
    ]
)
def test_circle_area(radius, area):
    c = Circle(radius)
    assert c.area == area, f"Area for circle with radius {radius} should be {area}"


@pytest.mark.parametrize(
    ("radius",),
    [
        (0,),
        (-2,)
    ],
    ids=[
        "zero radius",
        "negative radius"
    ]
)
def test_circle_area_negative(radius):
    with pytest.raises(ValueError):
        Circle(radius)
