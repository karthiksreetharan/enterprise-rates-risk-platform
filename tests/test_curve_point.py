from src.curves.curve_point import CurvePoint


def test_curve_point_creation():

    point = CurvePoint(
        tenor="1Y",
        maturity=1.0,
        zero_rate=0.05,
        discount_factor=0.951229,
    )

    assert point.tenor == "1Y"
    assert point.maturity == 1.0
    assert point.zero_rate == 0.05
    assert point.discount_factor == 0.951229


def test_invalid_maturity():

    try:
        CurvePoint(
            tenor="1Y",
            maturity=0,
            zero_rate=0.05,
            discount_factor=0.95,
        )
        assert False
    except ValueError:
        assert True


def test_invalid_zero_rate():

    try:
        CurvePoint(
            tenor="1Y",
            maturity=1,
            zero_rate=1.2,
            discount_factor=0.95,
        )
        assert False
    except ValueError:
        assert True


def test_invalid_discount_factor():

    try:
        CurvePoint(
            tenor="1Y",
            maturity=1,
            zero_rate=0.05,
            discount_factor=1.2,
        )
        assert False
    except ValueError:
        assert True