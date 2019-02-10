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

    result, TSH = diagnosis(patient)
    assert result == expected
