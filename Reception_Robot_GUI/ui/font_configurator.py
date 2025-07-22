# ui/font_configurator.py

from ui.fonts import set_bold, set_regular

def apply_custom_fonts(ui):
    #thanh cong cu
    set_bold(ui.label_mqtt)
    set_bold(ui.label_battery)

    #dashboard_login 
    set_regular(ui.Signin_btn_signup)
    set_regular(ui.Signin_btn_signin)
    set_bold(ui.Signin_text)
    
    #page_signin
    set_bold(ui.label_2)
    set_regular(ui.label_4)
    set_regular(ui.Signin_username)
    set_regular(ui.Signin_password)
    set_regular(ui.Signin_btn_login)

    #page_signup
    set_bold(ui.label_9)
    set_regular(ui.Signup_name)
    set_regular(ui.Signup_code)
    set_regular(ui.Signup_password)
    set_regular(ui.Signup_phone)
    set_regular(ui.Signup_username)
    set_regular(ui.Signup_btn_signup)

    #thanh cong cu
    set_bold(ui.label_mqtt_3)
    set_bold(ui.label_battery_3)
    set_bold(ui.comboBox_2)

    #page_attendance
    set_regular(ui.label_22)
    set_regular(ui.label_15)
    set_regular(ui.label_16)
    set_regular(ui.label_17)
    set_bold(ui.table_attendance_2)

    #page_control 
    set_regular(ui.label1_5)
    set_bold(ui.label_left_2)
    set_bold(ui.label_right_2)
    set_regular(ui.label1_6)
    set_bold(ui.label_13)
    set_bold(ui.label_19)
    set_bold(ui.label_14)
    set_bold(ui.mode_select_2)