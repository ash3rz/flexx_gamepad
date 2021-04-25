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
    "axis": {
        0: ["stick left", "x"],
        1: ["stick left", "y"],
        2: ["stick right", "x"],
        5: ["stick right", "y"]
    }
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
    "axis": {
        0: ["stick left", "x"],
        1: ["stick left", "y"],
        3: ["stick right", "x"],
        4: ["stick right", "y"]
    }
}


def button_mapping(button_key):
    platform = sys.platform
    if "darwin" == platform:
        return darwin[button_key]
    else:
        return linux[button_key]
