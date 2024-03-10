#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-=-=-=
# Class
#---------------------
class Department:
    def __init__(self, id_department, bonus_salary):
        self.id_department = id_department
        self.bonus_salary = bonus_salary
# ------------------------------------
class Employee(Department):
    def __init__(self, id, id_department, cv,name, salary_base, working_days, working_performance, bonus, late_coming_days, bonus_salary):
        super().__init__(id_department,bonus_salary)
        self.id=id
        self.cv = cv
        self.name=name
        self.salary_base=salary_base
        self.working_days=working_days
        self.working_performance=working_performance
        self.bonus=bonus
        self.late_coming_days=late_coming_days
        self.luong_thuc_nhan= self.tinh_luong_thuc_nhan()
        #print(f'----\nMã số: {self.id}\nThu nhập thực nhận: {self.luong_thuc_nhan:,d} (VND)\n----')

    def luong_tre(self):
        phat_tre = 0
        if self.late_coming_days >= 0 and self.late_coming_days < 3:
            phat_tre = self.late_coming_days * 20000
        elif self.late_coming_days >= 3 and self.late_coming_days < 6:
            phat_tre = self.late_coming_days * 30000
        elif self.late_coming_days >= 6:
            phat_tre = self.late_coming_days * 50000
        return phat_tre

    def tinh_luong_tre(self):
        phat_tre = self.luong_tre()
        tổng_thu_nhập_chưa_thưởng = (self.salary_base * self.working_days) * self.working_performance

        tổng_thu_nhập = tổng_thu_nhập_chưa_thưởng + self.bonus + self.bonus_salary - phat_tre

        return tổng_thu_nhập

    def luong_thue(self):
        tổng_thu_nhập = self.tinh_luong_tre()
        global tổng_thu_nhập_chưa_thuế
        tổng_thu_nhập_chưa_thuế = tổng_thu_nhập * (89.5 / 100)

        luong_nhanchuathuong = 0
        if tổng_thu_nhập_chưa_thuế >0 and tổng_thu_nhập_chưa_thuế <=5000000:
            luong_nhanchuathuong = tổng_thu_nhập_chưa_thuế *(5/100)
        elif tổng_thu_nhập_chưa_thuế > 5000000 and tổng_thu_nhập_chưa_thuế <= 10000000:
            luong_nhanchuathuong = tổng_thu_nhập_chưa_thuế *(10 / 100)
        elif tổng_thu_nhập_chưa_thuế > 10000000 and tổng_thu_nhập_chưa_thuế <= 15000000:
            luong_nhanchuathuong = tổng_thu_nhập_chưa_thuế *(18 / 100)
        elif tổng_thu_nhập_chưa_thuế > 18000000 and tổng_thu_nhập_chưa_thuế <= 20000000:
            luong_nhanchuathuong = tổng_thu_nhập_chưa_thuế *(32 / 100)
        elif tổng_thu_nhập_chưa_thuế > 32000000 and tổng_thu_nhập_chưa_thuế <= 25000000:
            luong_nhanchuathuong = tổng_thu_nhập_chưa_thuế *(52 / 100)
        elif tổng_thu_nhập_chưa_thuế > 52000000 and tổng_thu_nhập_chưa_thuế <= 30000000:
            luong_nhanchuathuong = tổng_thu_nhập_chưa_thuế *(80 / 100)
        return luong_nhanchuathuong

    def tinh_luong_thuc_nhan(self):
        luong_thue = self.luong_thue()
        lương_thực_nhận = tổng_thu_nhập_chưa_thuế - luong_thue
        return round(lương_thực_nhận)
        #print(lương_thực_nhận)

    def hien_thi_luong(self):
        print(f'----\nMã số: {self.id}\nThu nhập thực nhận: {self.luong_thuc_nhan:,d} (VND)\n----')
