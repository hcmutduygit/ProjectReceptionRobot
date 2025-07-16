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

    #page_attendance
    set_bold(ui.label_28)
    set_regular(ui.label)
    set_regular(ui.label_3)
    set_regular(ui.label_5)
    set_regular(ui.label_6)
    set_bold(ui.table_attendance)

    #page_camera, live telemetry, tracking
    set_bold(ui.label_26)
    set_bold(ui.label_27)
    set_bold(ui.label_30)

    #page_robotstatus
    set_bold(ui.label_29)
    set_regular(ui.label1_3)
    set_bold(ui.label_7)
    set_bold(ui.label_18)