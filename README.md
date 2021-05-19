# Multi-EAR

The Multi Earth and Atmospheric data Recorder (Multi-EAR); a mobile low-cost multidiciplinairy sensor platform for scientific monitoring of earth and atmosphere.

<hr/>

A collabarotive project between the Royal Netherlands Meteorological Institute (KNMI) and Delft University of Technology (TU Delft).

<sub><sup>Auke Barnhoorn (TUD), Jens van den Berg (TUD), Mathijs Koymans (KNMI/TUD), Olivier den Ouden (KNMI/TUD), Pieter Smets (TUD/KNMI)</sup></sub>

<hr/>

This project has been awarded the 'Digitaliseringsfonds en Ontwikkeling' research grand by the Netherlands Ministry of Infrastructure and Water Management, and an 'Innovation' grand by Delft University of Technology. 

The Mulit-EAR is an extension of the <a href="https://amt.copernicus.org/articles/14/3301/2021/amt-14-3301-2021-discussion.html">INFRA-EAR</a>, which is a multidiciplinairy sensor platform for the monitoring of geophysical parameters, and especially designed to fit a Wandering Albatros. The Multi-EAR, however, does not have dimensinal restrictions. The goal of the project is to develop, based on earlier recommandations, a multidiciplinairy mobile sensor platform to complement the exisiting high-fidelity monitoring network. Due to its digital design, the sensor platform can readily be integrated with existing geophysical data infrastructures and be embedded in geophysical data analysis. The small dimensions and low cost price per unit allow for unconventional, experimental designs, for example, high-density spatial sampling or deployment on moving measurement platforms. Moreover, such deployments can complement existing high-fidelity geophysical sensor networks. To include the Multi-EAR within exisiting monitoring networks, a Technology Readiness Level (TRL) of 8 is needed. 

## PCB design
#### Hardware
The platform uses various digital MEMS sensors embedded on a Printed Circuit Board (PCB). Micro-electromechanical systems (MEMS) are small single-chip sensors that combine electrical and mechanical components and have low energy consumption. A programmable microcontroller unit, as well embedded on the PCB, controls the sensors’ sampling frequency and establishes the energy supply for the sensors and the data-communication and storage. A waterproof casing protects the platform against the weather. Because of its low power consumption, the system can be powered by a battery, solar panel, or an external power supply.

The PCB carries two differential pressure sensor (to measure infrasound), a 6-axis acclerometer/gyroscope, a 6-axis accelerometer/magnetometer, a barometric pressure sensor, a temperature/humidity sensor, microphones (to measure audible sound), and has in addition a GPS for location and timing purposes, and LoRa telecomunication for data exchange. 

#### Firmware
The communication between the microcontroller and MEMS sensor on the PCB is either done by Inter-Integrated Circuit (I2C) or Serial Peripheral Interface (SPI), and depends on the sensor and personal preference. Both communication methods are bus protocols and allow for serial data transfer. However, SPI handles full-duplex communication, simultaneous communication between microcontroller and MEMS sensor, while I2C is half-duplex. Therefore, I2C has the option of clock stretching, and the communication is stopped whenever the MEMS sensor cannot send data. Besides, I2C has built-in features to verify the data communication (e.g., start/stop bit, acknowledgement of data). Although the I2C protocol is favourable, it requires more power.

The microcontroller runs on self-made software, complementing the required manufacturers electrical and communication protocols. The software allows determining the sample time, sample frequency, and data storage of selected MEMS. The raw output of the digital MEMS sensors are stored as bits, and the microcontroller performs no data processing to save power consumption. 

## Raspberry Pi ~ external datalogger
The data can either be stored locally on a micro-SD card on the PCB, or be transfered to a Raspeberry Pi (RPi), which functions as datalogger. The data communication is done via UART communication. The RPi recieves on a pre-specified baud-rate the data in bytes, whenafter the data can either be formatted to floats, integer, or real units, before sending it to the server.

## Casings
The protection of the PCB is done with a weather- and waterproof casing. The RPi and the Multi-EAR are connected by the GPIO pins. For insurance, they are as well connected by four screws on the corners. The casing exists of a pre-ordered polyethylene case with an atmospheric dome on top. The RPi is connected to the casing, by a 3D-printed bottemplate, for direct coupling.

An atmospheric done is placed on top of the casing, fastened with screws and glue. The dome alows air to flow in and out the casing, which is essential for the atmospheric measurements, but deducts water to enter the casing.

### Formats
Two different casings are developed for the Multi-EAR. The smaller casing has a dimension of 00x00x00mm. The dome is placed on top of the transperent lid of the casing, while the two antennas are mounted to the side, as well the external power supply plug. The smaller casings are not fully autonome, it does not function without connection to an external power supply. Whenever powered, however, the Muilti-EAR starts recording and collecting data, as pre-defined in the firmware.

The larger casings have a dimension of 00x00x00mm, and have a solar panel on top of it. These casings are designed to make the Multi-EAR completely autonome. Again a polyethylene case with atmospheric dome on top is used. The solar panel charges the V75 battery pack, which is placed inside the casing. The power supply of the Multi-EAR is via the battery pack, which is either charged by the solar panel or external power supply. The GPS and LoRa antenna's are connected to the outside of the casing, as well the ability to use external power.




