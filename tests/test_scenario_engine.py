from src.risk.scenario import Scenario
from src.risk.scenario_engine import ScenarioEngine


def test_parallel_up_scenario(
    sample_swap,
    sample_curve,
):

    scenario = Scenario(
        name="Parallel +10bp",
        parallel_shift=0.001,
    )

    result = ScenarioEngine().run(
        sample_swap,
        sample_curve,
        scenario,
    )

    assert result.trade_id == "IRS001"

    assert result.currency == "USD"

    assert result.scenario == "Parallel +10bp"

    assert result.present_value > 0

    assert result.pnl != 0