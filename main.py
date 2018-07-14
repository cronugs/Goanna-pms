#Goanna PMS


def welcome():
    new_open = input('Goanna PMS - (N)ew patient, (O)pen file: ')
    if new_open == 'N':
        new_patient()
    elif new_open == 'O':
        open_patient()
    else:
        print('Enter N to start a new patient file \nPress O to open an existing patient file')
        welcome()

class Patient(self, fname, lname, phone, pnumber):
    first_name = fname
    #last_name = input('Last name: ')
    last_name = last_name
    phone = phone
    pnumber = pnumber

    full_name = first_name + ' ' + last_name

    if new_note == 'Y':
        open_new_patient_file()
        notes = input('{}: '.format(full_name))
        print('file {} has been saved'.format(full_name))
        welcome()
    else:
        touch_empty_file()
        print('An empty patient file has been created for {}'.format(full_name))
        welcome()
    return;

new_note = input('Would you like to begin documenting this case now? [Y/n]: ')


def open_new_patient_file():
    return;

def touch_empty_file():
    return;

def set_name(fname_string, lname_string):
    first_name = fname_string
    last_name = lname_string
    return '{} {}'.format(first_name, last_name);

def add_diagnosis(diag):
    diagnosis = diag
    return;

def patient_file();

welcome()
