def getNonBlankInput(message, error_message):
    x = input(message)
    while len(x.strip()) == 0:
        x = input(error_message)
    return x
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-=-=-=
# Xóa bộ phận theo ID
#--------------------
def Xóa_bộ_phận_theo_ID():
    import json
    try:
        f = open("names.json", "r")
        x = json.load(f)
        f.close()
    except IOError:
        print('nofile')
    # ------------------------------------
    ids = x['id']
    depa = x["department"]
    # ------------------------------------
    print('----')
    dep = getNonBlankInput('Nhập mã bộ phận: ', 'Bạn không được bỏ trống thông tin này ')
    #print(x)                  # {'id': {'1': {'id_department': '1, ,'2':,{},,'3':,{},,'4': {...'bonus_salary': 4}}
    #print(ids)                                # {'1': {'id_department': '2','2': {...'bonus_salary': 3}}
    #print(depa)                               # {'1': 1, '2':2, '4':4}
    # ------------------------------------
    idlast = []
    deplast = []
    for n,a in ids.items():
        idlast.append(n)
        #print(idlast)                                       # ['1', '2']
        b,c,d,e,f,g,h,j,k = a.values()
        deplast.append(b)
        #print(deplast)                                      # ['1', '2', '3', '4']
    # ------------------------------------
    try:
        if dep not in idlast:
            depa.pop(dep)                                                   # input: 4,3 --> ['2', '1']
            print('Đã xóa thành công\n----')
        else:
            print('Bạn không thể xóa bộ phận đang có nhân viên\n----')            # input: 1 --> ['1', '2']

    except KeyError:
        print('Mã bộ phận không tồn tại',dep,'\n----')                      # input: 9 --> ['1', '2']

    # ------------------------------------
    with open('names.json', 'w') as f:
        x = json.dump(x, f, indent=3)