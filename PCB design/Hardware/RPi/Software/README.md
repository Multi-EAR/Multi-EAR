# READ ME guide when creating a new datalogger

(1) write "raspbian-lite" to a SD-Card \
(2) Go into the "boot" file on the SD-Card, and "touch ssh", this enables SSH communication \
(3) Create within the "boot" file on the SD-Card: wpa_supplicant.conf. In here you add the WiFi details as explained in Appendix D. \
(4) Boot the RPi, and create the SSH connection \
(5) Create two folders: "/home/pi/UART" and "/home/pi/Data". \
(6) Import the python scripts: "UART_readout.py" and GEOPHYS_unit_convert.py" and add these to the "UART" folder. \
(7) Create a crontab at reboot: "@reboot python3 /home/pi/UART/UART_readout.py" \
(8) Reboot the RPi ~ the sensorplatform and RPi start logging data whenever the RPi is booted.


or

(2) connect the RPi direct to the TU Delft PC
(3) in Putty conntect to: "raspberrypi.local"
(4) login with "pi", and "raspberry"
(3) Go to the terminal and: "sudo raspi-config"
(4) enable SSH
(5) enable Serial
(6) Connect to WiFi by importing the modified "wpa_config.conf" file
(7) Continue from step (5) above!