# ------------------------------------
class Manager(Employee):
    def __init__(self, id, id_department,cv, name, salary_base, working_days, working_performance, bonus, late_coming_days, bonus_salary):
        super().__init__(id, id_department,cv, name, salary_base, working_days, working_performance, bonus, late_coming_days, bonus_salary )
        # Sai /Department.__init__(self, id_department, bonus_salary)/
        self.luong_thuc_nhan = self.tinh_luong_thuc_nhan1()
        #print(f'----\nMã số: {self.id}\nThu nhập thực nhận: {self.luong_thuc_nhan:,d} (VND)\n----')

    #def tinh_luong_Qly(self):
        #luong_nhanchuathuong = self.tinh_luong_thuc_nhan()
        #tổng_thu_nhập_Qly = luong_nhanchuathuong + ((10/100) * self.bonus_salary)
        #return round(tổng_thu_nhập_Qly)
        #print(tổng_thu_nhập_Qly)

    def tinh_luong_tre1(self):
        phat_tre = self.luong_tre()
        tổng_thu_nhập_chưa_thưởng = (self.salary_base * self.working_days) * self.working_performance

        tổng_thu_nhập = tổng_thu_nhập_chưa_thưởng + self.bonus + (10/100) *self.bonus_salary - phat_tre
        return tổng_thu_nhập


    def luong_thue1(self):
        tổng_thu_nhập = self.tinh_luong_tre1()
        global tổng_thu_nhập_chưa_thuế
        tổng_thu_nhập_chưa_thuế = tổng_thu_nhập * (89.5 / 100)

        luong_nhanchuathuong = 0
        if tổng_thu_nhập_chưa_thuế >0 and tổng_thu_nhập_chưa_thuế <=5000000:
            luong_nhanchuathuong = tổng_thu_nhập_chưa_thuế *(5/100)
        elif tổng_thu_nhập_chưa_thuế > 5000000 and tổng_thu_nhập_chưa_thuế <= 10000000:
            luong_nhanchuathuong = tổng_thu_nhập_chưa_thuế *(10 / 100)
        elif tổng_thu_nhập_chưa_thuế > 10000000 and tổng_thu_nhập_chưa_thuế <= 15000000:
            luong_nhanchuathuong = tổng_thu_nhập_chưa_thuế *(18 / 100)
        elif tổng_thu_nhập_chưa_thuế > 18000000 and tổng_thu_nhập_chưa_thuế <= 20000000:
            luong_nhanchuathuong = tổng_thu_nhập_chưa_thuế *(32 / 100)
        elif tổng_thu_nhập_chưa_thuế > 32000000 and tổng_thu_nhập_chưa_thuế <= 25000000:
            luong_nhanchuathuong = tổng_thu_nhập_chưa_thuế *(52 / 100)
        elif tổng_thu_nhập_chưa_thuế > 52000000 and tổng_thu_nhập_chưa_thuế <= 30000000:
            luong_nhanchuathuong = tổng_thu_nhập_chưa_thuế *(80 / 100)
        return luong_nhanchuathuong

    def tinh_luong_thuc_nhan1(self):
        luong_thue = self.luong_thue()
        lương_thực_nhận = tổng_thu_nhập_chưa_thuế - luong_thue
        return round(lương_thực_nhận)
        #print(lương_thực_nhận)




#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-=-=-=
# Hiển thị bảng lương
#---------------------
def Hiển_thị_bảng_lương():
    import json
    try:
        f = open("names.json", "r")
        x = json.load(f)
        f.close()
    except IOError:
        print('nofile')
    # ------------------------------------
    ids = x['id']                                       # {'1': {'id_department': '1','3': {...'bonus_salary': 3}}
# ------------------------------------
    aa = []
    idlast=[]
    for n, a in ids.items():
        idlast.append(n)
        aa.append(list(a.values()))
    # print(idlast)                                          # ['1', '3', '4']
    # print(aa)                               # [['1', 'QL', 'a', 200000, 26, 0.9, 9, 3, 500000], ['1', 'NV', 'a', 200000, 26, 0.9, 9, 3, 500000], ['4', 'NV', '4', 3, 3, 3, 3, 3, 3]]
# ------------------------------------
    for n,x in zip(idlast,aa):
        #print(n,x)
        if x[1] == 'QL':
            z = Manager(n,x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8])
            print(z.hien_thi_luong())
        else:
            z = Employee(n,x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8])
            print(z.hien_thi_luong())

'''Mời bạn nhập chức năng mong muốn (1-->8): 6
----
Mã số: 1
Thu nhập thực nhận: 5,082,706 (VND)
----
None
----
Mã số: 4
Thu nhập thực nhận: 21,712,702 (VND)
----
None
----
Mã số: 2
Thu nhập thực nhận: 8,660,021 (VND)
----
None'''