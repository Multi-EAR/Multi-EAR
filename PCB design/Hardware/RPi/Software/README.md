# READ ME guide when creating a new datalogger

(1) write "raspbian-lite" to a SD-Card \
(2) Go into the "boot" file on the SD-Card, and "touch ssh", this enables SSH communication \
(3) Create within the "boot" file on the SD-Card: wpa_supplicant.conf. In here you add the WiFi details as explained in Appendix D. \
(4) Boot the RPi, and create the SSH connection \
(5) Create two folders: "/home/pi/UART" and "/home/pi/Data". \
(6) Import the python scripts: "UART_readout.py" and GEOPHYS_unit_convert.py" and add these to the "UART" folder. \
(7) Create a crontab at reboot: "@reboot python3 /home/pi/UART/UART_readout.py" \
(8) Reboot the RPi ~ the sensorplatform and RPi start logging data whenever the RPi is booted.
