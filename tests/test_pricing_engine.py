from src.pricing.pricing_engine import PricingEngine


def test_pricing_engine_returns_swap_valuation(
    sample_swap,
    sample_curve,
):

    valuation = PricingEngine().value(
        sample_swap,
        sample_curve,
    )

    assert valuation.trade_id == "IRS001"
    assert valuation.currency == "USD"
    assert valuation.present_value > 0