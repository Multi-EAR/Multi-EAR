# Connecting the Multi-EAR to a local network.

Connecting the sensor platform to a local WiFi network can be done in various ways. The information of the known WiFi networks is stored on the Raspberry Pi (RPi).  Within the folder “/etc/wpa_supplicant/“ the file “wpa_supplicant.conf” is stored. This is the WiFi information file. There are two, relatively easy ways, to update this file with a new WiFi network. This is either one (1) directly on the SD-card or (2) via an external connection od the RPi to a laptop.

## (1) Direct update on SD-card

Eject the SD-card from the RPi, and put it in the SD-card reader of your computer. Within the computer folder an external volume is detected: “boot”. This is the boot file of the RPi, which is used every time the RPi is booted. Within this boot file you “simply” paste the example “wpa_supplicant.conf” file from this GitHub page. **NOTE! You have to update this “wpa_supplicant.conf” file with the details of the local (or university) WiFi network!**

Whenever you have pasted this file to the boot volume, you can safely eject the SD-card from your computer. Insert the SD-card back into the RPi, whenever the RPi is booted the WiFi wpa_supplicant file is update with the new network information.

Knowledge about the IP-adres of the RPi on your local network can be obtained from the “Fing” app, which is available in the Apple App-store. This app allows to detect all devices on your local network, and their IP-adres. If you correctly followed the steps the RPi will show up within this list of devices connected to your network.

Thanks to a pre-check the RPi is enabled to acces via SSH. This can be done via Putty (Windows) or the Terminal (UNIX/Mac). 

## (2) External connection with computer 
**NOTE! First remove the Multi-EAR extension PCB!** 

A different approach is by connecting the RPi with a MicroSD-USB cable to your computer. The RPi is booted thanks to the power supply form the computer. Again via Putty or the Terminal you can now directly SSH towards the RPi. This is done by using the local IP adres:
	raspberrypi.local

Now you have entered the RPi, and you are able to update the “wpa_supplicant.conf”. 

Enter: “sudo nano /etc/wpa_supplicant/wpa_supplicant.conf“
Add the information of your local network (as shown within the example)
Exit the file, and reboot the system

To detect the IP-adres you can either use the “Fing” app, or: 
SSH again via: “raspberry.local”
Enter: “ifconfig” and readout the IP-adres.
