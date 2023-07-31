# README
This is a MicroPython package, created primarily with the Raspberry Pi Pico in mind. See here for more info: https://docs.micropython.org/en/latest/pyboard/tutorial/index.html

* Python version 3.x
  * (IDE) Pycharm has a slightly more involved setup than Thonny but is much better suited for project work
    * download Pycharm Community edition here: https://www.jetbrains.com/pycharm/

## Setting up MicroPython in Pycharm
1. Create a new project using Python 3.x (any version of Python 3 should work) as your project interpreter
2. In your project, got to ->Settings->Plugins and install MicroPython 
3. Next in the same Settings window of your project, go to the Languages & Frameworks tab, select MicroPrython from the highlighted options, then check the box 'Enable MicroPython Support'
4. Now you're ready to prepare your Raspberry Pi Pico 

## Preparing your Pico
1. Visit https://micropython.org/download/rp2-pico/ and download the latest firmware release
2. Connect your Pico to your machine while holding the BOOTSEL button on the Pico
3. Copy the firmware file to the base directory of the Pico (you should see the Pico listed in file explorer)
4. The Pico with reboot and be accessible in Pycharm

## Selecting and flashing your Pico in Pycharm
1. Open your Pycharm project back up and head back to Settings->Languages & Frameworks->MicroPython
2. With 'Enable MicroPython support' checked, select Raspberry Pi Pico from the Device type dropdown
3. Enter the path to your Pico in the Device Path field, the Detect button usually works as well
4. You're ready to start flashing Python files to your Pico
