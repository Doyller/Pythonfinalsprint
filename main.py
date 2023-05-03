# final sprint SD7
#I.Doyle, S.Fifield, A.Singleton, J.Lodge, M.Mouland
import datetime
import FormatValues as FV
# Enter a new Employee (Driver)

# EmployeeFile = Employee.dat
# DefaultsFile = Default.dat

def EmployeeDat():
    DefaultsFile = open("Defaults.dat", "r")
    NextTransactionNum = float(DefaultsFile.readline())
    DriverNum = int(DefaultsFile.readline())
    StandFee = float(DefaultsFile.readline())
    DailyRentalFee = float(DefaultsFile.readline())
    WklyRentalRate = float(DefaultsFile.readline())
    HST = float(DefaultsFile.readline())

    DefaultsFile.close()
    AllowedChar = "ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-'"

    while True:
        JoinDate = input("Enter Date (YYYY-MM-DD) : ")
        if JoinDate == "":
            print("Date must not be blank. Please re-enter.")
        else:
            break

    while True:
        EmpFirstN = input("Enter new employee first name: ").title()
        if EmpFirstN == "":
            print("first name Name must not be blank. Please re-enter.")
        elif set(EmpFirstN).issubset(AllowedChar) == False:
            print("first Name contains invalid characters - re-enter")
        else:
            break

    while True:
        EmpLastN = input("Enter new employee last name: ").title()
        if EmpLastN == "":
            print("Last name must not be blank. Please re-enter.")
        elif set(EmpLastN).issubset(AllowedChar) == False:
            print("Last Name contains invalid characters - re-enter")
        else:
            break

    while True:
        Address = input("Enter employee address: ")
        if Address == "":
            print("Address can not be blank. Please re-enter.")
        else:
            break

    while True:
        PhoneNum = input("Enter phone number: ")
        if PhoneNum == "":
            print("Phone number cannot be blank - re-enter.")
        elif len(PhoneNum) != 10:
            print("Phone number must contain 10 digits - re-enter.")
        elif PhoneNum.isdigit() == False:
            print("Phone number must be 10 digits")
        else:
            break

    while True:
        LicenseNum = input("Enter driver license Number: ")
        if LicenseNum == "":
            print("License number can't be blank - re- enter")
        elif LicenseNum.isdigit() == False:
            print("License number must be Numbers")
        else:
            break

    while True:
        LicenseExpiry = input("Enter driver license expiry date (YYYY-MM-DD): ")
        if LicenseExpiry == "":
            print("License expiry date can't be blank - re- enter")
        else:
            break

    while True:
        CompanyNum = input("Enter company number: ")
        if CompanyNum == "":
            print("Company number can't be blank - re- enter")
        else:
            break

    while True:
        InsurancePolicy = input("Enter insurance policy Company: ")
        if InsurancePolicy == "":
            print("car make can't be blank - re- enter")
        else:
            break

    while True:
        PolicyNum = input("Enter policy number: ")
        if PolicyNum == "":
            print("Policy number can't be blank - re- enter")
        elif PolicyNum.isdigit() == False:
            print("Policy number must be Numbers")
        else:
            break

    while True:
        CarModel = ""
        CarStatus = input("Enter if Company vehicle (Y/N): ").upper()
        if CarStatus == "":
            print("can't be blank - re- enter")
        elif CarStatus == "Y":
            CarModel = (input("Enter Car model (1-4):"))
            break
        elif CarStatus == "N":
            CarModel = "NA"
            break

        # save Data to the Employee.dat file
        EmployeeFile = open("Employee.dat", "a")

        EmployeeFile.write("{}, ".format(JoinDate))
        EmployeeFile.write("{}, ".format(DriverNum))
        EmployeeFile.write("{}, ".format(EmpFirstN))
        EmployeeFile.write("{}, ".format(EmpLastN))
        EmployeeFile.write("{}, ".format(Address))
        EmployeeFile.write("{}, ".format(PolicyNum))
        EmployeeFile.write("{}, ".format(LicenseNum))
        EmployeeFile.write("{}, ".format(LicenseExpiry))
        EmployeeFile.write("{}, ".format(InsurancePolicy))
        EmployeeFile.write("{}, ".format(CompanyNum))
        EmployeeFile.write("{}, ".format(CarStatus))
        EmployeeFile.write("{},\n ".format(CarModel))

        EmployeeFile.close()

        DriverNum += 1

        while True:
            Continue = input("Do you want to process more Employees? (Y / N): ").upper()
            if Continue == "Y":
                return EmployeeDat
            else:
                break

