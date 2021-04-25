from flexx import flx
from button_mapping import button_mapping
import os

BASE_DIR = os.getcwd()

with open(BASE_DIR + '/flexx-gamepad/style.css') as f:
    style = f.read()

flx.assets.associate_asset(__name__, 'style.css', style)

global document


def create_triggers():
    triggers = document.createElement('div')
    triggers.setAttribute('class', 'triggers')

    trigger_left = document.createElement('span')
    trigger_left.setAttribute('class', 'trigger left')

    triggers.appendChild(trigger_left)

    trigger_right = document.createElement('span')
    trigger_right.setAttribute('class', 'trigger right')

    triggers.appendChild(trigger_right)

    trigger_clear = document.createElement('span')
    trigger_clear.setAttribute('class', 'clear')
    triggers.appendChild(trigger_clear)

    return triggers


def create_bumpers():
    bumpers = document.createElement('div')
    bumpers.setAttribute('class', 'bumpers')

    bumper_left = document.createElement('span')
    bumper_left.setAttribute('class', 'bumper left')

    bumpers.appendChild(bumper_left)

    bumper_right = document.createElement('span')
    bumper_right.setAttribute('class', 'bumper right')

    bumpers.appendChild(bumper_right)

    bumper_clear = document.createElement('span')
    bumper_clear.setAttribute('class', 'clear')
    bumpers.appendChild(bumper_clear)

    return bumpers


def create_touchpad():
    touchpad = document.createElement('div')
    touchpad.setAttribute('class', 'touchpad')

    return touchpad


def create_meta():
    meta = document.createElement('div')
    meta.setAttribute('class', 'meta')

    return meta


def create_arrows():
    arrows = document.createElement('div')
    arrows.setAttribute('class', 'arrows')

    select = document.createElement('span')
    select.setAttribute('class', 'select')

    arrows.appendChild(select)

    start = document.createElement('span')
    start.setAttribute('class', 'start')

    arrows.appendChild(start)

    arrow_clear = document.createElement('span')
    arrow_clear.setAttribute('class', 'clear')
    arrows.appendChild(arrow_clear)

    return arrows


def create_buttons():
    buttons = document.createElement('div')
    buttons.setAttribute('class', 'buttons')

    button_cross = document.createElement('span')
    button_cross.setAttribute('class', 'button cross')

    buttons.appendChild(button_cross)

    button_circle = document.createElement('span')
    button_circle.setAttribute('class', 'button circle')

    buttons.appendChild(button_circle)

    button_square = document.createElement('span')
    button_square.setAttribute('class', 'button square')

    buttons.appendChild(button_square)

    button_triangle = document.createElement('span')
    button_triangle.setAttribute('class', 'button triangle')

    buttons.appendChild(button_triangle)

    return buttons


def create_sticks():
    sticks = document.createElement('div')
    sticks.setAttribute('class', 'sticks')

    stick_left = document.createElement('span')
    stick_left.setAttribute('class', 'stick left')

    stick_left.setAttribute('data-axis-x', 0)
    stick_left.setAttribute('data-axis-y', 1)
    sticks.appendChild(stick_left)

    stick_right = document.createElement('span')
    stick_right.setAttribute('class', 'stick right')

    stick_right.setAttribute('data-axis-x', 2)
    stick_right.setAttribute('data-axis-y', 3)
    sticks.appendChild(stick_right)

    return sticks


def create_dpad():
    dpad = document.createElement('div')
    dpad.setAttribute('class', 'dpads')

    face_up = document.createElement('span')
    face_up.setAttribute('class', 'dpad up')

    dpad.appendChild(face_up)

    face_down = document.createElement('span')
    face_down.setAttribute('class', 'dpad down')

    dpad.appendChild(face_down)

    face_left = document.createElement('span')
    face_left.setAttribute('class', 'dpad left')

    dpad.appendChild(face_left)

    face_right = document.createElement('span')
    face_right.setAttribute('class', 'dpad right')

    dpad.appendChild(face_right)

    return dpad


class GamepadClient(flx.Widget):

    def _create_dom(self):
        root = document.createElement('div')
        root.setAttribute('id', 'gamepad')

        # This controls the gamepad skin color
        root.setAttribute('data-color', 'black')

        triggers = create_triggers()
        root.appendChild(triggers)

        bumpers = create_bumpers()
        root.appendChild(bumpers)

        touchpad = create_touchpad()
        root.appendChild(touchpad)

        meta = create_meta()
        root.appendChild(meta)

        arrows = create_arrows()
        root.appendChild(arrows)

        buttons = create_buttons()
        root.appendChild(buttons)

        sticks = create_sticks()
        root.appendChild(sticks)

        dpad = create_dpad()
        root.appendChild(dpad)

        return root

    @flx.action
    def connected(self, connected):
        element = document.getElementById("gamepad")
        if element:
            if connected:
                element.classList.remove("disconnected")
            else:
                element.classList.add("disconnected")

    @flx.action
    def axis_update(self, class_name, axis, value):
        element = document.getElementsByClassName(class_name)[0]
        if element:
            element.setAttribute("data-value-x" if axis == "x" else "data-value-y", value)
            x_value = element.getAttribute("data-value-x")
            y_value = element.getAttribute("data-value-y")
            element.style["margin-top"] = float(y_value) * 25 + "px"
            element.style["margin-left"] = float(x_value) * 25 + "px"

    @flx.action
    def button_update(self, button_key, pressed):
        class_name = button_mapping(button_key)
        self.button_render(class_name, pressed)

    @flx.action
    def button_render(self, class_name, pressed):
        button = document.getElementsByClassName(class_name)[0]
        if button:
            button.setAttribute("data-pressed", pressed)