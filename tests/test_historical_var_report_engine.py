import pytest

from src.risk.historical_var_report_engine import (
    HistoricalVaRReportEngine,
)
from src.risk.scenario_result import ScenarioResult


def test_historical_var_report_engine():

    results = [

        ScenarioResult(
            scenario="Day1",
            trade_id="IRS001",
            currency="USD",
            present_value=100.0,
            pnl=-120.0,
        ),

        ScenarioResult(
            scenario="Day2",
            trade_id="IRS001",
            currency="USD",
            present_value=110.0,
            pnl=-30.0,
        ),

        ScenarioResult(
            scenario="Day3",
            trade_id="IRS001",
            currency="USD",
            present_value=125.0,
            pnl=40.0,
        ),

        ScenarioResult(
            scenario="Day4",
            trade_id="IRS001",
            currency="USD",
            present_value=140.0,
            pnl=80.0,
        ),

        ScenarioResult(
            scenario="Day5",
            trade_id="IRS001",
            currency="USD",
            present_value=150.0,
            pnl=150.0,
        ),
    ]

    report = HistoricalVaRReportEngine().run(
        results
    )

    assert report.number_of_scenarios == 5
    assert report.best_gain == 150.0
    assert report.worst_loss == -120.0
    assert report.average_pnl == 24.0
    assert report.median_pnl == 40.0
    assert report.var_95 == 120.0
    assert report.var_99 == 120.0


def test_empty_results():

    with pytest.raises(ValueError):

        HistoricalVaRReportEngine().run([])