# Enter Revenues

# imports
def RevFile():

    AllCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-'"

    # Constants
    HST_RATE = 0.15
    STANDFEE_RATE = 175.00

    # inputs

    while True:
        TransID = input("Enter the transaction ID: ")
        if TransID == "":
            print("Transaction ID invalid. Please re-enter. ")
        else:
            break

    while True:
        TransDate = input("Enter Transaction date YYYY-MM-DD: ")
        if TransDate == "":
            print("Transaction Date invalid, please re-enter.")
        else:
            break

    while True:
        DriverID = input("Enter the Driver ID: ")
        if DriverID == "":
            print("Driver ID cannot be blank, please re-enter.")
        else:
            break

    while True:
        TransAmt = float(input("Enter the transaction amount: "))
        if TransAmt == "":
            print("Transaction amount cannot be blank, please re-enter.")
        else:
            break

    # Calculations

    HST = TransAmt * HST_RATE
    TotCost = TransAmt + HST
    StandFee = STANDFEE_RATE

    # Create revenues file

    RevenueFile = open("Revenues.dat", "a")

    RevenueFile.write("{}, ".format(TransDate))
    RevenueFile.write("{}, ".format(TransID))
    RevenueFile.write("{}, ".format(DriverID))
    RevenueFile.write("{}, ".format(TransAmt))
    RevenueFile.write("{}, ".format(HST))
    RevenueFile.write("{}, ".format(TotCost))
    RevenueFile.write("{}, ".format(StandFee))

    RevenueFile.close()

    while True:
        Continue = input("Would you like to enter another Revenue? Y/N: ").upper()
        if Continue == "Y":
            return RevFile
        else:
            break


def Expenses():
    while True:
        DefaultsFile = open("Defaults.dat", "r")

        NextTransactionNum = float(DefaultsFile.readline())
        DriverNum = int(DefaultsFile.readline())
        StandFee = float(DefaultsFile.readline())
        DailyRentalFee = float(DefaultsFile.readline())
        WklyRentalRate = float(DefaultsFile.readline())
        HSTRATE = float(DefaultsFile.readline())

        DefaultsFile.close()

        InVoiceNum = input("Enter the invoice number: ")
        if InVoiceNum == "":
            print("The invoice number can't' be blank - re enter.")
            continue
        elif InVoiceNum.isdigit() == False:
            print("The invoice number can only be numbers - re enter")
            continue
        else:
            break

    while True:

        InvoiceDate = input("Enter Invoice date(YYYY-MM-DD): ")
        if InvoiceDate == "":
            print("Invoice date can't be blank - re enter ")
            continue
        else:
            break

    while True:

        DriverNum = input("Enter driver number: ")
        if DriverNum == "":
            print("Drive number can't be blank - re enter ")
            continue
        elif DriverNum.isdigit() == False:
            print("The Driver number can only be numbers - re enter")
            continue
        else:
            break

    while True:

        Itemnum = (input("Enter item number : "))
        if Itemnum == "":
            print("Item number can't be blank - re enter ")
            continue
        elif Itemnum.isdigit() == False:
            print("The item number can only be numbers - re enter")
            continue
        else:
            break

    while True:

        ItemDescription = input("Enter item description: ")
        if ItemDescription == "":
            print("Item description can't be blank - re enter")
            continue
        else:
            break

    while True:

        ItemCost = float(input("Enter item cost: "))
        if ItemCost == "":
            print("Item cost can't be blank - re enter ")
            continue
        else:
            break

    while True:

        Quantity = int(input("Enter the Quantity of items: "))
        if Quantity == "":
            print("Quantity can't be blank - re enter")
            continue
        else:
            break

    # cal
    ItemTotal = ItemCost * Quantity
    HSTExpenses = HSTRATE * ItemTotal
    TotalExpenses = ItemTotal + HSTExpenses

    # save Data to the Expenses.dat file
    EmployeeFile = open("Expenses.dat", "a")

    EmployeeFile.write("{}, ".format(InVoiceNum))
    EmployeeFile.write("{}, ".format(InvoiceDate))
    EmployeeFile.write("{}, ".format(DriverNum))
    EmployeeFile.write("{}, ".format(Itemnum))
    EmployeeFile.write("{}, ".format(ItemDescription))
    EmployeeFile.write("{:,.2f}, ".format(ItemCost))
    EmployeeFile.write("{}, ".format(Quantity))
    EmployeeFile.write("{:,.2f}, ".format(ItemTotal))
    EmployeeFile.write("{:,.2f}, ".format(HSTExpenses))
    EmployeeFile.write("{:,.2f},\n ".format(TotalExpenses))

    EmployeeFile.close()

    while True:

        Continue = input("Do you want to process more Expenses? (Y / N): ").upper()
        if Continue == "Y":
            return Expenses()
        elif Continue == "N":
            break

