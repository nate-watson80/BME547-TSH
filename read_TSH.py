import numpy
import json


def main():
    """ Main operating code to call modules.

    First, load data from the a .txt data file. For each patient, their lab
    values are passed into a diagnosis module to determine their diagnosis.
    Finally, all of the data is assembled together as a dictionary and outputed
    as a .JSON file to a file on the path ./output_files/Firstname-Lastname

    Args:
        None

    Returns:
        None

    """
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
        input_file (str): Raw data to be analyzed

    Returns:
        name (list of str): Full name of patients
        age (list of str): Age of patients
        gender (list of str): Gender of patients
        lab_vals (list of str): TSH laboratory values

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

    A TSH diagnosis was based upon a number of TSH measurements. Patients that
    presented with one TSH reading under 1.0 mU/L were determined to have
    hyperthyroidism. Patients taht presented with one TSH measurement above
    4.0 mU/L were determined to have hypothyroidism.

    Args:
        lab_vals (list-string): TSH laboratory values

    Returns:
        patient_diagnosis (str):  Diagnosis of "hypothyroidism",
            "hyperthyroidism", or "normal thyroid function."
        TSH_vals (list of list of floats): List of TSH values for each patient.

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
    """ Organize all patient data into patient specific dictionaries.

    Data for each patient was decoded from a .txt input file previously.
    Data is now organized into dictionaries containing their first name, last
    name, age, gender, diagnosis, and TSH laboratory values. These dictionaries
    are then stored in a list called patient_dicts.

    Args:
        name (list of str): Full name of patients
        age (list of str): Age of patients
        gender (list-str): Gender of patients
        diagnosis (str):  Diagnosis of "hypothyroidism","hyperthyroidism",
            or "normal thyroid function."
        TSH_vals (list of list of floats): List of TSH values for each patient.

    Returns:
        patient_dicts (list of dicts): List where each element is a
            patient-specific dictionaries conaining irst name, last
            name, age, gender, diagnosis, and TSH laboratory values.

    """
    # Seperate first name and last name
    first_name = []
    last_name = []
    dict_names = []
    for c in name:
        c = c.replace("\n", "")
        split_name = c.split(" ")
        first_name.append(split_name[0])
        last_name.append(split_name[1])

        dict_names.append(c.replace(" ", "_"))

    # Create the dictionaries
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
    """ Output dictionaries into patient specific .JSON files.

    Patient dictionaries are sorted and sperated into individual .JSON files.
    Files take the name firstname-lastname.JSON and contain all information
    present in their dictionary. Files are added to a directory labelled
    output_files on the path ./output_files/filename.

    Args:
        patient_dicts (list of dicts): List where each element is a
            patient-specific dictionaries conaining irst name, last
            name, age, gender, diagnosis, and TSH laboratory values.

    Returns:
        None

    """
    for c in patient_dicts:
        filename = c.get("First Name") + "-" + c.get("Last Name") + ".json"
        path = "./" + "output_files/" + filename
        out_file = open(path, "w")
        json.dump(c, out_file)
        out_file.close()


if __name__ == "__main__":
    main()
