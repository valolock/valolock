# ValoLock

ValoLock is a tool designed for Valorant players who wants to instalock(Yeah, I see you Jett main) ValoLock detects the game screen and automatically selects your preferred agent, ensuring you get to play the role you excel at, every game.

### Important Notice
Before diving into ValoLock, please review the **Warning** section to understand potential limitations and considerations.

## Features

- **Agent Auto-Selection**: Automatically selects your preferred agent using image recognition.
- **Customizable**: Configure agent positions and the lock-in button via the `config/config.json` file.
- **Easy to Use**: Simple UI for effortless operation.
- **Open Source**: Dive into the source code to understand how ValoLock works or contribute to its development.

## Getting Started

### Prerequisites
There are none, unless you are running the source code.

If so, ensure you have the following libraries installed:

- **OpenCV**: For image processing and recognition.
- **PyAutoGUI**: For simulating mouse and keyboard inputs.
- **pandas**: For efficient data manipulation.

### Installation

1. Download the latest release of ValoLock from [GitHub Releases](https://github.com/valolock/valolock/releases). Make sure to download `valolockx.x.x.zip`, not the source code archive.
2. Extract the `valolock` folder from the ZIP file.
3. Run the `valolock` executable found within the extracted folder.

### How to Use

1. After launching ValoLock, select your desired agent from the provided list.
2. Click the **Start** button.
3. Upon entering the agent selection screen in Valorant, ValoLock will automatically select your chosen agent.

## Configuration

Modify `config/config.json` to customize the positions of agents and the lock-in button to match your screen setup.

## Warning

- **Early Selection Bug**: There's a known issue where ValoLock attempts to select the agent before the selection screen is fully loaded. Any suggestions for resolving this are welcome.
- **Security Notice**: Windows may present a warning due to the executable's unrecognized status. We encourage users to review the source code if they have security concerns. Your safety and trust are paramount.

## Contributing

ValoLock welcomes contributions from the community. Whether it's fixing bugs, adding new features, or improving documentation, your help is valuable. Check out our [contributing guidelines](https://github.com/valolock/valolock/blob/main/CONTRIBUTING.md) for more information.
"""