def RentalDat():
    DefaultsFile = open("Defaults.dat", "r")
    TransactionNum = float(DefaultsFile.readline())
    DriverID = int(DefaultsFile.readline())
    StandFee = float(DefaultsFile.readline())
    DailyRentalFee = float(DefaultsFile.readline())
    WklyRentalRate = float(DefaultsFile.readline())
    HST = float(DefaultsFile.readline())

    while True:
        RentOpt = input("Enter if the vehicle is being rented or an owned vehicle (O or R): ")
        if RentOpt == "R":
            PickUp = input("Enter when the vehicle was picked up (YYYY-MM-DD): ")
            CarNum = int(input("Enter which car was rented (1-4): "))
            NumDays = int(input("Enter how many days the car was rented for: "))
        else:
            break

        if NumDays <= 7:
            RentCost = NumDays * DailyRentalFee
        elif NumDays == 7:
            RentCost = WklyRentalRate
        else:
            break

        HST = RentCost * HST
        Total = HST + RentCost

        print("")
        print(f"HAB taxi service rental listing report")
        print(f"Was this a rented vehicle or was it an owner?: {RentOpt}")
        print("---------------------------------------------------------")
        print(f"Driver ID number:                              {DriverID:>4d}")
        print(f"Date of car rental:                            {PickUp}")
        print(f"Number of car that was rented:                 {CarNum:>1d}")
        print(f"Number of days vehicle was rented for:        {NumDays:>2d}")
        print("---------------------------------------------------------")
        print(f"Rental Cost:                                   {FV.FDollar2(RentCost)}")
        print("                                              ---------")
        print(f"HST Cost (@15%):                               {FV.FDollar2(HST)}")
        print("                                              ---------")
        print(f"Total cost after taxes:                        {FV.FDollar2(Total)}")

        f = open("Policies.dat", "a")
        f.write("{}, ".format(int(DriverID)))
        f.write("{}, ".format(RentOpt))
        f.write("{}, ".format(PickUp))
        f.write("{}, ".format(CarNum))
        f.write("{}, ".format(NumDays))
        f.write("{}\n, ".format(FV.FDollar2(Total)))
        f.close()
        print()
        print("Rental information processed and saved.")
        DriverID += 1

