# 5.	Create a Bank class with a class variable bank_name = "SBI" .
# Write a class method change_bank(new_bank) to update the bank name.

class Bank_class:
    bank_name = "SBI"

    @classmethod

    def change_bank(cls,new_bank):
        print("before ---------> {}".format(cls.bank_name))

        cls.bank_name = new_bank

        print("After ---------> {}".format(cls.bank_name))


Bank_class.change_bank("Au")