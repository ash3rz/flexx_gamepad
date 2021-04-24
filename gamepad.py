from flexx import flx

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

    #gamepad .a {
        background-position: 0 0;
        bottom: 0px;
        left: 56px;
    }

    #gamepad .b {
        background-position: -56px 0;
        top: 56px;
        right: 0px;
    }

    #gamepad .x {
        background-position: 112px 0;
        top: 56px;
    }

    #gamepad .y {
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

    #gamepad .dpad {
        position: absolute;
        width: 125px;
        height: 126px;
        top: 181px;
        left: 92px;
    }

    #gamepad .face {
        background: url(https://raw.githubusercontent.com/e7d/gamepad-viewer/master/templates/ds4/dpad.svg);
        position: absolute;
    }

    #gamepad .face.up,
    #gamepad .face.down {
        width: 36px;
        height: 52px;
    }

    #gamepad .face.left,
    #gamepad .face.right {
        width: 52px;
        height: 36px;
    }

    #gamepad .face.up {
        left: 44px;
        top: 0;
        background-position: -37px 0px;
    }

    #gamepad .face.down {
        left: 44px;
        bottom: 0;
        background-position: 0px 0;
    }

    #gamepad .face.left {
        top: 44px;
        left: 0;
        background-position: 104px 0;
    }

    #gamepad .face.right {
        top: 44px;
        right: 0px;
        background-position: 52px 0;
    }

    #gamepad .face[data-pressed="true"] {
        /* margin-top: 5px; */
        background-position-y: 52px;
    }

    #gamepad.half {
        margin-top: -300px;
    }

    """

    def create_triggers(self, root):
        triggers = document.createElement('div')
        triggers.setAttribute('class', 'triggers')

        triggerLeft = document.createElement('span')
        triggerLeft.setAttribute('class', 'trigger left')
        triggerLeft.setAttribute('data-button', 6)
        triggers.appendChild(triggerLeft)

        triggerRight = document.createElement('span')
        triggerRight.setAttribute('class', 'trigger right')
        triggerRight.setAttribute('data-button', 7)
        triggers.appendChild(triggerRight)

        triggerClear = document.createElement('span')
        triggerClear.setAttribute('class', 'clear')
        triggers.appendChild(triggerClear)

        root.appendChild(triggers)

    def create_bumpers(self, root):
        bumpers = document.createElement('div')
        bumpers.setAttribute('class', 'bumpers')

        bumperLeft = document.createElement('span')
        bumperLeft.setAttribute('class', 'bumper left')
        bumperLeft.setAttribute('data-button', 4)
        bumpers.appendChild(bumperLeft)

        bumperRight = document.createElement('span')
        bumperRight.setAttribute('class', 'bumper right')
        bumperRight.setAttribute('data-button', 5)
        bumpers.appendChild(bumperRight)

        bumperClear = document.createElement('span')
        bumperClear.setAttribute('class', 'clear')
        bumpers.appendChild(bumperClear)

        root.appendChild(bumpers)


    def create_touchpad(self, root):
        touchpad = document.createElement('div')
        touchpad.setAttribute('class', 'touchpad')
        touchpad.setAttribute('data-button', 17)

        root.appendChild(touchpad)

    def create_meta(self, root):
        meta = document.createElement('div')
        meta.setAttribute('class', 'meta')
        meta.setAttribute('data-button', 16)

        root.appendChild(meta)

    def create_arrows(self, root):
        arrows = document.createElement('div')
        arrows.setAttribute('class', 'arrows')
        
        select = document.createElement('span')
        select.setAttribute('class', 'select')
        select.setAttribute('data-button', 8)
        arrows.appendChild(select)

        start = document.createElement('span')
        start.setAttribute('class', 'start')
        start.setAttribute('data-button', 9)
        arrows.appendChild(start)

        arrowClear = document.createElement('span')
        arrowClear.setAttribute('class', 'clear')
        arrows.appendChild(arrowClear)

        root.appendChild(arrows)

    def create_buttons(self, root):
        buttons = document.createElement('div')
        buttons.setAttribute('class', 'buttons')

        aBtn = document.createElement('span')
        aBtn.setAttribute('class', 'button a')
        aBtn.setAttribute('data-button', 0)
        buttons.appendChild(aBtn)

        bBtn = document.createElement('span')
        bBtn.setAttribute('class', 'button b')
        bBtn.setAttribute('data-button', 1)
        buttons.appendChild(bBtn)

        xBtn = document.createElement('span')
        xBtn.setAttribute('class', 'button x')
        xBtn.setAttribute('data-button', 2)
        buttons.appendChild(xBtn)

        yBtn = document.createElement('span')
        yBtn.setAttribute('class', 'button y')
        yBtn.setAttribute('data-button', 3)
        buttons.appendChild(yBtn)

        root.appendChild(buttons)

    def create_sticks(self, root):
        sticks = document.createElement('div')  
        sticks.setAttribute('class', 'sticks')

        stickLeft = document.createElement('span')
        stickLeft.setAttribute('class', 'stick left')
        stickLeft.setAttribute('data-button', 10)
        stickLeft.setAttribute('data-axis-x', 0)
        stickLeft.setAttribute('data-axis-y', 1)
        sticks.appendChild(stickLeft)

        stickRight = document.createElement('span')
        stickRight.setAttribute('class', 'stick right')
        stickRight.setAttribute('data-button', 11)
        stickRight.setAttribute('data-axis-x', 2)
        stickRight.setAttribute('data-axis-y', 3)
        sticks.appendChild(stickRight)

        root.appendChild(sticks)

    def create_dpad(self, root):
        dpad = document.createElement('div')
        dpad.setAttribute('class', 'dpad')

        faceUp = document.createElement('span')
        faceUp.setAttribute('class', 'face up')
        faceUp.setAttribute('data-button', 12)
        dpad.appendChild(faceUp)

        faceDown = document.createElement('span')
        faceDown.setAttribute('class', 'face down')
        faceDown.setAttribute('data-button', 13)
        dpad.appendChild(faceDown)

        faceLeft = document.createElement('span')
        faceLeft.setAttribute('class', 'face left')
        faceLeft.setAttribute('data-button', 14)
        dpad.appendChild(faceLeft)

        faceRight = document.createElement('span')
        faceRight.setAttribute('class', 'face right')
        faceRight.setAttribute('data-button', 15)
        dpad.appendChild(faceRight)

        root.appendChild(dpad)


    def _create_dom(self):
        # Create the root element
        global document

        root = document.createElement('div')

        root.setAttribute('id', 'gamepad')
        root.setAttribute('data-color', 'black')

        self.create_triggers(root)
        self.create_bumpers(root)
        self.create_touchpad(root)
        self.create_meta(root)
        self.create_arrows(root)
        self.create_buttons(root)
        self.create_sticks(root)
        self.create_dpad(root)

        return root

class GamepadServer(flx.Widget):
    
    def init(self):
        with flx.HBox(title='Gamepad Test'):
            self.gamepad = GamepadClient()
        self.pressed = False
        self.cycle()

    def cycle(self):
        global window
        global document

        square = document.getElementsByClassName('button x')[0]
        if (square):
            self.pressed = not self.pressed
            square.setAttribute("data-pressed", self.pressed)
        
        window.setTimeout(self.cycle, 1000)


if __name__ == '__main__':
    a = flx.App(GamepadServer)
    a.serve()
    # m = a.launch('firefox')  # for use during development
    flx.start()