import sys

def main():
    fund_donor = []
    recipient = []
    while True:
        print("\n\n1. Enter fund donor's data\n2. Enter fund recipient's data\n3. Retrieve Donor specific data\n4. Retrieve Recipient specific data\n5. Exit system\n\n")
        ch = int(input("Enter your choice : "))
        if ch==1:
            print("\nEnter the following details:")
            name = input("Fund donor's name : ")
            ind = -1
            for i in range(len(fund_donor)):
                if name.lower()==fund_donor[i][0]:
                    ind = i
            if ind > -1:
                fund_donor[ind][2] += 1
            else:
                amtdon = input("Amount donated : ")
                waydon = input("Enter the method of donation : ")
                fund_donor.append([name,amtdon,1,waydon])
                print("\nThank you! Fund donor's details successfully updated!")
        elif ch==2:
            print("Enter the following details:")
            name = input("Fund recipient name : ")
            ind = -1
            for i in range(len(recipient)):
                if name.lower()==recipient[i][0]:
                    ind = i
            amtrec = input("Amount received : ")
            wayrec = input("Enter the method of fund transfer : ")
            recipient.append([name,amtrec,wayrec])
            print("\nThank you! Recipient details successfully updated!")
        elif ch==3:
            while True:
                print("\n1. Show data of all fund donors\n2. Show data of specific method of fund transfer\n")
                opt = int(input("Enter choice : "))
                if opt==1:
                    print("\n\nNAME\tAMT DONATED\tMETHOD\n")
                    for i in range(len(fund_donor)):
                        print(fund_donor[i][0]+"\t"+fund_donor[i][1]+"\t"+str(fund_donor[i][2]))
                        break
                elif opt==2:
                    hosp = input("Enter fund transfer method : ")
                    print("\n\nNAME\tAMT DONATED\tMETHOD\n")
                    for i in range(len(fund_donor)):
                        if fund_donor[i][2]==  waydon.lower():
                            print(fund_donor[i][0]+"\t"+fund_donor[i][1]+"\t"+str(fund_donor[i][2]))
                            break
                        else:
                            print("Wrong choice!! Try again!")
        elif ch==4:
            while True:
                print("1. Show dataof all Recipients\n2. Show data of specifc fund transfer\n")
                opt = int(input("Enter choice : "))
                if opt==1:
                    print("\n\nNAME\tAMT RECEIVED\tMETHOD OF FUND TRANSFER\n")
                    for i in range(len(recipient)):
                        print(recipient[i][0]+"\t"+recipient[i][1]+"\t"+str(recipient[i][2]))
                        break
                elif opt==2:
                    hosp = input("Enter method name : ")
                    print("\n\nNAME\tAMT RECIEVED\tMETHOD\n")
                    for i in range(len(fund_donor)):
                        if recipient[i][3].lower()==wayrec.lower():
                            print(recipient[i][0]+"\t"+recipient[i][1]+"\t"+str(recipient[i][2]))
                            break
                        else:
                            print("Wrong choice!! Try again!")
        elif ch==5:
            print("\n\nThank you for using our system!!\nHave a good day!\n")
            sys.exit(1)
        else:
            print("Wrong Choice!! Try again!")

main()