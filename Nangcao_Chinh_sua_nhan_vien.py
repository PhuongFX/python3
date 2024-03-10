
# --------------------------------------------------
def getNonBlankInput(message, error_message):
    x = input(message)
    while len(x.strip()) == 0:
        x = input(error_message)
    return x
# ------------------------------------


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-=-=-=
# (Nâng cao) Thêm chức năng chỉnh sửa nhân viên
#----------------------------------------------
def Nângcao_Chỉnh_sửa_nhân_viên():
    import json
    try:
        f = open("names.json", "r")
        x = json.load(f)
        f.close()
    except IOError:
        print('nofile')
# ------------------------------------
    ids = x['id']                                      # {'1': {'id_department': '1','3': {...'bonus_salary': 3}}
# ------------------------------------
    print('----')
    print('Chỉnh sửa nhân viên')                       # 1
    edit = getNonBlankInput('Nhập mã nhân viên: ', 'Bạn không được bỏ trống thông tin này ')
# ------------------------------------
    idlast = []
    for n, a in ids.items():
        idlast.append(n)                                # ['1', '3', '4']
    # ------------------------------------
    if edit in idlast:
        name = str(input('Nhập họ và tên:'))                       # blank, any input
        if name != '':
            ids[edit]['name'] = name
        else:
            pass
    # ------------------------------------
        while True:
            try:
                cv = str(input('Nhập chức vụ(NV / QL): '))             # blank, only str () NV / QL --> blank break

                if str(cv) == '':
                    break
                if str(cv) == 'NV' or str(cv) == 'QL':
                    ids[edit]['cv'] = cv
                    break
                else:
                    print('Bạn cần nhập đúng NV / QL')
            except ValueError:
                print('Bạn cần nhập đúng NV / QL')

    # ------------------------------------
        while True:
            try:
                salary_base = input('Nhập hệ số lương: ')  # blank, only int() --> blank break
                if salary_base == '':
                    break
                else:
                    if int(salary_base) > 0 and int(salary_base) >= 1000:
                        ids[edit]['salary_base'] = int(salary_base)
                        break
                    if int(salary_base) > 0 and int(salary_base) < 1000:
                        print('[Nhập don vi: (ngan) VND] VD:100,000 VND/ngay ')
                    if int(salary_base) == 0:
                        ids[edit]['salary_base'] = int(salary_base)
                        break
                    if int(salary_base) < 0:
                        print('Bạn cần nhập đúng định dạng')
            except ValueError:
                print('Bạn cần nhập đúng định dạng')

    # ------------------------------------

        while True:
            try:
                working_days = input('Nhập số ngày làm việc:')
                if working_days == '':
                    break
                else:
                    if int(working_days) >= 0:
                        ids[edit]['working_days'] = int(working_days)
                        break
                    else:
                        print('Bạn cần nhập đúng định dạng')
            except ValueError:
                print('Bạn cần nhập đúng định dạng')

    # ------------------------------------

        while True:
            try:
                working_performance = input('Nhập hệ số hiệu quả:')
                if working_performance == '':
                    break
                if float(working_performance) >= 0:
                    ids[edit]['working_performance'] = float(working_performance)
                    break
                else:
                    if float(working_performance) <0:
                        print('Bạn cần nhập đúng định dạng')
            except ValueError:
                print('Bạn cần nhập đúng định dạng')


    # ------------------------------------
        while True:
            try:
                bonuse = input('Nhập thưởng: ')  # blank, only int() --> blank break
                if bonuse == '':
                    break
                else:
                    if int(bonuse) > 0 and int(bonuse) >= 1000:
                        ids[edit]['bonus'] = int(bonuse)
                        break
                    if int(bonuse) > 0 and int(bonuse) < 1000:
                        print('[Nhập don vi: (ngan) VND] VD:100,000 VND/ngay ')
                    if int(bonuse) == 0:
                        ids[edit]['bonus'] = int(bonuse)
                        break
                    if int(bonuse) < 0:
                        print('Bạn cần nhập đúng định dạng')
            except ValueError:
                print('Bạn cần nhập đúng định dạng')

        # ------------------------------------

        while True:
            try:
                late_coming_days = input('Nhập số ngày đi muộn: ')
                if late_coming_days == '':
                    break
                else:
                    if int(late_coming_days) >= 0:
                        ids[edit]['late_coming_days'] = int(late_coming_days)
                        break
                    else:
                        print('Bạn cần nhập đúng định dạng')
            except ValueError:
                print('Bạn cần nhập đúng định dạng')

    # ------------------------------------
        print('Đã hoàn tất chỉnh sửa\n----')
    # ------------------------------------
        dict_edit = ids[edit]                                       # ids[3]  # {'id_department': '3'..}
        b = list(dict_edit.values())                                # [3,QL,..]
        print(f'----\nMã số: {edit}\n'
              f'Mã bộ phận: {b[0]}\n'
              f'Chức vụ: {b[1]}\n'
              f'Họ và tên: {b[2]}\n'
              f'Hệ số lương: {b[3]:,d} (VND)\n'
              f'Số ngày làm việc: {b[4]} (ngày)\n'
              f'Hệ số hiệu quả: {b[5]}\n'
              f'Thưởng: {int(b[6]):,d} (VND)\n'
              f'Số ngày đi muộn: {b[7]}\n----')
        # ------------------------------------
    else:
        print('Mã nhân viên không tồn tại', edit, '\n----')

# ------------------------------------
    f = open("names.json", "w")
    x = json.dump(x, f,indent=2)
    f.close()