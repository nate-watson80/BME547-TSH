import numpy

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
    iterate = numpy.linspace(0,4*num_patient-4,num_patient)
    iterate = iterate.astype(int)

    # Seperate name and lab_vals into indiviudal data lists
    for i,c in enumerate(iterate):
        name.append(data_list[c])
        lab_vals.append(data_list[c+3])
        #print(c)

    age = []
    gender = []
    for i,c in enumerate(data_list):
        data_list[i] =  data_list[i].rstrip()  # Cut out trailing zeros
        data_list[i] =  data_list[i].lstrip()  # Cut out leading zeros

        if (data_list[i].isdigit() == True):
            age.append(data_list[i])

        if (data_list[i] == "Male" or data_list[i] == "Female"):
            gender.append(data_list[i])
    return name, age, gender, lab_vals

    raw_data.close()

name, age, gender, lab_vals = load_data("test_data.txt")
