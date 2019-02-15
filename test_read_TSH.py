import pytest
import numpy
from read_TSH import diagnosis

raw_data = open("test_data.txt")
data_list = raw_data.readlines()
num_patient = int(len(data_list)/4)
lab_vals = []

# Create a list to iterate through
iterate = numpy.linspace(0, 4*num_patient-4, num_patient)
iterate = iterate.astype(int)

# Seperate name and lab_vals into indiviudal data lists
for i, c in enumerate(iterate):
    lab_vals.append(data_list[c+3])


@pytest.mark.parametrize("patient,expected", [
    (lab_vals, ["normal thyroid function",
                "hyperthyroidism",
                "normal thyroid function",
                "hypothyroidism",
                "hyperthyroidism",
                "normal thyroid function",
                "hypothyroidism",
                "hyperthyroidism",
                "hypothyroidism",
                "hyperthyroidism"]),
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
