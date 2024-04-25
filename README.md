# rpi-gpio-automation-interface

RPi GPIO Automation Interface, to implement design pattern for RPi GPIO.

## Implementation

This repository provides GPIO interface for RPi. Also implement "State" Design Pattern so that we can implement FSM easily for RPi systems.

## Initiation

- Fork this project and modify `__main__.py` for the main flow of the machine.

- Modify `context.py` and `states.py` to describe the state machine.

- Modify `.env.template` to describe how to add env variables to each machine.

- Modify `gpio_config.yml` to describe how many ports are used.

- Generally, `gpio` does not need to be modified.

## Creating a virtual env

```sh
python3 -m venv env
source env/bin/activate
pip3 install -r requirement.txt
```
