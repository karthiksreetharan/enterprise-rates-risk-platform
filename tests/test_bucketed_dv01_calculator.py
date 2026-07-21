from src.products.bucketed_dv01_result import BucketedDV01Result
from src.risk.bucketed_dv01_calculator import BucketedDV01Calculator


def test_bucketed_dv01_returns_result(
    sample_swap,
    sample_curve,
):

    result = BucketedDV01Calculator().calculate(
        sample_swap,
        sample_curve,
    )

    assert isinstance(result, BucketedDV01Result)

    assert result.trade_id == "IRS001"
    assert result.currency == "USD"
    assert result.present_value > 0

    assert len(result.bucketed_dv01) == len(sample_curve)