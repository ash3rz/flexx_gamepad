from flexx import flx

class Gamepad(flx.Widget):

    CSS = """
    #gamepad {
    width: 806px;
    height: 598px;
    }

    #gamepad {
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

    def _create_dom(self):
        # Create the root element
        return flx.create_element('div', {'id': 'gamepad', 'data-color': 'black'})

    def _render_dom(self):
        global document
        document.getElementById('gamepad').setAttribute('data-color', 'black')
        return [
            flx.create_element('div', {'class': 'triggers'},
                flx.create_element('span', {'class': 'trigger left', 'data-button': '6'}),
                flx.create_element('span', {'class': 'trigger right', 'data-button': '7'}),
                flx.create_element('span', {'class': 'clear'})),
            flx.create_element('div', {'class': 'bumpers'},
                flx.create_element('span', {'class': 'bumper left', 'data-button': '4'}),
                flx.create_element('span', {'class': 'bumper right', 'data-button': '5'}),
                flx.create_element('span', {'class': 'clear'})),
            flx.create_element('div', {'class': 'touchpad', 'data-button': '17'}),
            flx.create_element('div', {'class': 'meta', 'data-button': '16'}),
            flx.create_element('div', {'class': 'arrows'},
                flx.create_element('span', {'class': 'select', 'data-button': '8'}),
                flx.create_element('span', {'class': 'start', 'data-button': '9'}),
                flx.create_element('span', {'class': 'clear'})),
            flx.create_element('div', {'class': 'buttons'},
                flx.create_element('span', {'class': 'button a', 'data-button': '0'}),
                flx.create_element('span', {'class': 'button b', 'data-button': '1'}),
                flx.create_element('span', {'class': 'button x', 'data-button': '2'}),
                flx.create_element('span', {'class': 'button y', 'data-button': '3'})),
            flx.create_element('div', {'class': 'sticks'},
                flx.create_element('span', {'class': 'stick left', 'data-button': '10', 'data-axis-x': '0', 'data-axis-y': '1'}),
                flx.create_element('span', {'class': 'stick right', 'data-button': '11', 'data-axis-x': '2', 'data-axis-y': '3'})),
            flx.create_element('div', {'class': 'dpad'},
                flx.create_element('span', {'class': 'face up', 'data-button': '12'}),
                flx.create_element('span', {'class': 'face down', 'data-button': '13'}),
                flx.create_element('span', {'class': 'face left', 'data-button': '14'}),
                flx.create_element('span', {'class': 'face right', 'data-button': '15'}))
        ]

if __name__ == '__main__':
    a = flx.App(Gamepad)
    a.serve()
    # m = a.launch('firefox')  # for use during development
    flx.start()