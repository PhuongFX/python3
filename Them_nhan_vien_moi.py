
def getNonBlankInput(message, error_message):
    x = input(message)
    while len(x.strip()) == 0:
        x = input(error_message)
    return x
# ------------------------------------
def getStrInput(message, error_message):
    msg = message
    while True:
        try:
            x = str(input(msg))
            if x == 'NV' or x == 'QL':
                break
            else:
                raise ValueError
        except ValueError:
            msg = error_message
    return x
# ------------------------------------
def getValidIntegerInput(message, error_message):
    msg = message
    while(True):
        try:
            x = int(input(msg))
            if x>=0:
                break
            else:
                raise ValueError
        except ValueError:
            msg = error_message
    return x
# ------------------------------------
def getValidIntegerInput_000VND(message, error1, error2):
    msg = message
    while(True):
        try:
            x = int(input(msg))
            if x >0 and x >=1000:
                break
            else:
                if x < 1000:
                    msg = error2
                if x == 0:
                    break
                if x <0:
                    msg = error1
        except ValueError:
            msg = error1

    return x
# ------------------------------------
def getFLoatInput(message, error1):
    msg = message
    while True:
        try:
            x = float(input(msg))
            if x >=0:
                break
            else:
                msg = error1
        except ValueError:
            msg = error1
    return x


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-=-=-=
# Thêm nhân viên mới
#-------------------
def Thêm_nhân_viên_mới():
    import json
    try:
        f = open("names.json", "r")
        x = json.load(f)
        f.close()
    except IOError:
        print('nofile')
# ------------------------------------
    a = []
    id_inputs = []
    list_id = []
    list_dep = []
# ------------------------------------
    ids = x['id']
    # print(ids)                                    # {'1': {'id_department': '1','3': {...'bonus_salary': 3}}
    for n, z in zip(ids.values(), ids):
        list_id.append(z)

    depa = x["department"]
    # print(depa)                                   # {'1': 1, '2': 2, '3': 3}
    for n, d in depa.items():
        list_dep.append(n)
# ------------------------------------
    #print(list_id)                                 # ['1', '2', '3']
    #print(list_dep)                                # ['1', '3']
    # ------------------------------------
    print('----\nThêm nhân viên mới ...')
    id = getNonBlankInput('Nhập mã số: ', 'Bạn không được bỏ trống thông tin này ')
    # ------------------------------------
    if id not in list_id:
        id_inputs.append(id)
        d = {}
        d['id_department'] = getNonBlankInput('Nhập mã bộ phận: ', 'Bạn không được bỏ trống thông tin này ')
        d['cv'] = getStrInput('Nhập chức vụ(NV / QL): ', 'Nhập NV / QL ')
        d['name'] = getNonBlankInput('Nhập họ và tên: ', 'Bạn không được bỏ trống thông tin này ')
        d['salary_base'] = getValidIntegerInput_000VND('Nhập hệ sô lương: [don vi: (_000 VND)] ', 'Bạn phải nhập một số không âm ','[Nhập don vi: (ngan) VND] VD:100,000 VND/ngay ')
        d['working_days'] = getValidIntegerInput('Nhập số ngày làm việc: ', 'Bạn phải nhập một số không âm ')
        d['working_performance'] = getFLoatInput('Nhập hệ số hiệu quả: ','Bạn phải nhập một số không âm ')
        d['bonus'] = getValidIntegerInput_000VND('Nhập thưởng: [don vi: (_000 VND)] ', 'Bạn phải nhập một số không âm ','[Nhập don vi: (ngan) VND] VD:100,000 VND ')
        d['late_coming_days'] = getValidIntegerInput('Nhập số ngày đi muộn: ', 'Bạn phải nhập một số không âm ')
        print('Đã thêm nhân viên mới ...\n----')
        a.append(d)
        # ------------------------------------
        if d['id_department'] not in list_dep:
            print('Mã bộ phận chưa tồn tại, tạo mới ...')
            bonus_salary = getValidIntegerInput('Nhập thưởng bộ phận:', 'Bạn phải nhập một số không âm ')
            print('Đã tạo bộ phận mới ...\nĐã thêm nhân viên mới ...')
            d['bonus_salary'] = bonus_salary
        else:
            bonus_salary = depa[d['id_department']]
            d['bonus_salary'] = bonus_salary
        # ------------------------------------
        out = {}
        # print(d)                                   # {'id_department': '3', 'cv': 'QL', 'name': '3','bonus_salary': 3}
        # print(a)                                  # [{'id_department': '3', 'cv': 'QL', 'name': '3''bonus_salary': 3}]

        for n, z in zip(id_inputs, a):
            out[n] = z
            # print(out)                              # {'3': {'id_department': '3', ,,'name': '3','bonus_salary': 3}}
            x["id"][n] = z

        x["department"][d['id_department']] = d['bonus_salary']
    # ------------------------------------
    else:
        print('Mã nhân viên đã tồn tại')
# ------------------------------------

    # data = json.load(open('original_file.json'))
    with open('names.json', 'w') as f:
        x = json.dump(x, f, indent=3)


