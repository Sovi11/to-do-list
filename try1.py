# I want to make an app that is basically a calendar with to do apps 
# So every day will have 2 things right now, a to do list and a reminder list (both of the type list)


# I will start by making a class for the day
# This class will have 2 lists, one for to do and one for reminders
# It will also have a date attribute
# It will have methods to add to the to do and reminder lists
# It will have a method to display the lists
# It will have a method to remove from the lists
# It will have a method to clear the lists
# The dates will be from today -1 week to today + 3 weeks 

# we should make a class for reimnder and to do as well
# they will have a name , and a ID and the body which is list 

# each remider list will have a reminder object which is basically a string a time and a id

# each to do list will have a to do object which is basically a string and a id

# I will start by making the classes for the reminder and to do objects 

import datetime

ALL = 0
TODAY = 1
WEEK = 2

# I want to print output of a function in a file

import sys

debug = False




class todo_object :
    def __init__(self, ID, body):
        self.ID = ID
        self.body = body # string

    def display(self):
        print(f"T{self.ID}: {self.body}")

class todo_list:
    def __init__(self):
        self.list = []
        self.curr_id = 1
    
    def add_element(self, element):
        if (type(element) != todo_object):
            print(element)
            print(type(element))
            print("Error: element is not of type todo_object")
        else:
            self.list.append(element) # element should be of type todo_object
            self.curr_id += 1
    
    def display(self):
        print("TO LIST :")
        for element in self.list:
            element.display()
    
    def remove_element(self, element):
        self.list.remove(element)
    def remove_element_by_id(self, ID):
        for element in self.list:
            if element.ID == ID:
                self.list.remove(element)
                break
    
    def clear(self):
        self.list = []    
        self.curr_id = 1
    
    def give_curr_id(self):
        return self.curr_id

class reminder_object:
    def __init__(self,  ID , time , body):
        self.start_time = time # should be of type datetime
        self.ID = ID
        self.body = body # string

    def display(self):
        print(f"R{self.ID}: {self.body} at time {self.start_time}")
    
class reminder_list:
    def __init__(self):
        self.curr_id = 1
        self.list = []

    def add_element(self, element):
        if (type(element) != reminder_object):
            print("Error: element is not of type reminder_object")
        else:
            self.list.append(element) # element should be of type reminder_object
            self.curr_id += 1
    
    def display(self):
        print("REMINDER LIST :")
        for element in self.list:
            element.display()
    
    def remove_element(self, element):
        self.list.remove(element)

    def remove_element_by_id(self, ID):
        for element in self.list:
            if element.ID == ID:
                self.list.remove(element)
                break

    def clear(self):
        self.list = []
        self.curr_id = 1

    def give_curr_id(self):
        return self.curr_id

# Now I will make the class for the day

class day_calender:
    def __init__(self, date):
        self.date = date # should be of type datetime
        self.todo_list = todo_list()
        self.reminder_list = reminder_list()

    def display(self):
        print(f"Date: {self.date}")
        self.todo_list.display()
        self.reminder_list.display()

    def add_todo_element(self, element):
        self.todo_list.add_element(element)
    
    def add_reminder_element(self, element):
        self.reminder_list.add_element(element)
    
    def remove_todo_element(self, element):
        self.todo_list.remove_element(element)
    
    def remove_reminder_element(self, element):
        self.reminder_list.remove_element(element)
    
    def remove_todo_element_by_id(self, ID):
        self.todo_list.remove_element_by_id(ID)
    
    def remove_reminder_element_by_id(self, ID):
        self.reminder_list.remove_element_by_id(ID)
    
    def clear_todo_list(self):
        self.todo_list.clear()
    
    def clear_reminder_list(self):
        self.reminder_list.clear()
    def give_ids(self):
        return self.todo_list.give_curr_id(), self.reminder_list.give_curr_id()
    
# Now I will make the class for the calendar 
# this will have a list of days

