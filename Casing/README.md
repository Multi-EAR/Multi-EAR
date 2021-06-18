# Casings

The protection of the PCB is done with a weather- and waterproof casing. The GPIO pins connect the RPi and the Multi-EAR. For insurance, they are as well connected by four screws on the corners. The casing exists of a pre-ordered polyethene case with an atmospheric dome on top. The RPi is connected to the casing, by a 3D-printed ground-plate, for direct coupling.

## Atmospheric dome
An atmospheric done is placed on top of the casing, fastened with screws and glue. The dome allows air to flow in and out of the casing, essential for the atmospheric measurements but deducts water to enter the casing. Figure \ref{fig:10} shows the 3D CAD design of the dome. Air can flow into the dome via the inlets on the side and top of the capture. This way, the dome enables airflow inside the casing but obstructs water. Whenever moisture becomes a problem, GoreTex air vents may be considered (\cite{den2020low}). Furthermore, the dome also prevents stagnation pressure, which may mask the differential pressure measurements (\cite{raspet2019new}).
 
## Casing designs
Two different casings are developed for the Multi-EAR (Appendix D). The smaller casing (\cite{SmallCasing})has a dimension of 130 x 85 x 115 mm (Figure \ref{fig:11}). The dome is placed on top of the transparent lid of the casing, while the two antennas are mounted to the side and the external power supply plug. The smaller casings are not fully autonomous, and it does not function without connection to an external power supply. Whenever powered, however, the Multi-EAR starts recording and collecting data, as pre-defined in the firmware.
 
The larger casings have a dimension of 240 x 191 x 130 mm (\cite{LargeCasing}) and includes a solar panel. These casings are designed to make the Multi-EAR completely autonomous. Again a polyethene case with the atmospheric dome on top is used. The GPS and LoRa antenna are connected to the outside of the casing and the ability to use external power.

## Antennae
The LoRa and GPS on the PCB are both connected to external antenna's. The antennae are passive LinX antennae (\cite{Linx}). The band with range is between 617MHz - 5 GHz. The classification of the antenna is a high-blade for optimal signal coverage. 
The polarization of the antennae is linear, and the radiation of signals omnidirectional. Moreover, the GPS on the PCB, and thus the antenna, is a GNSS receiver (\cite{GNS2301}) and thus compatible with GPS (global system), GLONASS (Russian navigational system), Beidou (Chinese navigational system), Galileo (European navigational system). Therefore the PCB has perfect coverage.   
The antennae are mounted to the outside of the casings and connected to the MEMS of the GPS and LoRa by SMA extension cables (\cite{SMAcable}, Appendix D).

## External power supply
5W micro-USB connectors generate the external power supply. The cable is modified to ensure the complete protection of the casing. Moreover, the modification allows disconnecting the power supply from the outside without doing modifications within the casing.
Within the casing, the RPi is connected through Micro-USB with a female Amphenol connector (\cite{Amphenol}, Appendix D). This female connector is pinned to the outside of the casing. The male connector is directly connected to a 5W adaptor. The connection between male and female connectors is strong and weather/waterproof. Figure \ref{fig:pin} shows the 'three-pin layout of the Amphenol connectors.
 
## Autonomous system
The larger casings are equipped with a solar panel (\cite{VoltaicSolar}) and battery pack (\cite{VoltaicBattery}). These platforms can either be powered by an external power supply or by a battery pack. The battery pack is a V75 battery and is placed within the casing. It has an 'always-on mode; it can power, charge, and pass-through charging. The capacity is 19.200 mAh (71 Watt-Hours), and the output is 5V. 

The solar panel that charges the V75 battery pack is placed on top of the casing. The mounting allows modification of sunlight's angle. The panel is waterproof and has a 9Watt, 6V output. 

## Energy analysis

To determine whether the autonomous system can monitor continuously, thorough energy analysis is performed. The energy analysis is divided into (1) the energy consumption by the PCB and RPi during concurrently continuous monitoring and the (2) power supply by the solar panel and battery capacity to survive the evenings.

First, the energy consumption by the RPi. Assuming continuous measurements and thus power supply, the RPi will use approximately 1 Watt per hour, which adds to a maximum of 24 Watt per day. 

The consumption by the PCB depends on the low-energy MEMS sensors, which is marginal compared to other monitoring devices. The power consumption is estimated at around 5W per day, which is 0.2 Watt per hour. 

Therefore, the total power consumption of the entire system is estimated to be approximately 29 Watt per day, which is 1.2 Watt per hour.

The V75 battery pack has a maximum capacity of 71 Watt. Without charging the battery pack, the monitoring system can be active for approximately 70 hours. During summer, the time between sunset and sunlight is approximately 6 hours. Therefore it is assumed the system will 'survive' the summer evenings. In winter, the nights are longer, and therefore the re-charging time of the battery is shorter. Moreover, thus the monitoring system is assumed to run out of power during these periods.

During the day, the battery pack needs to be charged while supplying the needed power for the monitoring system. To determine the expected charging energy of the solar panel, a thorough analysis is performed. For the analysis, the solar panel position is fixed to the Campus of the TU Delft. Based on the technical specifications of the 9 Watt solar panel and the expected sunlight at the Campus, energy analysis is calculated (\cite{SolarEnergy}). Figure \ref{fig:solar} shows the average energy output of the solar panel in Watt per day. Note that from March until September, the Solar panel provides enough power to run the system. Since enough power is provided for the monitoring system, the battery will be charged during the day. Within the winter months, however, the monitoring system will run out of power. The battery and solar panel will not provide sufficient power for continuous and concurrent monitoring.


