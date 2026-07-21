from src.risk.scenario import Scenario
from src.risk.scenario_report import ScenarioReport
from src.risk.scenario_report_engine import ScenarioReportEngine


def test_scenario_report(
    sample_swap,
    sample_curve,
):

    scenarios = [
        Scenario("Base", 0.0),
        Scenario("Up 10bp", 0.001),
        Scenario("Down 10bp", -0.001),
    ]

    report = ScenarioReportEngine().run(
        sample_swap,
        sample_curve,
        scenarios,
    )

    assert isinstance(report, ScenarioReport)

    assert len(report.results) == 3