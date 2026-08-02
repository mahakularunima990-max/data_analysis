#Storing Student records using tuples
students=(("John", 80), ("Alice", 65), ("Bob", 90)) 
for name,marks in students:
        if marks >= 80:
            print(f"{name} has passed with distinction.")    