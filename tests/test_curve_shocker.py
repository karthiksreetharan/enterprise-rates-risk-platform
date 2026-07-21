from src.risk.curve_shocker import CurveShocker


def test_parallel_shift(sample_curve):

    shocked = CurveShocker().parallel_shift(
        sample_curve,
        0.0001,
    )

    for original, shifted in zip(sample_curve, shocked):

        assert shifted.tenor == original.tenor
        assert shifted.zero_rate == original.zero_rate + 0.0001


def test_bucket_shift(sample_curve):

    shocked = CurveShocker().bucket_shift(
        sample_curve,
        tenor="2Y",
        shift=0.0001,
    )

    for original, shifted in zip(sample_curve, shocked):

        if original.tenor == "2Y":
            assert shifted.zero_rate == original.zero_rate + 0.0001
        else:
            assert shifted.zero_rate == original.zero_rate


def test_multi_bucket_shift(sample_curve):

    shocked = CurveShocker().multi_bucket_shift(
        sample_curve,
        tenor_shifts={
            "1Y": 0.0010,
            "2Y": -0.0005,
        },
    )

    for original, shifted in zip(sample_curve, shocked):

        if original.tenor == "1Y":
            assert shifted.zero_rate == original.zero_rate + 0.0010

        elif original.tenor == "2Y":
            assert shifted.zero_rate == original.zero_rate - 0.0005

        else:
            assert shifted.zero_rate == original.zero_rate