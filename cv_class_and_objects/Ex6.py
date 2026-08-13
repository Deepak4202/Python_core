# 6.	Create a Hospital class with a class variable, hospital_name = "City Hospital" .
# Write a class method change_hospital(new_name) to update the hospital name.

class Hospital:
    hospital_name = "City Hospital"

    @classmethod
    def change_hospital(cls,new_name):
        cls.hospital_name =new_name


Hospital.change_hospital("XYZ Hospital")
print(Hospital.hospital_name)