from Hien_thi_danh_sach_nhan_vien import Hiển_thị_danh_sách_nhân_viên
from Hien_thi_danh_sach_bo_phan import Hiển_thị_danh_sách_bộ_phận
from Them_nhan_vien_moi import Thêm_nhân_viên_mới
from Xoa_nhan_vien_theo_ID import Xóa_nhân_viên_theo_ID
from Xoa_bo_phan_theo_ID import Xóa_bộ_phận_theo_ID
from Hien_thi_bang_luong import Hiển_thị_bảng_lương
from Nangcao_Chinh_sua_nhan_vien import Nângcao_Chỉnh_sửa_nhân_viên

def main():
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-=-=-=
# Tạo menu khi khởi động chương trình
#------------------------------------
    while True:
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('1. Hiển thị danh sách nhân viên')
           # ------------------------------------
        print('2. Hiển thị danh sách bộ phận')
           # ------------------------------------
        print('3. Thêm nhân viên mới')
           # ------------------------------------
        print('4. Xóa nhân viên theo ID')
           # ------------------------------------
        print('5. Xóa bộ phân theo ID')
           # ------------------------------------
        print('6. Hiển thị bảng lương')
           # ------------------------------------
        print('7. Thoát')
           # ------------------------------------
        print('8. Chỉnh sửa nhân viên')
# ------------------------------------
        print('__________________________')
        user_input = input('Mời bạn nhập chức năng mong muốn (1-->8): ')
        if user_input == '3':
            Thêm_nhân_viên_mới()
        elif user_input == '1':
            Hiển_thị_danh_sách_nhân_viên()
        elif user_input == '2':
            Hiển_thị_danh_sách_bộ_phận()
        elif user_input == '4':
            Xóa_nhân_viên_theo_ID()
        elif user_input == '5':
            Xóa_bộ_phận_theo_ID()
        elif user_input == '6':
            Hiển_thị_bảng_lương()
        elif user_input == '7':
            print('Quit....')
            exit()
        elif user_input == '8':
            Nângcao_Chỉnh_sửa_nhân_viên()
        else:
            print('Type 1,2,3,4,5,6,7,8')


    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
if __name__=="__main__":
   main()

#oaeuopwqe