# ui/font_configurator.py

from ui.fonts import set_bold, set_regular

def apply_custom_fonts(ui):
    set_bold(ui.label_mqtt)
    set_bold(ui.Signin_btn_login)
    set_regular(ui.Signin_btn_signup)
