Function= ""
started=False
print("Insert the command HELP for proceed")
while True:
    Function=input(">").upper()
    if Function== "HELP":
        print('''Start-To start a car
Stop-To stop a car
Exit-To exit
        ''')
    elif Function== "START":
        if started:
            print("Car is already started....")
        else:
            started=True
            print("Car is started")


    elif Function== "STOP":
        if not started:
            print("Car is already stopped ....")
        else:
            started=False
            print("Car is stopped")
    elif Function=="EXIT":
        break
    else:
        print("I don't understand the statement")














