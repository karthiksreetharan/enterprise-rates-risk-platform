from datetime import date

from src.risk.historical_scenario import HistoricalScenario


def test_historical_scenario():

    scenario = HistoricalScenario(
        scenario_date=date(2025, 1, 14),
        tenor_shifts={
            "1Y": 0.0003,
            "2Y": 0.0005,
            "3Y": 0.0007,
        },
    )

    assert scenario.scenario_date == date(2025, 1, 14)

    assert len(scenario.tenor_shifts) == 3

    assert scenario.tenor_shifts["1Y"] == 0.0003
    assert scenario.tenor_shifts["2Y"] == 0.0005
    assert scenario.tenor_shifts["3Y"] == 0.0007