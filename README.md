**Employee Management Program**
=====================================

<div style="text-align: left;">

  <a href='https://github.com/PhuongFX/ButterFlySpace/blob/main/LICENSE'><img style='display: inline-block; margin: 0; padding: 0;' src='https://img.shields.io/badge/License-AGPL%203.0-blue.svg' alt='License: AGPL-3.0'></a>
  <a href='https://www.python.org/'><img style='display: inline-block; margin: 0; padding: 0;' src='https://img.shields.io/badge/Python-3.x-blue' alt='Python'></a>
  <a href='https://github.com/PhuongFX/python3'><img style='display: inline-block; margin: 0; padding: 0;' src='https://img.shields.io/badge/Open%20Source-%E2%9D%A4-green.svg' alt='Open Source'></a>
  
</div>


<p align='center'>
  <img src="https://raw.githubusercontent.com/PhuongFX/python3/main/Screenshot%202024-09-05%20095431.jpg"/>
</p>


## `Resources`

[File containing tax information (XML)](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FChung%20chi%20dieu%20kien%2FPYB101x_1.1%2FASM_Resources%2Ftax.xml?alt=media&token=f7a6f73d-9e6d-4807-bb14-efc6875442c7)

* min < taxable income <= max
  
~~~xml
<tax>
	<min>0</min>
	<max>5</max>
	<value>5</value>
</tax>
<tax>
	<min>5</min>
	<max>10</max>
	<value>10</value>
</tax>
...
~~~


[File containing late coming penalty information (JSON)](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FChung%20chi%20dieu%20kien%2FPYB101x_1.1%2FASM_Resources%2Flate_coming.json?alt=media&token=55246ee9-44fa-4642-aca2-dde101d705de)

~~~json
{
	"min": 0,
	"max": 3,
	"value": 20000
},
~~~

~~~python
late_comming_days * 20000
~~~

## `Classes`

> ### Employee, Manager
* id: Employee ID
* name: Employee name
* salary_base: Basic salary
* working_days: Number of working days in a month
* department: Department ID
* working_performance: Performance coefficient
* bonus: Bonus
* late_comming_days: Number of late coming days

> ### Department
* id: Department ID
* bonus_salary: Department bonus


## `Menu Functions`

* Display all menu functions
* Add, edit, and delete employee functions
* Display employee salary function

~~~
1. Display employee list.
2. Display department list.
3. Add new employee.
4. Delete employee by ID.
5. Delete department by ID
6. Display salary table.
7. Exit.
Enter your desired function:
~~~

> ### "Display Employee List"

This function displays the information of all employees in the system, in the following format:

~~~
----
ID: NV001
Department ID: SALE001
Position: Employee
Name: Nguyen Van A
Basic Salary: 200,000 (VND)
Working Days: 26 (days)
Performance Coefficient: 1
Bonus: 500,000 (VND)
Late Coming Days: 2
----
~~~

> ### "Display Department List"

This function displays the list of all departments in the system, in the following format:

~~~
----
Department ID: SALE01
Department Bonus: 500,000 (VND)
----
~~~

> ### "Add New Employee"

This function allows users to add a new employee to the system. Users will be prompted to enter the following information:

~~~
----
Add new employee...
Enter employee ID: 'NV002'
Enter department ID: 'SALE002'
Enter position (NV / QL): 'NV'
Enter name: 'Nguyen Van B'
Enter basic salary: '300000'
Enter working days: '25'
Enter performance coefficient: '0.8'
Enter bonus: '0'
Enter late coming days: '0'
Added new employee...
----
~~~
~~~
Department ID does not exist, creating new department...
Enter department bonus: 100000
Created new department...
Added new employee...
~~~

> ### "Delete Employee by ID"

This function allows users to delete an employee by entering their ID.

~~~
----
Enter employee ID to delete: 'NV001'
Deleted successfully
----
~~~

> ### "Delete Department by ID"

This function is similar to "Delete Employee by ID", but for deleting departments.

> ### "Display Salary"

This function displays the salary of all employees in the system, in the following format:

~~~
----
ID: NV001
Actual Income: 4,961,880 (VND)
----
~~~

> ### "Exit"

This function exits the program.

> ### "Edit Employee"

Users can enter the ID of the employee they want to edit, and then enter the new values for the employee's information.

~~~
----
Edit employee
Enter employee ID: 'NV002'

Enter name:...
Enter position (NV / QL):...
Enter basic salary:...
Enter working days:...
Enter performance coefficient:...
Enter bonus:...
Enter late coming days:...

Editing complete
----
~~~
