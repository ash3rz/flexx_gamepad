import sys

darwin = {
    0: "button square",
    1: "button cross",
    2: "button circle",
    3: "button triangle",
    4: "bumper left",
    5: "bumper right",
    6: "trigger left",
    7: "trigger right",
    8: "select",
    9: "start",
    10: "left stick",
    11: "right stick",
    12: "meta",
    13: "touchpad",
    "left": "dpad left",
    "right": "dpad right",
    "up": "dpad up",
    "down": "dpad down",
    "left_joystick_x": 0,
    "left_joystick_y": 1,
    "right_joystick_x": 2,
    "right_joystick_y": 5,
}

linux = {
    0: "button cross",
    1: "button circle",
    2: "button triangle",
    3: "button square",
    4: "bumper left",
    5: "bumper right",
    6: "trigger left",
    7: "trigger right",
    8: "select",
    9: "start",
    10: "meta",
    11: "left stick",
    12: "right stick",
    13: "touchpad",
    "left": "dpad left",
    "right": "dpad right",
    "up": "dpad up",
    "down": "dpad down",
    "left_joystick_x": 0,
    "left_joystick_y": 1,
    "right_joystick_x": 3,
    "right_joystick_y": 4,
}


def button_mapping(button_key):
    platform = sys.platform
    if "darwin" == platform:
        return darwin[button_key]
    else:
        return linux[button_key]
