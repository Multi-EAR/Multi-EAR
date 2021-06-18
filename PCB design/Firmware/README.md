# Firmware

The communication between the microcontroller and MEMS on the PCB is either done by Inter-Integrated Circuit (I2C) or Serial Peripheral Interface (SPI) and depends on the sensor and personal preference. Both communication methods are bus protocols and allow for serial data transfer. However, SPI handles full-duplex communication, simultaneous communication between microcontroller and MEMS sensor, while I2C is half-duplex. Therefore, I2C has the option of clock stretching, and the communication is stopped whenever the MEMS sensor cannot send data. Besides, I2C has built-in features to verify the data communication (e.g., start/stop bit, acknowledgement of data). Although the I2C protocol is favourable, it requires more power. Moreover, the number of I2C ports on the microcontroller is limited. Therefore a mix of both SPI and I2C protocols is needed.

The microcontroller runs on self-made software, complementing the required manufacturers electrical and communication protocols. The software allows determining the sample time, sample frequency, and data storage of selected MEMS. The raw output of the digital MEMS sensors are stored as bits, and the microcontroller performs no data processing to save power consumption. 

The firmware, and thus the data acquisition, can be changed and updated on the microcontroller.
