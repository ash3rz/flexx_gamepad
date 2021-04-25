Flexx Gamepad
=============
A gamepad visualizer written in Python with [Flexx](https://github.com/flexxui/flexx) and [Pygame](https://github.com/pygame/pygame) with assets from [e7d's visualizer](https://github.com/e7d/gamepad-viewer).

Most gamepad visualizers work by reading inputs directly from the browser. This comes with the requirement that the gamepad be connected to the same device you want the visualizer to display on.

The purpose of this project is to enable users to connect their gamepad to any device and display the visualizer on a separate device, as long as the two devices are accessible to each other.

# Supported Controllers
* PlayStation DS4

# Supported Operating Systems
* Linux
* MacOS
* Windows

# Installation

You must have Python 3.5+.  Flexx has a [known issue](https://github.com/flexxui/flexx/issues/674) with Python 3.9 however.

```bash
$ pip install -r requirements.txt
```

# Running flexx_gamepad

> NOTE: Depending on your OS, you may encounter an error regarding missing dependencies for `pygame`.  Please refer to their [dependency docs](https://github.com/pygame/pygame#dependencies).

```bash
$ python3 server.py

Serving apps at http://0.0.0.0:3000
```

Open your local browser to http://0.0.0.0:3000, or, if the gamepad is connected to a separate device, open your browser to http://IP_ADDRESS:3000 where `IP_ADDRESS` is the IP address of the separate device.
