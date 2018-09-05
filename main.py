#Goanna PMS

from classes.patient import Patient
from classes.patientFile import PatientFile
import datetime
import sys

pat_dict = {'None':'None'}

def main_menu():

    ##The main menu

    print('\nGoanna PMS - Main menu \n')
    print('(N)ew patient')
    print('(S)earch and open patient file')
    print('(Q)uit \n')

    greeting = input('What would you like to do?: ')
    if greeting.lower() in ['n', 'new']:
        temp_pat = Patient()
        PatientFile.create_new_file(
            temp_pat.getPatnum(),
            temp_pat.getFullName(),
            temp_pat.getFName(),
            temp_pat.getLName(),
            temp_pat.getPatRecord()
            )
        temp_pat.add_record_library()
        main_menu()
    elif greeting.lower() in ['s', 'search']:
        search_and_open()
    elif greeting.lower() in ['q', 'quit']:
        sys.exit()
        #main_menu()
    else:
        print('Enter N to start a new patient file \nPress O to open an existing patient file')
        main_menu()

def search_and_open():
    ## Takes a string and returns all matching lines from a file of patient names and numbers
    ## The lines are returned as numbered options
    entry = []
    substr = input('Enter patient names or number: ')

    try:
        with open ('patient_list.txt', 'rt') as in_file:
            for linenum, line in enumerate(in_file):
                if line.lower().find(substr) != -1:
                    entry.append((linenum, line.rstrip('\n')))
                    for linenum, line in entry:
                        print("\nFile ", linenum, ": ", line, sep='')
                        #print(entry)
    except FileNotFoundError:
        print("Log file not found.")

    result_dict = {k:v for k,v in entry} #Convert list of tuples into key:value pairs
    #print(result_dict)
    open_file = int(input('\nWhich file would you like to open?: '))

    match = result_dict.get(open_file)
    #print(match)
    clean = match.replace(" ", "")
    with open(clean + '.txt', 'r') as myfile:
        data = myfile.read()
    print('\n' + data)
    PatientFile.open_existing_file(clean)
    main_menu()


main_menu()
