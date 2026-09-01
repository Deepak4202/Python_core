# 3. Login System
# Create an abstract class LoginSystem with:
# login(username, password)
# logout()
# Create:
# •	AdminLogin
# •	UserLogin
# Implement login differently for admin and normal users.


from abc import ABC,abstractmethod
password = "Deepak"
class LoginSystem(ABC):

    @abstractmethod
    def login(self,username,passwords):
        pass

    @abstractmethod
    def logout(self):
        pass


class adminlogin(LoginSystem):

    def login(self,username,passwords):

        if password == passwords:

            print(f"Wellcome {username},admin login")

        else:
            print("Invalid Passwords")

    def logout(self):

        print("Logout successfully")


class UserLogin(LoginSystem):

    def login(self,username,passwords):
        if password == passwords:

            print(f"Wellcome {username},admin login")

        else:
            print("Invalid Passwords")

    def logout(self):

        print("Logout successfully")


obj1 = adminlogin()

obj1.login("Deepak","Deepak")

obj1.logout()

obj2 = UserLogin()

obj1.login("Deepak","Deepak")

obj1.logout()