from src.curves.interpolation import linear_interpolate


def test_linear_interpolation():

    value = linear_interpolate(
        2,
        1,
        10,
        3,
        20,
    )

    assert value == 15


def test_exact_left():

    assert (
        linear_interpolate(
            1,
            1,
            10,
            3,
            20,
        )
        == 10
    )


def test_exact_right():

    assert (
        linear_interpolate(
            3,
            1,
            10,
            3,
            20,
        )
        == 20
    )


def test_invalid_interval():

    try:

        linear_interpolate(
            2,
            3,
            10,
            1,
            20,
        )

        assert False

    except ValueError:

        assert True