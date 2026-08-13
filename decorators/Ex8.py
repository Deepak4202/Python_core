# 3. User Authentication + Payment Access
# Create two decorators:
# auth_required
# Output:
# 	Checking user authentication
# payment_required
# Output:
# 	Checking payment status
# Apply:
# 	@auth_required
# 	@payment_required
# 	def download_course():
# 	    	print(“Course downloaded”)
# Expected output:
# 	Checking user authentication
# 	Checking payment status
# 	Course downloaded

def auth_required(fun):
    def ar():
        print("Checking user authentication")
        fun()
    return ar

def payment_required(fun):
    def pr():
        print("Checking payment status")
        fun()
    return pr

@auth_required
@payment_required

def download_course():
 	print("Course downloaded")

download_course()