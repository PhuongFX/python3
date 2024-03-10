def getNonBlankInput(message, error_message):
    x = input(message)
    while len(x.strip()) == 0:
        x = input(error_message)
    return x

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-=-=-=
# Xóa nhân viên theo ID
#----------------------
def Xóa_nhân_viên_theo_ID():
    import json
    try:
        f = open("names.json", "r")
        x = json.load(f)
        f.close()
    except IOError:
        print('nofile')
    ids = x['id']
    #print(ids)                                        # {'1': {'id_department': '2','2': {...'bonus_salary': 3}}
# ------------------------------------
    print('----')
    id = getNonBlankInput('Nhập mã nhân viên muốn xóa: ', 'Bạn không được bỏ trống thông tin này ')
# ------------------------------------
    idlast = []
    for n, a in ids.items():
        idlast.append(n)
        # print(idlast)                                                 # ['1', '2', '3', '4']
    # ------------------------------------
    try:
        if id in idlast:
            ids.pop(id)                                                 # input: 3 ,4 --> ['1', '2']
            print('Đã xóa thành công\n----')
        else:
            raise KeyError
    except KeyError:
        print('Mã nhân viên không tồn tại', id, '\n----')               # input: 9 --> ['1', '2', '3','4']
# ------------------------------------
    f = open("names.json", "w")
    x = json.dump(x, f,indent=2)
    f.close()