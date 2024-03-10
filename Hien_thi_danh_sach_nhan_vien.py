

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-=-=-=
# Hiển thị danh sách nhân viên
#-----------------------------
def Hiển_thị_danh_sách_nhân_viên():
    import json
    try:
        f = open("names.json", "r")
        x = json.load(f)
        f.close()
    except IOError:
        print('nofile')
    # ------------------------------------
    #print(x)
    '''{'id': {'1': {'id_department': '1', 'cv': 'QL', 'name': '1', 'salary_base': 1, 'working_days': 1,
                  'working_performance': 1, 'bonus': 1, 'late_coming_days': 1, 'bonus_salary': 1},
            '3': {'id_department': '3', 'cv': 'QL', 'name': '33', 'salary_base': 3, 'working_days': 3,
                  'working_performance': 3, 'bonus': 3, 'late_coming_days': 3, 'bonus_salary': 3}},
     'department': {'1': 1, '3': 3}}'''
    ids = x['id']
    #print(ids)                                           # {'1': {'id_department': '1','3': {...'bonus_salary': 3}}
    # ------------------------------------
    for n,z in zip(ids.values(),ids):
        a = list(n.values())                                   # ['3','1','3',,]  -->  [3, 1, 3, 23, 21, 3, 213,12]
        print(f'----\nMã số: {z}\n'
              f'Mã bộ phận: {a[0]}\n'
              f'Chức vụ: {a[1]}\n'
              f'Họ và tên: {a[2]}\n'
              f'Hệ số lương: {a[3]:,d} (VND)\n'
              f'Số ngày làm việc: {a[4]} (ngày)\n'
              f'Hệ số hiệu quả: {a[5]}\n'
              f'Thưởng: {int(a[6]):,d} (VND)\n'
              f'Số ngày đi muộn: {a[7]}\n----')
