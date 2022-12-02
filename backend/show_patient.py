import csv
def patient_show(parameter):
    #open the csv file and check if the parameter correspond to a row and show the row if it does
    row_patient = []

    with open('patient.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if parameter in row:
                row_patient.append(row)
    return row_patient
