# Instructions:

# Write an inventory program in Python using OOP and SQLite. Use the db_base class we did in class to inherit from.

# Specifications:

# The  inventory database shall have two tables called "parts" and "inventory". (use the script from the in-class exercise as a reference, most should just be copy+paste and replacing column names)

# The parts table columns: id, name
# id of type integer; (INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE)
# name of type text (or you could use something like type varchar(50) [variable character length with a max of 50 characters]), you'll want to make this field unique using the "UNIQUE" attribute.
# The inventory table columns: id, part_id, quantity, current_price
# id of type integer; (INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE)
# part_id of type integer (This is your link to the parts table)
# quantity of type integer
# current_price of type varchar(20)
 

# Create a class that inherits from DBbase called Inventory and implement the Ctor and abstract methods accordingly.

# Create another class called Parts which also inherits from DBbase.

# Use the same DB file for each class.

 

# Create CRUD methods in each class to interact with the database:

# Basic functions for the Parts class:

# The ability to add a new part, change a part name, select a part and delete a part. Hint: if a part exists in the inventory table, you must first delete the inventory record.

 

# Basic functions for the Inventory class:

# Add inventory record based on the part Id.
# Update the quantity (plus or minus) and current price of the inventory.
# Ability to get all inventory
# Ability to get inventory of a specific part number.
# Write and include python code to create instances of your objects and test your class methods. Print out the outcomes using the print() function.

# Submit both your .py file and sqlite db file to receive a grade for this assignment.

 

# Parts Class Outline

# class Parts(DBbase):

#     def update(self, parts_id, name):
#         pass

#     def add(self, name):
#         pass

#     def delete(self, parts_id):
#         pass

#     def fetch(self, parts_id=None):
#         # if Id is null (or None), then get everything, else get by id
#         pass

#     def reset_database(self):
#         pass
 

# SQL Syntax Guidance:

# When to use execute_script(): When you have no parameters and no variables.
# Example: execute_script("""SELECT * FROM Artist""") -> notice there's no parameters, no variables, just raw SQL.
# When to use get_cursor.execute(): When you need to pass it parameters from the variables. This must be followed by a commit().
# Example: cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist,)) -> artist is the parameter, the "?" symbol gets replaced by the parameter.
# Handling SQL data types:
# When inserting numerical data types (ie integer), never use quotes.
# When inserting non-numerical data types, must use single quotes.
# Note: You don't need to worry about single quotes when using the parameters, the processor will figure it out.
 

# Full walk through videos for this assignment located in the Media Gallery.

# Please Note: The recording will reference this is homework 7, it is now homework 9.

 

# Alternatively, they are also posted on YouTube.

# SQL and HW9 Walkthrough Part 1 Parts Class:

# https://youtu.be/nUis_2n2X10 (Links to an external site.)


 

# SQL and HW9 Walkthrough Part 2 Inventory Class:

# https://youtu.be/YUdnFHa_kMY (Links to an external site.)


 

# SQL and HW9 Walkthrough Part 3:

# https://youtu.be/1Wuo68VY0_c (Links to an external site.)
