# Field calibration

The field tests of the monitoring platform have been performed within building K of the KNMI. This building is placed at the border of the KNMI test field. Building K is a shelter and provides an energy supply for the monitoring system. However, for direct and correct comparison between the meteorological MEMS with the KNMI sensor network, it is recommended to perform future comparisons outside building K. The remainder of geophysical parameters are correctly sensed from building K.

## Meteorological observations
The LPS sensor has been field-tested (Figure \ref{fig:5}-a), along with a Paroscientific Digiquartz 1015A barometer, which has an accuracy of 0.05 hPa. Figure \ref{fig:fieldBaro} shows the comparison between the Mulit-EAR (red line) and the baroemtric reference sensor (black line). It stands out that both sensors resolve the changing barometric pressure. From the distribution of observations, it has been estimated that the LPS sensor has a precision of $\pm 0.1$ hPa for $87\%$ of the time. For the remainder, the maximum deviation was $\pm 0.2$ hPa. 

The comparison between the Multi-EAR's temperature has been performed with the reference sensor xx. This sensor has an accuracy of xx. Figure \ref{fig:fieldtemp}-a shows the comparisons between both. Not that the maximum temperature is correctly resolved by the Mulit-EAR. The minimum temperatures (occurring during the night), however, are not correctly resolved. This is due to the monitoring circumstances, building K conserves the 'day-warmth'.

The same phenomena occurs with the humidity sensor. The humidity within building K is continuously below the actual meteorological humidity. Therefore a correct comparison between the Multi-EAR's humidity sensor and the KNMI reference sensor can not be performed. 
 
## Sound observations


## Movement observations

Within \cite{den2020low} a comparison test has been carried out in the seismic pavilion of the KNMI. Inside this pavilion, the LSM accelerometers has been compared to a Streckeisen STS-2 seismometer connected to a Quanterra Q330, as a reference sensor \cite{knmi:1993}. Both sensors were installed on pillars, to ensure a good coupling between the subsurface and the sensor. The comparison test, which was based on 24 hours of recording, shows that the accuracy of the LSM303 3-axis accelerometer is $\pm1.5$ mg ($1.5 \text{ cm/s}^{2}$). While the sensors are deployed on the same seismic pillar and are thus subject to similar seismic noise conditions, the MEMS sensor could not measure ambient seismic noise (\cite{peterson1993observations,mcnamara2004ambient}) due to its high self-noise level. The LSM accelerometer exceeds both the U.S. Geological Survey New High Noise Model (NHNM) (\cite{peterson1993observations}) and the STS-2 reference sensor by at least 35 dB.

For the comparison between the two accelerometers on the Multi-EAR the z-components of both sensors has been used. The full recordings are divided into hourly recoridngs, which are used to calculate PSD's. The reference sensor in the seismic paviljoen confirms no major seismic activity has been recorded. Therefore, only ambient seismic noise is expected within the MEMS recordings. 

Figure \ref{fig:Accl} shows the stacked PSD's for the LSM (panel a) and LIS (panel b) MEMS sensors. The solid gray lines indicate the high and low ambient seismic noise curves (\cite{peterson1993observations,mcnamara2004ambient}). It is shown that both MEMS have a self-noise higher as the ambient seimsic noise. The MEMS, therefore, can not resolve these noise levels. Note that the self-noise levels of the MEMS is not equal. The LIS has a lower self-noise as the LSM, while the ADC has the same amount of bits (\cite{sleeman2006three}). However, ADC's are sometimes suffering a 'loss of bits' due to power supply. Whenever the efficiency of the MEMS not optimal, this may lead to less power supply towards the ADC, and thus a loss of bits. The LIS sensor is a accelerometer and gyroscope, whereas the LSM is an accelerometer and magnetometer. The combination may influence the efficiency of power towards the ADC, which explains the different self-noise levels.

Furthermore, the dotted black lines within both panels indicate the expected amplitude levels of earthquakes with an approximate distance of 10km (nearby transient sources) [cite raspberry shake manual]. Based on these levels it is highly expected that both MEMS will record a nearby transient event. 

Based on these plots, it is unlikely to use both MEMS for monitoring purposes of ambient seismic noise or teleseismic events. Previous studies drew similar conclusions concerning the performance of MEMS accelerometers. Various calibration set-ups are considered while comparing MEMS accelerometers with conventional accelerometers of geophones (\cite{hons2008field,albarbar2009performance,anthony2019low}), each concluding that the accuracy of the MEMS is not sufficient for recording ambient seismic noise. However, strong local events or boisterous environments the MEMS sensor will resolve those seismic signals.

