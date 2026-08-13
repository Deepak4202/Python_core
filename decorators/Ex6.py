# 1. Login + Admin Access
# Create two decorators:
# login_required
# Output:
# 	Checking login
# admin_required
# Output:
# 	Checking admin permission
# Apply:
# 	@login_required
# 	@admin_required
# 	def delete_record():
#     		print(“Record deleted”)
# Output should be:
# 	Checking login
# 	Checking admin permission
# 	Record deleted

def login_required(fun):
    def login():
        print("Checking login")
        fun()
    return login
def admin_required(fun):
    def admin():
        print("Checking admin permission")
        fun()
    return admin

@login_required
@admin_required
def delete_record():
    print("Record deleted")

delete_record()

