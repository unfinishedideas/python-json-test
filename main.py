import json
import datetime

# Simple python test for using JSON. Feel free to mess this up and play around with it...
#testing 1
#testing 2
filename = "./data/service_records.json"

def clearScreen():
    """Clears the screen with 100 lines""" #this is a docstring! (hover over function to show this string with intellisense)
    for i in range(100):
        print()

def choice():
    """Outputs menu options"""
    print("[1] View All Data")
    print("[2] Add Data")
    print("[3] Exit")

def viewData():
    """Outputs all data stored within json file"""
    with open(filename, "r") as f:
        temp = json.load(f)   #load json into python dictionary
        for key in temp:      #iterates over the keys stored in the json file 
            date_created = key["date_created"] #Ex. of how to extract key values
            date_of_service = key["date_of_service"]
            provider_id = key["provider_id"]
            member_id = key["member_id"]
            comments = key["comments"]
            print(f"Created on {date_created}")
            print(f"Date of Service: {date_of_service}")
            print(f"Provider ID: {provider_id}")
            print(f"Member ID: {member_id}")
            print(f"Comments: {comments}\n")

def addData():
    """Adds a service record to the database."""

    print("Add a Service Record\n\n")
    service_record = {} # empty dictionary, holds one service record

    with open (filename, "r") as f:
        temp = json.load(f) #returns json object as a python dictionary to temp

    current_date = datetime.date.today().strftime("%m-%d-%Y")
    print("Current Date: " + current_date)

    #assign values to all keys for a member account
    service_record["date_created"] = current_date
    service_record["date_of_service"] = input("Enter Date of Service [MM-DD-YYYY]: ") 
    service_record["provider_id"] = input("Enter Your Provider ID [9 digits]: ")
    service_record["member_id"] = input("Enter Member Number [9 digits]: ")
    service_record["comments"] = input("Enter Comments: ")

    clearScreen()
    temp.append(service_record) #update temp
    print("Service Record Added!\n")

    with open (filename, 'w') as f:
        json.dump(temp,f,indent=4)   #writes our updated temp dictionary to the json file

# Is this what main looks like in python? 
def runTest():
    clearScreen()
    print("Test JSON Database")
    print("Data Management System\n")

    while True: 
        choice()
        response = input("\nEnter Number: ")
        if response == "1":
            clearScreen()
            print("\nViewing All Service Records:\n")
            viewData()
            print()
        elif response == '2':
            clearScreen()
            addData()
        elif response =='3':
            clearScreen()
            print("Goodbye!\n\n\n\n")
            break
        else:
            clearScreen()
            print("You did not select a number, please read more carefully.\n")

runTest()