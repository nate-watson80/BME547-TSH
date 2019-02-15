import pytest
from read_TSH import diagnosis


@pytest.mark.parametrize("patient,expected", [
    (["TSH,3.5,3.6,1.8,2.8,1.9,3.4,3,3.6,3,4"], ["normal thyroid function"]),
    (["TSH,2.7,1.4,2.5,3.1,0.4,1.8,3.1,3,3.8,0.9,2.3"], ["hyperthyroidism"]),
    (["TSH,2.5,1.1,1.3,2.7,1.9,2.6,3.5,1,1.4"], ["normal thyroid function"]),
    (["TSH,6.3,6.7,6.3,7.6,2.1,6.9,7.1,4.1,7.2,3.5,2.9"], ["hypothyroidism"]),
    (["TSH,2.8,2.5,0.7,3.8,2.7,0.2,2.9,1.5,0.8,2.4"], ["hyperthyroidism"]),
    (["TSH,2.4,2.4,3.5,1.1,3,3.9,2,3.7,2.1,3.9"], ["normal thyroid function"]),
    (["TSH,2.7,5.2,4.5,3.3,5.8,2.4,5.3,4.2,2.5,5.2,4"], ["hypothyroidism"]),
    (["TSH,0.6,3.5,0.2,3.7,1.1,0.2,3.5,2.2,1,0.6,3.5"], ["hyperthyroidism"]),
    (["TSH,3.1,4.5,3.5,3.6,5.6,4.8,4.3,5.7,4.2,2.4,5.5"], ["hypothyroidism"]),
    (["TSH,2,2.6,2.4,2.2,1,1.4,0.2,0.5,2,2.3,0.2"], ["hyperthyroidism"]),
    (["2,3,4,3,2,2,3.4", "TSH,  0.8,1.0,1.1,1.0,2,3,3"],
        ["normal thyroid function", "hyperthyroidism"]),
])
def test_diagnosis(patient, expected):
    """ Main testing modules for the diagnosis module.

    Import in diagnosis from the read_TSH file. Standard lab values are
    fed into the algorithm with what the diagnosis should be. This testing
    module should be utilized via the pytest package.

    Args:
        patient (str): Patient TSH values
        expected (str): Diagnosis result expected.

    Returns:
        None

    """

    result, TSH = diagnosis(patient)
    assert result == expected
