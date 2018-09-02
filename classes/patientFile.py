class PatientFile:
    def __init__(self):

    def newFile(self, fname, lname, phone, pernum, patnum):
        fo = open(full_name + ".txt", "a+")
        fo.write(datetime.date + " " + 'full_name \n')

        append = input('Would you like to begin documenting this case now?: Y/n')
        if append == 'N' or 'n':
            fo.close()
            print('File saved and closed')
            main_menu()
        elif append == 'Y' or 'y':
            fo.write(input('Case notes: \n'))
        else:
            main_menu()

        fo.close()

    def openFile():
