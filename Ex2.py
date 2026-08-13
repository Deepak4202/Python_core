def employee(**kwargs):
    k =kwargs
    for key, value in enumerate(k):
        print(key, ":", value)

employee(Name="Deepak", Salary=50000, City="Hyderabad")