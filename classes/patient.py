class Patient:

    def __init__(self):
        self.fname = input('Enter patients first name: ')
        self.lname = input('Enter patients last name: ')
        self.phone = input('Enter patients phone: ')
        self.pernum = input('Enter patients pernum: ')
        self.patnum = patnum = self.phone[-4:] + self.pernum[-4:]
        self.full_name = self.fname + ' ' + self.lname
        self.pat_record = self.patnum + ' ' + self.full_name
        print('\nNew patient number generated: ' + self.patnum)
        print('New patient entry recorded: ' + self.pat_record)

    def getFName(self):
        return self.fname;
    def getLName(self):
        return self.lname;
    def getPhone(self):
        return self.phone;
    def getPernum(self):
        return self.pernum;
    def getPatnum(self):
        return self.patnum;
    def getFullName(self):
        return self.full_name;
    def getPatRecord(self):
        return self.pat_record;
