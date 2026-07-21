from datetime import date

from src.risk.historical_scenario import HistoricalScenario
from src.risk.historical_var_engine import HistoricalVaREngine


def test_historical_var_engine(
    sample_swap,
    sample_curve,
):

    scenarios = [

        HistoricalScenario(
            scenario_date=date(2025, 1, 14),
            tenor_shifts={
                "1Y": 0.0003,
                "2Y": 0.0005,
                "3Y": 0.0007,
            },
        ),

        HistoricalScenario(
            scenario_date=date(2025, 1, 15),
            tenor_shifts={
                "1Y": -0.0002,
                "2Y": -0.0004,
                "3Y": -0.0005,
            },
        ),
    ]

    results = HistoricalVaREngine().run(
        sample_swap,
        sample_curve,
        scenarios,
    )

    assert len(results) == 2

    assert results[0].scenario == "2025-01-14"
    assert results[1].scenario == "2025-01-15"

    assert results[0].trade_id == "IRS001"
    assert results[1].trade_id == "IRS001"

    assert isinstance(results[0].present_value, float)
    assert isinstance(results[0].pnl, float)