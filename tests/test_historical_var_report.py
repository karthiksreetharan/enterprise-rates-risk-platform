from src.risk.historical_var_report import HistoricalVaRReport


def test_historical_var_report():

    report = HistoricalVaRReport(
        number_of_scenarios=250,
        best_gain=1250.0,
        worst_loss=-980.0,
        average_pnl=15.4,
        median_pnl=10.2,
        var_95=425.0,
        var_99=812.0,
    )

    assert report.number_of_scenarios == 250
    assert report.best_gain == 1250.0
    assert report.worst_loss == -980.0
    assert report.average_pnl == 15.4
    assert report.median_pnl == 10.2
    assert report.var_95 == 425.0
    assert report.var_99 == 812.0