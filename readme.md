# valolock

This project is a tool for automatically selecting agents in valorant. It uses image recognition to detect the screen and select the agent.

## How to Run

To run this project, execute the `main.py` script or download one of the releases and pick the agent you want to instalock and click start. When you load into agent select
it should then instalock the agent.

## Dependencies

This project uses the following libraries:

- OpenCV: For image processing and recognition.
- PyAutoGUI: For automating mouse and keyboard actions.
- pandas: For handling data.

## Configuration

You can configure the positions of the agents and the lock-in button in the `config/config.json` file.

## Warning
It does contain a bug where it tries to lock the agent before you're fully loaded in. I don't know what to do about it, but you're very much welcome to suggest a solution.