def ProfList():
    print("HAB Taxi Company")
    print(f"Profit Listing from (FV.FDateS(ProfitStartDate) to (FV.FDateS(ProfitEndDate)")
    print(
        "-------------------------------------------------------------------------------------------------------------------------------")
    print(" ")
    print(
        "Transaction ID.     Transaction Date.     Invoice Number.     Driver Number.     Item Number.     Quantity.     Revenue Amount.")
    print("")
    print(
        f"     (TransID:>4d)                  (FV.FDateS(TransDate))                    (InvoiceNum)                  (DriverNum:>4d)               (ItemNum:>4d)          (Quantity:>3d)               (FV.FDollar2(RevenueAmount):>9f")
    print("")
    print(
        f"     (TransID:>4d)                  (FV.FDateS(TransDate))                    (InvoiceNum)                  (DriverNum:>4d)               (ItemNum:>4d)          (Quantity:>3d)               (FV.FDollar2(RevenueAmount):>9f")
    print(
        "-------------------------------------------------------------------------------------------------------------------------------")
    print("")
    print(
        f"Revenues Listed:                                                                                                      (FV.FDollar2((RevenueAmount): > 9f")
    print(
        "                                                                                                                       --------")
    print(
        f"HST:                                                                                                                  (FV.FDollar((HST): > 9f")
    print(
        "                                                                                                                       --------")
    print(
        f"Total Revenue plus HST:                                                                                               (FV.FDollar2(RevenueAmount) + FV.FDollar2(HST):>9f")
    print(
        "                                                                                                                       --------")
    print(
        f"Calculated Profit:                                                                                                    (FV.FDollar2(Profit):>9f")
    print("We chose to not do this option, this would be the layout however")

def DriFinList():

    DefaultsFile = open("Defaults.dat", "r")
    TransactionNum = float(DefaultsFile.readline())
    DriverID = int(DefaultsFile.readline())
    StandFee = float(DefaultsFile.readline())
    DailyRentalFee = float(DefaultsFile.readline())
    WklyRentalRate = float(DefaultsFile.readline())
    HST = float(DefaultsFile.readline())
    while True:
        InvoiceDate = input("Enter the date of the invoice(YYYY-MM-DD): ")
        EndDate = input("Enter the end date of the invoice(YYYY-MM-DD): ")
        RentOpt = input("Enter whether this was an owner or a renter(O or R): ")
        NumDays = input(float("Enter the amount of days the car was rented for : "))

        if NumDays <= 7:
            RentalCosts = NumDays * DailyRentalFee
        elif NumDays == 7:
            RentalCosts = WklyRentalRate
        else:
            break

        if RentOpt == "R":
            Due = RentalCosts
        else:
            Due = StandFee

        HST = RentalCosts * HST
        Total = HST + RentalCosts



    print("       Driver Financial listing")
    print("—-----------------------------------")
    print(f"Driver Number:                  {DriverID:>4d}")
    print(f"Start date:                {FV.FDateS(InvoiceDate):>9}")
    print(f"End date:                  {FV.FDateS(EndDate):>9}")
    print(f"Daily Rental Fee:          {FV.FDollar2(DailyRentalFee):>9f}")
    print(f"Weekly Rental Fee:         {FV.FDollar2(WklyRentalRate):>9f}")
    print("                             --------")
    print(f"Monthly Stand Fee:         {FV.FDollar2(StandFee):>9f}")
    print(f"Transaction Cost:          {FV.FDollar2(RentalCosts):>9f}")
    print(f"Balance Due:               {FV.FDollar2(Due):>9f}")
    print("                             --------")
    print(f"HST:                       {FV.FDollar2(HST):>9f}")
    print(f"Total:                     {FV.FDollar2(Total):>9f}")

    f = open("FinList.dat", "a")
    f.write("{}, ".format(int(DriverID)))
    f.write("{}, ".format(RentOpt))
    f.write("{}, ".format(InvoiceDate))
    f.write("{}, ".format(EndDate))
    f.write("{}, ".format(NumDays))
    f.write("{}, ".format(Due))
    f.write("{}\n, ".format(FV.FDollar2(Total)))
    f.close()
    print()
    print("Financial information processed and saved.")
    DriverID += 1

