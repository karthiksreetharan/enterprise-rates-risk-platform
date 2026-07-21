from src.pricing.dv01_calculator import DV01Calculator


def test_dv01_calculator(
    sample_swap,
    sample_curve,
):

    result = DV01Calculator().calculate(
        sample_swap,
        sample_curve,
    )

    assert result.trade_id == "IRS001"
    assert result.currency == "USD"
    assert result.present_value > 0
    assert result.dv01 < 0