from flexx import flx
from button_mapping import button_mapping

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

    CSS = """
    #gamepad {
        width: 806px;
        height: 598px;
    }
    
    #gamepad[data-color="black"] {
        background-image: url(https://raw.githubusercontent.com/e7d/gamepad-viewer/master/templates/ds4/base-black.svg);
    }
    
    #gamepad[data-color="white"] {
        background-image: url(https://raw.githubusercontent.com/e7d/gamepad-viewer/master/templates/ds4/base-white.svg);
    }
    
    #gamepad[data-color="red"] {
        background-image: url(https://raw.githubusercontent.com/e7d/gamepad-viewer/master/templates/ds4/base-red.svg);
    }
    
    #gamepad[data-color="blue"] {
        background-image: url(https://raw.githubusercontent.com/e7d/gamepad-viewer/master/templates/ds4/base-blue.svg);
    }
    
    #gamepad.disconnected {
        background-image: url(https://raw.githubusercontent.com/e7d/gamepad-viewer/master/templates/ds4/disconnected.svg);
    }
    
    #gamepad.disconnected div {
        display: none;
    }
    
    #gamepad .triggers {
        width: 588px;
        height: 90px;
        position: absolute;
        left: 109px;
    }
    
    #gamepad .trigger {
        width: 99px;
        height: 100%;
        background: url(https://raw.githubusercontent.com/e7d/gamepad-viewer/master/templates/ds4/triggers.svg);
        clip-path: inset(100% 0px 0px 0pc);
    }
    
    #gamepad .trigger[data-value="0"] {
        opacity: 0;
    }
    
    #gamepad .trigger.left {
        float: left;
    }
    
    #gamepad .trigger.right {
        float: right;
        background-position-x: 99px;
    }
    
    #gamepad .trigger[data-pressed="true"] {
        clip-path: inset(0% 0px 0px 0pc);
    }
    
    #gamepad .bumper {
        width: 99px;
        height: 23px;
        background: url(https://raw.githubusercontent.com/e7d/gamepad-viewer/master/templates/ds4/bumper.svg) no-repeat;
        opacity: 0;
    }
    
    #gamepad .bumpers {
        position: absolute;
        width: 588px;
        height: 23px;
        left: 109px;
        top: 94px;
    }
    
    #gamepad .bumper[data-pressed="true"] {
        opacity: 1;
    }
    
    #gamepad .bumper.left {
        /* -webkit-transform: rotateY(180deg); */
        /* transform: rotateY(180deg); */
        float: left;
    }
    
    #gamepad .bumper.right {
        float: right;
        transform: rotateY(180deg);
    }
    
    #gamepad .touchpad {
        width: 262px;
        height: 151px;
        position: absolute;
        left: 272px;
        top: 122px;
    }
    
    #gamepad .touchpad[data-pressed="true"] {
        background: url(https://raw.githubusercontent.com/e7d/gamepad-viewer/master/templates/ds4/touchpad.svg) no-repeat center;
    }
    
    #gamepad .meta {
        width: 42px;
        height: 42px;
        position: absolute;
        left: 382px;
        bottom: 216px;
    }
    
    #gamepad .meta[data-pressed="true"] {
        background: url(https://raw.githubusercontent.com/e7d/gamepad-viewer/master/templates/ds4/meta.svg) no-repeat center;
    }
    
    #gamepad .arrows {
        position: absolute;
        width: 352px;
        height: 46px;
        top: 142px;
        left: 227px;
    }
    
    #gamepad .select,
    #gamepad .start {
        background: url(https://raw.githubusercontent.com/e7d/gamepad-viewer/master/templates/ds4/start.svg);
        width: 28px;
        height: 46px;
        opacity: 0;
    }
    
    #gamepad .select[data-pressed="true"],
    #gamepad .start[data-pressed="true"] {
        opacity: 1;
    }
    
    #gamepad .select {
        float: left;
    }
    
    #gamepad .start {
        float: right;
        background-position: 28px 0;
    }
    
    #gamepad .buttons {
        position: absolute;
        width: 170px;
        height: 170px;
        top: 159px;
        left: 567px;
    }
    
    #gamepad .button {
        position: absolute;
        width: 56px;
        height: 56px;
        background: url(https://raw.githubusercontent.com/e7d/gamepad-viewer/master/templates/ds4/buttons.svg);
    }
    
    #gamepad .button[data-pressed="true"] {
        background-position-y: 56px;
    }
    
    #gamepad .cross {
        background-position: 0 0;
        bottom: 0px;
        left: 56px;
    }
    
    #gamepad .circle {
        background-position: -56px 0;
        top: 56px;
        right: 0px;
    }
    
    #gamepad .square {
        background-position: 112px 0;
        top: 56px;
    }
    
    #gamepad .triangle {
        background-position: 56px 0;
        left: 56px;
    }
    
    #gamepad .sticks {
        position: absolute;
        width: 361px;
        height: 105px;
        top: 308px;
        left: 228px;
    }
    
    #gamepad .stick {
        position: absolute;
        background: url(https://raw.githubusercontent.com/e7d/gamepad-viewer/master/templates/ds4/sticks.svg);
        height: 94px;
        width: 94px;
    }
    
    #gamepad .stick[data-pressed="true"].left {
        background-position-x: -96px;
    }
    
    #gamepad .stick[data-pressed="true"].right {
        background-position-x: -192px;
    }
    
    #gamepad .stick.left {
        top: 0;
        left: 0;
    }
    
    #gamepad .stick.right {
        top: calc(100% - 105px);
        left: calc(100% - 105px);
    }
    
    #gamepad .dpads {
        position: absolute;
        width: 125px;
        height: 126px;
        top: 181px;
        left: 92px;
    }
    
    #gamepad .dpad {
        background: url(https://raw.githubusercontent.com/e7d/gamepad-viewer/master/templates/ds4/dpad.svg);
        position: absolute;
    }
    
    #gamepad .dpad.up,
    #gamepad .dpad.down {
        width: 36px;
        height: 52px;
    }
    
    #gamepad .dpad.left,
    #gamepad .dpad.right {
        width: 52px;
        height: 36px;
    }
    
    #gamepad .dpad.up {
        left: 44px;
        top: 0;
        background-position: -37px 0px;
    }
    
    #gamepad .dpad.down {
        left: 44px;
        bottom: 0;
        background-position: 0px 0;
    }
    
    #gamepad .dpad.left {
        top: 44px;
        left: 0;
        background-position: 104px 0;
    }
    
    #gamepad .dpad.right {
        top: 44px;
        right: 0px;
        background-position: 52px 0;
    }
    
    #gamepad .dpad[data-pressed="true"] {
        /* margin-top: 5px; */
        background-position-y: 52px;
    }
    
    #gamepad.half {
        margin-top: -300px;
    }
    """

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