def ExtraFeat():
    f = open("EfeatDefault.dat", "r")
    GAS_PER_LT = float(f.readline())
    WIN_WASH_PER = float(f.readline())
    SEAS_TIRE_CHG = float(f.readline())
    ROAD_ASSIST = float(f.readline())
    REG_COST = float(f.readline())
    f.close()

    while True:
        InvDate = datetime.datetime.now()
        InvDateDsp = InvDate.strftime("%Y-%m-%d")
        FirstCarYear = input("Enter the year of vehicle 1: ")
        FirstCarMake = input("Enter the make of vehicle 1: ")
        FirstCarModel = input("Enter the model of vehicle 1: ")
        FirstCarInsCost = float(input("Enter the yearly cost of insurance: "))
        SecondCarYear = input("Enter the year of vehicle 2: ")
        SecondCarMake = input("Enter the make of vehicle 2: ")
        SecondCarModel = input("Enter the model of vehicle 2: ")
        SecondCarInsCost = float(input("Enter the yearly cost of insurance: "))
        ThirdCarYear = input("Enter the year of vehicle 3: ")
        ThirdCarMake = input("Enter the make of vehicle 3: ")
        ThirdCarModel = input("Enter the model of vehicle 3: ")
        ThirdCarInsCost = float(input("Enter the yearly cost of insurance: "))
        FourthCarYear = input("Enter the year of vehicle 4: ")
        FourthCarMake = input("Enter the make of vehicle 4: ")
        FourthCarModel = input("Enter the model of vehicle 4: ")
        FourthCarInsCost = float(input("Enter the yearly cost of insurance: "))
        AmtWinWash = int(input("Enter the amount of windshield wash used :"))
        SeasonalTire = input("Enter whether tires will be changed (Y or N): ")
        CarOneLt = float(input("Enter the litres needed to fill car 1: "))
        CarTwoLt = float(input("Enter the litres needed to fill car 2: "))
        CarThreeLt = float(input("Enter the litres needed to fill car 3: "))
        CarFourLt = float(input("Enter the litres needed to fill car 4: "))
        CarOneFills = float(input("Enter how many times car 1 was filled this month: "))
        CarTwoFills = float(input("Enter how many times car 2 was filled this month: "))
        CarThreeFills = float(input("Enter how many times car 3 was filled this month: "))
        CarFourFills = float(input("Enter how many times car 4 was filled this month: "))
        RegDue = input("Enter whether registration will be paid this month(Y or N): " )

        if SeasonalTire == "Y":
            TireCost = SEAS_TIRE_CHG * 4
        else:
            TireCost = 0

        TotMonIns = (FirstCarInsCost + SecondCarInsCost + ThirdCarInsCost + FourthCarInsCost)/12
        RoadAssistCost = (ROAD_ASSIST * 4)/12
        OneGas = (CarOneLt * CarOneFills) * GAS_PER_LT
        TwoGas = (CarTwoLt * CarTwoFills) * GAS_PER_LT
        ThreeGas = (CarThreeLt * CarThreeFills) * GAS_PER_LT
        FourGas = (CarFourLt * CarFourFills) * GAS_PER_LT
        TotGas = OneGas + TwoGas + ThreeGas + FourGas
        WinWashCost = AmtWinWash * WIN_WASH_PER

        if RegDue == "Y":
            RegTotal = REG_COST * 4
            print(f"Cost of yearly registration: {FV.FDollar2(RegTotal)}")
        else:
            RegTotal = 0

        MonCost = TotMonIns + RoadAssistCost + RegTotal + TireCost + TotGas + WinWashCost
        HST = MonCost * 0.15
        TotMonCost = MonCost + HST
        print("---------------------------------------------------------------------------------------")
        print("HAB taxi service extra expenses report")
        print(f"{InvDateDsp}")
        print("Car Year   Car Model   Car Make   Number of fills")
        print("---------------------------------------------------------------------------------------")
        print(f"{FirstCarYear:>4s} {FirstCarMake:<10s}   {FirstCarModel:<10s}     {CarOneFills:<2f}")
        print(f"{SecondCarYear:>4s} {SecondCarMake:<10s}   {SecondCarModel:<10s}     {CarTwoFills:<2f}")
        print(f"{ThirdCarYear:>4s} {ThirdCarMake:<10s}   {ThirdCarModel:<10s}     {CarThreeFills:<2f}")
        print(f"{FourthCarYear:>4s} {FourthCarMake:<10s}   {FourthCarModel:<10s}     {CarFourFills:<2f}")
        print("---------------------------------------------------------------------------------------")
        print(f"Monthly gas cost for vehicle 1:   {FV.FDollar2(OneGas)}")
        print(f"Monthly gas cost for vehicle 2:   {FV.FDollar2(TwoGas)}")
        print(f"Monthly gas cost for vehicle 3:   {FV.FDollar2(ThreeGas)}")
        print(f"Monthly gas cost for vehicle 4:   {FV.FDollar2(FourGas)}")
        print(f"Total monthly gas cost:           {FV.FDollar2(TotGas)}")
        if SeasonalTire == "Y":
            print(f"Cost of seasonal tire change: {FV.FDollar2(TireCost)}")
        else:
            break
        if RegDue == "Y":
            print(f"Cost of yearly registration: {FV.FDollar2(RegTotal)}")
        else:
            break
        print(f"Total monthly cost of roadside assistance: {FV.FDollar2(RoadAssistCost)}")
        print(f"Total monthly cost of windshield wash:     {FV.FDollar2(WinWashCost)}")
        if SeasonalTire == "Y":
            print(f"Cost of seasonal tire change:      {FV.FDollar2(TireCost)}")
        else:
            break
        if RegDue == "Y":
            print(f"Cost of yearly registration:       {FV.FDollar2(RegTotal)}")
        else:
            break
        print(f"Monthly cost pre tax:                     {FV.FDollar2(MonCost)}")
        print(f"HST cost:                                 {FV.FDollar2(HST)}")
        print(f"Total monthly cost:                       {FV.FDollar2(TotMonCost)}")
        print()

        f = open("ExtraFeat.dat", "a")
        f.write("{}, ".format(InvDateDsp))
        f.write("{}, ".format(FirstCarYear))
        f.write("{}, ".format(FirstCarMake))
        f.write("{}, ".format(FirstCarModel))
        f.write("{}, ".format(CarOneFills))
        f.write("{}, ".format(SecondCarYear))
        f.write("{}, ".format(SecondCarMake))
        f.write("{}, ".format(SecondCarModel))
        f.write("{}, ".format(CarTwoFills))
        f.write("{}, ".format(ThirdCarYear))
        f.write("{}, ".format(ThirdCarMake))
        f.write("{}, ".format(ThirdCarModel))
        f.write("{}, ".format(CarThreeFills))
        f.write("{}, ".format(FourthCarYear))
        f.write("{}, ".format(FourthCarMake))
        f.write("{}, ".format(FourthCarModel))
        f.write("{}, ".format(CarFourFills))
        f.write("{}, ".format(OneGas))
        f.write("{}, ".format(TwoGas))
        f.write("{}, ".format(ThreeGas))
        f.write("{}, ".format(FourGas))
        f.write("{}, ".format(TotGas))
        f.write("{}, ".format(TireCost))
        f.write("{}, ".format(RegTotal))
        f.write("{}, ".format(RoadAssistCost))
        f.write("{}, ".format(WinWashCost))
        f.write("{}\n ".format(TotMonCost))
        f.close()
        print()
        print("Monthly report processed and saved.")

def Quit():
    print("Thank you for using HAB taxi menu program, bye bye. ")

while True:
    DisplayMenu()
    tmp = DisplayMenu()
    if tmp == "1":
        callable(EmployeeDat)
    elif tmp == "2":
        callable(RevFile)
    elif tmp == "3":
        callable(Expenses)
    elif tmp == "4":
        callable(RentalDat)
    elif tmp == "5":
    
    elif tmp == "6":
        callable(ProfList)
    elif tmp == "7":
        callable(DriFinList)
    elif tmp == "8":
        callable(ExtraFeat)
    elif tmp == "9":
        callable(Quit)
    else:
        input("invalid input, Please enter a valid option - press enter to continue...")