class calendar:
    def __init__(self):
        # I will make a list of days from today - 1 week to today + 3 weeks
        self.list = []
        for i in range(-7, 21):
            today = day_calender(datetime.datetime.now().date() + datetime.timedelta(days=i))
            self.list.append(today)
    
    def add_day(self, tday):
        if (type(tday) != day_calender):
            print("Error: element is not of type day")
        else:
            self.list.append(tday)
    
    def display(self,type = ALL):
        if (type == ALL):
            for day in self.list:
                day.display()
                print("")
        elif (type == TODAY):
            self.list[7].display()
        elif (type == WEEK):
            for i in range(8):
                self.list[7+i].display()
                print("")
        else:
            print("Error: Invalid type")
    
    def remove_day(self, day):
        self.list.remove(day)
    
    def remove_day_by_date(self, date):
        for day in self.list:
            if day.date == date:
                self.list.remove(day)
                break
    
    def clear(self):
        self.list = []
    
    def update(self):
        # remove the oldest day and add the newest day
        today = day_calender(datetime.datetime.now().date() + datetime.timedelta(days=21))
        self.list.pop(0)
        self.list.append(today)

    def add_to_todo_list(self, which_day,body):
        # which day can go from -7 to 21
        to_do_id , reminder_id  =self.list[which_day+7].give_ids()
        self.list[which_day+7].add_todo_element(todo_object(to_do_id, body))
    
    def add_to_reminder_list(self, which_day, time, body):
        # which day can go from -7 to 21
        to_do_id , reminder_id  =self.list[which_day+7].give_ids()
        self.list[which_day+7].add_reminder_element(reminder_object(reminder_id, time, body))
    
    def remove_from_todo_list_id(self, which_day, ID):
        self.list[which_day+7].remove_todo_element_by_id(ID)
    
    def remove_from_reminder_list_id(self, which_day, ID):
        self.list[which_day+7].remove_reminder_element_by_id(ID)
    def save_to_main(self,main_file):
        orig_stdout = sys.stdout

        f = open(main_file, 'w')
        sys.stdout = f
        c.display()
        sys.stdout = orig_stdout
        f.close()
    
    def save_to_backup(self,backup_file):
        orig_stdout = sys.stdout

        f = open(backup_file, 'w')
        sys.stdout = f
        c.display()
        sys.stdout = orig_stdout
        f.close()

    def load_from_file(self,file):
        self.save_to_backup("backup.txt")
        self.clear()
        f = open(file, 'r')
        lines = f.readlines()
        if (lines[0][0:5] != "Date:"):
            print("Error: File is not of the correct format")
            return
        started = False
        parse_date = datetime.datetime.now().date()
        start_to_do = False
        start_reminder = False
        tday = day_calender(parse_date)
        if (debug ) : print(lines)
        for line in lines : 
            if (debug) : print(line)
            if (line[0:5]=="Date:" ):
                if (debug) : print(line)
                parse_date = datetime.datetime.strptime(line[6:16], "%Y-%m-%d").date()
                tday = day_calender(parse_date)
                started = True
                continue
            if (line[0:5]=="TO LI"):
                start_to_do = True
                start_reminder = False
                continue
            if (line[0:5]=="REMIN"):
                start_reminder = True
                start_to_do = False
                continue
            if (start_to_do):
                if (line[0:1]=="T"):
                    line_split = line.split()
                    tday.add_todo_element(todo_object(int(line_split[0][1:-1]),' '.join(line_split[1:])))
                    continue
                else:
                    print("Error: File is not of the correct format")
                    break
            if (start_reminder):
                if (line[0:1]=="R"):
                    line_split = line.split()
                    if (debug) : print(line_split)
                    # print(datetime.datetime.strptime(line_split[-2]+" "+line_split[-1], "%Y-%m-%d %H:%M:%S"))
                    tday.add_reminder_element(reminder_object(int(line_split[0][1:-1]),datetime.datetime.strptime((line_split[-2]+" "+line_split[-1]).split('.')[0], "%Y-%m-%d %H:%M:%S"),' '.join(line_split[1:-4])))
                    continue
                else:
                    if (line=='\n' or len(line)==0):
                        if (debug) : print("here")
                        start_reminder = False
                        start_to_do = False
                        started = False
                        if (debug): tday.display()
                        self.add_day(tday)
                    else:
                        print("Error: File is not of the correct format")
                        break

            

        


    


# I want todays date
# print(datetime.datetime.now().date())

# I will now test the classes
c = calendar()
c.load_from_file("storage.txt")
c.display()




