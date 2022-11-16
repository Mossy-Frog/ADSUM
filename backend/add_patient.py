
def patient_add(name,age,weight,symptoms):
    import csv
    from csv import writer
    #open csv file to write in the next row the variables
    with open('patient.csv', 'a') as f_object:
 

        writer_object = writer(f_object)
 
        writer_object.writerow([name,age,weight,symptoms])    # Pass the list as an argument into the writerow()
 

        f_object.close()     # Close the file object
    return "Patient created"