"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract, commission = None):
        self.name = name
        self.contract = contract
        self.commission = commission

    def get_pay(self):
        pay = self.contract.earning
        if self.commission != None:
            pay = pay + self.commission.earning
        return pay

    def __str__(self):
        pay = self.get_pay()

        pay_str = f"{self.name} works on a {self.contract}"
        commission_str = f""

        if self.commission != None:
            commission_str = f" and receives a {self.commission}"
        total_pay_str = f" Their total pay is {pay}."
        
        complete_str = pay_str + commission_str + "." + total_pay_str
        print(complete_str)
        return complete_str

class Contract:
    def __init__(self,earning, hours_worked = 0, hourly_rate = 0):
        self.earning = earning
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

        if earning == 0:
            self.earning = hourly_rate * hours_worked

    def __str__(self):
        contract_str = f""

        if self.hourly_rate == 0:
            contract_str = f"monthly salary of {self.earning}"
        else:
            contract_str = f"contract of {self.hours_worked} hours at {self.hourly_rate}/hour"

        return contract_str

class Commission:
    def __init__(self, earning, contracts = 0, pay_per_contract = 0):
        self.contracts = contracts
        self.pay_per_contract = pay_per_contract
        self.earning = earning

        if earning == 0:
            self.earning = contracts * pay_per_contract
        
    def __str__(self):
        commission_str = f""

        if self.contracts == 0:
            commission_str = f"bonus commission of {self.earning}"
        else:
            commission_str = f"commission for {self.contracts} contract(s) at {self.pay_per_contract}/contract"
        return commission_str


        

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', Contract(4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', Contract(0, 100, 25))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', Contract(3000), Commission(0, 4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', Contract(0, 150, 25), Commission(0, 3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', Contract(2000), Commission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', Contract(0, 120, 30), Commission(600))
