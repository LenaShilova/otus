import pytest


@pytest.fixture()
def get_rectangle_sides():

    def _wrapper(sides_type: str):
        if sides_type == "integer":
            return 2, 4, 8
        if sides_type == "float":
            return 2.1, 4.1, 8.61

        raise ValueError("Invalid sides type: float or integer")

    yield _wrapper


@pytest.fixture()
def get_circle_radius():

    def _wrapper(radius_type: str):
        if radius_type == "integer":
            return 2, 12.56
        if radius_type == "float":
            return 2.1, 13.8474

        raise ValueError("Invalid radius type: float or integer")

    yield _wrapper

@pytest.fixture()
def get_square_side():

    def _wrapper(side_type: str):
        if side_type == "integer":
            return 2, 4
        if side_type == "float":
            return 2.1, 4.41

        raise ValueError("Invalid radius type: float or integer")

    yield _wrapper

@pytest.fixture()
def get_triangle_sides():

    def _wrapper(sides_type: str):
        if sides_type == "integer":
            return 10, 15, 20, 72.6184
        if sides_type == "float":
            return 10.1, 15.1, 20.1, 73.9775

        raise ValueError("Invalid radius type: float or integer")

    yield _wrapper
