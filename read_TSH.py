import numpy
import json


def main():
    name, age, gender, lab_vals = load_data("test_data.txt")
    patient_diagnosis, TSH_vals = diagnosis(lab_vals)
    patient_dicts = create_dicts(
                                name, age, gender,
                                patient_diagnosis, TSH_vals)
    output_data(patient_dicts)


def load_data(input_file):
    """ Import, load, and sort the raw patient data.

    A raw .txt file is loaded into python. The data is expected to have
    the format of patient name, patient age, gender, then, TSH lab values.
    Individual data points are seperated on each line. This method will
    seperate each data line into lists of name, age, gender, and lab values.

    Args:
        input_file (string): Raw data to be analyzed

    Returns:
        name (list): Full name of patients
        age (list): Age of patients
        gender (list): Gender of patients
        lab_vals (list): TSH laboratory values

    """

    # Open data file, read the individual lines
    raw_data = open(input_file)
    data_list = raw_data.readlines()
    num_patient = int(len(data_list)/4)  # Determine number of patients

    name = []
    lab_vals = []
    # Create a list to iterate through
    iterate = numpy.linspace(0, 4*num_patient-4, num_patient)
    iterate = iterate.astype(int)

    # Seperate name and lab_vals into indiviudal data lists
    for i, c in enumerate(iterate):
        name.append(data_list[c])
        lab_vals.append(data_list[c+3])

    age = []
    gender = []
    for i, c in enumerate(data_list):
        data_list[i] = data_list[i].rstrip()  # Cut out trailing zeros
        data_list[i] = data_list[i].lstrip()  # Cut out leading zeros

        if data_list[i].isdigit() is True:
            age.append(data_list[i])

        if (data_list[i] == "Male" or data_list[i] == "Female"):
            gender.append(data_list[i])
    return name, age, gender, lab_vals

    raw_data.close()


def diagnosis(lab_vals):
    """ Load in raw TSH values and return the diagnosis.

    A raw .txt file is loaded into python.

    Args:

    Returns:

    """
    patient_diagnosis = []
    TSH_vals = []
    for i, c in enumerate(lab_vals):
        c = c.replace("\n", "")  # Remove \n
        split = c.split(",")  # Divide up numbers into a list

        # Isolate just the numbers from each patient data:
        TSH = []
        for l in split:
            if (l != "TSH"):
                TSH.append(float(l))
        TSH_vals.append(TSH)

        # Determine patient diagnosis:
        if (max(TSH) > 4.0 and min(TSH) > 1.0):
            patient_diagnosis.append("hypothyroidism")

        if (min(TSH) < 1.0 and max(TSH) < 4.0):
            patient_diagnosis.append("hyperthyroidism")

        if (min(TSH) >= 1.0 and max(TSH) <= 4.0):
            patient_diagnosis.append("normal thyroid function")

    return patient_diagnosis, TSH_vals


def create_dicts(name, age, gender, diagnosis, TSH_vals):
    # Step 1: Seperate first name and last name
    first_name = []
    last_name = []
    dict_names = []
    for c in name:
        c = c.replace("\n", "")
        split_name = c.split(" ")
        first_name.append(split_name[0])
        last_name.append(split_name[1])

        dict_names.append(c.replace(" ", "_"))

    # Step 2: Create the dictionaries
    patient_dicts = []
    for i, c in enumerate(name):

        dictionary = {
                    "First Name": first_name[i],
                    "Last Name": last_name[i],
                    "Age": age[i],
                    "Gender": gender[i],
                    "Diagnosis": diagnosis[i],
                    "TSH results": TSH_vals[i],
        }
        patient_dicts.append(dictionary)

    return patient_dicts


def output_data(patient_dicts):
    for c in patient_dicts:
        filename = c.get("First Name") + "-" + c.get("Last Name") + ".json"
        path = "./" + "output_files/" + filename
        out_file = open(path, "w")
        json.dump(c, out_file)
        out_file.close()


if __name__ == "__main__":
    main()
