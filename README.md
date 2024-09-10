**Employee Management Program**
=====================================

<div style="text-align: left;">

  <a href='https://github.com/PhuongFX/ButterFlySpace/blob/main/LICENSE'><img style='display: inline-block; margin: 0; padding: 0;' src='https://img.shields.io/badge/License-AGPL%203.0-blue.svg' alt='License: AGPL-3.0'></a>
  <a href='https://www.python.org/'><img style='display: inline-block; margin: 0; padding: 0;' src='https://img.shields.io/badge/Python-3.x-blue' alt='Python'></a>
  <a href='https://github.com/PhuongFX/python3'><img style='display: inline-block; margin: 0; padding: 0;' src='https://img.shields.io/badge/Open%20Source-%E2%9D%A4-green.svg' alt='Open Source'></a>
  
</div>

Here's VN version [^2]. Here's ENG version [^1].

[^1]: Back.


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
Department ID does not exist

It looks like you want me to continue translating the text. Here is the rest of the translation:

> Department ID does not exist, creating new department...
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

[^2]: Back.

**Quản lý và tính tiền lương hàng tháng nhân viên trong công ty**
=====================================

<div style="text-align: left;">

  <a href='https://github.com/PhuongFX/ButterFlySpace/blob/main/LICENSE'><img style='display: inline-block; margin: 0; padding: 0;' src='https://img.shields.io/badge/License-AGPL%203.0-blue.svg' alt='License: AGPL-3.0'></a>
  <a href='https://www.python.org/'><img style='display: inline-block; margin: 0; padding: 0;' src='https://img.shields.io/badge/Python-3.x-blue' alt='Python'></a>
  <a href='https://github.com/PhuongFX/python3'><img style='display: inline-block; margin: 0; padding: 0;' src='https://img.shields.io/badge/Open%20Source-%E2%9D%A4-green.svg' alt='Open Source'></a>
  
</div>


<p align='center'>
  <img src="https://raw.githubusercontent.com/PhuongFX/python3/main/Screenshot%202024-09-05%20095431.jpg"/>
</p>


## `Tài nguyên`

[File thông tin thuế TNCN (XML)](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FChung%20chi%20dieu%20kien%2FPYB101x_1.1%2FASM_Resources%2Ftax.xml?alt=media&token=f7a6f73d-9e6d-4807-bb14-efc6875442c7)

* min < lương chịu thuế <= max
  
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


[File thông tin mức phạt đi muộn (JSON)](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FChung%20chi%20dieu%20kien%2FPYB101x_1.1%2FASM_Resources%2Flate_coming.json?alt=media&token=55246ee9-44fa-4642-aca2-dde101d705de)

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


## `Class`

> ### Employee, Manager
* id: Mã số nhân viên
* name: Họ và tên nhân viên
* salary_base: Hệ số lương cơ bản
* working_days: Số ngày làm việc trong tháng
* department: Mã bộ phận
* working_performance: Hệ số hiệu quả
* bonus: Thưởng
* late_comming_days: Số ngày đi muộn

> ### Department
* id: Mã bộ phận
* bonus_salary: Thưởng bộ phận


## `Menu chức năng`

* Có màn hình menu hiển thị tất cả các chức năng
* Có chức năng thêm/sửa/xóa nhân viên mới
* Có chức năng hiển thị lương của từng nhân viên

~~~
1. Hiển thị danh sách nhân viên.
2. Hiển thị danh sách bộ phận.
3. Thêm nhân viên mới.
4. Xóa nhân viên theo ID.
5. Xóa bộ phân theo ID
6. Hiển thị bảng lương.
7. Thoát.
Mời bạn nhập chức năng mong muốn:
~~~

> ### "Hiển thị danh sách nhân viên"

Với chức năng này, bạn sẽ in ra thông tin của các nhân viên được lưu trong hệ thống, theo format như sau:
~~~
----
Mã số: NV001
Mã bộ phận: SALE001
Chức vụ: Nhân viên
Họ và tên: Nguyễn Văn A
Hệ số lương: 200,000 (VND)
Số ngày làm việc: 26 (ngày)
Hệ số hiệu quả: 1
Thưởng: 500,000 (VND)
Số ngày đi muộn: 2
----
~~~

> ### "Hiển thị danh sách bộ phận"

Với chức năng này, bạn sẽ hiện thị danh sách tất cả các bộ phận đang có, theo format như sau:
~~~
----
Mã bộ phận: SALE01
Thưởng bộ phận: 500,000 (VND)
----
~~~

> ### "Thêm nhân viên mới"

Với chức năng này, người dùng sẽ được thêm một nhân viên mới vào danh sách. Người dùng sẽ được nhập liệu các thông tin cho nhân viên mới như sau:

~~~
----
Thêm nhân viên mới ...
Nhập mã số: 'NV002'
Nhập mã bộ phận: 'SALE002'
Nhập chức vụ (NV / QL): 'NV'
Nhập họ và tên: 'Nguyen Van B'
Nhập hệ sô lương: '300000'
Nhập số ngày làm việc: '25'
Nhập hệ số hiệu quả: '0.8'
Nhập thưởng: '0'
Nhập số ngày đi muộn: '0'
Đã thêm nhân viên mới ...
----
~~~
~~~
Mã bộ phận chưa tồn tại, tạo mới ...
Nhập thưởng bộ phận: 100000
Đã tạo bộ phận mới ...
Đã thêm nhân viên mới ...
~~~

> ### "Xóa nhân viên theo ID"

Với chức năng này, người dùng sẽ nhập ID của nhân viên muốn xóa và xóa nhân viên đó khỏi hệ thống. Ví dụ:

~~~
----
Nhập mã nhân viên muốn xóa: 'NV001'
Đã xóa thành công
----
~~~

> ### "Xóa bộ phận theo ID"

Tương tự với chức năng "Xóa nhân viên theo ID" nhưng là xóa bộ phận trên hệ thống.

> ### "Hiển thị bảng lương"

Với chức năng này, bạn hãy hiển thị bảng lương của tất cả nhân viên trong hệ thống, với format như sau:

~~~
----
Mã số: NV001
Thu nhập thực nhận: 4,961,880 (VND)
----
~~~

> ### "Thoát"

Với chức năng này, chương trình sẽ kết thúc.

> ### "Thêm chức năng chỉnh sửa nhân viên"

Người dùng sẽ nhập vào mã nhân viên muốn chỉnh sửa, sau đó là các trường muốn sửa và giá trị mới. Ví dụ:

~~~
----
Chỉnh sửa nhân viên
Nhập mã nhân viên: 'NV002'

Nhập họ và tên: ...
Nhập chức vụ (NV / QL): ...
Nhập hệ số lương: ...
Nhập số ngày làm việc: ...
Nhập hệ số hiệu quả: ...
Nhập thưởng: ...
Nhập số ngày đi muộn: ...

Đã hoàn tất chỉnh sửa
----
~~~


