import pytest
from src.circle import Circle


@pytest.mark.parametrize(
    "radius_type",
    [
        "integer",
        "float"
    ]
)
def test_circle_area(get_circle_radius, radius_type):
    radius, area = get_circle_radius(radius_type=radius_type)

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
