
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-=-=-=
# Hiển thị danh sách bộ phận
#---------------------------
def Hiển_thị_danh_sách_bộ_phận():
    import json
    try:
        f = open("names.json", "r")
        x = json.load(f)
        f.close()
    except IOError:
        print('nofile')
    # ------------------------------------
    depa = x["department"]
    #print(depa)                                                        # {'1': 1, '2':2, '4':4}
    for n,d in depa.items():
        print(f'----\nMã bộ phận: {n}\n'
              f'Thưởng bộ phận: {d:,d} (VND)\n----')