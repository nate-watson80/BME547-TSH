# BME547-TSH
Nate Watson
February 14, 2019
BME 547 - Medical Software Design

## Contents:

  1. read_TSH.py - Main module. Contains modules to import data, sort into
  dictionaries, determine a diagnosis, and output JSON export files.

  2. test_read_TSH.py - Testing for the diagnosis algorithm.

  3. requirement.txt

  4. test_data.txt - Test data used during development.

  5. output_files - Output patient JSON files. Files are sorted in the format
  of firstname-lastname.JSON.

  6. docs - Sphinx generated documentation.

  7. .travis.yml - Travis continuous integration.

## Usage:

To read in a particular file, edit the main() module to have load_data() load
the text file of interest. 

## Description:

This program is designed to import raw patient data for the diagnosis of
hypothyroidism or hyperthyroidism. The clinical gold standard for diagnosing
these conditions is TSH measurement. Patients that presented with one TSH
readings under 1.0 mU/L were determined to have hyperthyroidism.
Patients that presented with one TSH measurement above 4.0 mU/L were
determined to have hypothyroidism.

## Modules:

1. main() - Main code loop. Main calls the appropriate modules in the correct
order to process and sort the data. The following modules were called in this
order.

2. load_data() - Module to open up the .txt file and return lists containing
the key data of interest: patient name, age, gender, and TSH laboratory values.

3. diagnosis() - Algorithm for determining TSH diagnosis.

4. create_dicts() - Algorithm utilized to store each value in patient specific
dictionaries. Patient dictionaries were subsequently stored in a list.

5. output_data() - Module to output the data to JSON files.
