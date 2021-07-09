#import numpy as np

#data = open('data_2.txt', 'r')

with open('data_1625816225.log', 'rb') as f2:
	data = f2.read()
	for i in range(0,len(data)-2):
		if data[i] == 17 and data[i+1] == 153 and data[i+2] == 34 and data[i+3] == 136 and data [i+4] == 51 and data[i+5] == 115:
			#print(data[i:i+60])
			n_bytes = data[i+10]
			pay_load = data[i+11:i+11+n_bytes]
			print(len(pay_load))
			
			for n in [0,4,6,8,11,20]:
#,15,21,27]:
#,23,25,27,29]:
				if n==0:
					hour = float(pay_load[n])
					min  = float(pay_load[n+1])
					sec  = float(pay_load[n+2])
					mult = float(pay_load[n+3])
					print(hour,min,sec,mult)
				elif n==4:
					DLVR = pay_load[n]
					DLVR|= pay_load[n+1]
					pDLVR = float(DLVR)
					pDLVR*= 0.01*250.0/6553.0
					print(pDLVR)
				
				elif n==6:
					SP210 = (pay_load[n])<<8
					SP210|= pay_load[n+1]
					pSP210 = float(SP210)
					pSP210 = pSP210*1.0/(0.9*32768.0)
					pSP210 = pSP210*250
					print(pSP210)

				elif n==8:
					LPS = (pay_load[n])+(pay_load[n+1]<<8)+(pay_load[n+2]<<16)
					pLPS= float(LPS)
					pLPS/=4096.0
					print(pLPS)

				elif n==11:
					LIS3_x = pay_load[n]
					LIS3_x|= pay_load[n+1]
					pLIS_x = float(LIS3_x)
					pLIS_x*=0.076

					LIS3_y = pay_load[n+2]
					LIS3_y|= pay_load[n+3]
					pLIS_y = float(LIS3_y)
					pLIS_y*=0.076

					LIS3_z = pay_load[n+4]
					LIS3_z|= pay_load[n+5]
					pLIS_z = float(LIS3_z)
					pLIS_z*=0.076
					print(pLIS_x,pLIS_y,pLIS_z)
				elif n==160:
					LSM_x = pay_load[n]
					LSM_y = pay_load[n+1]
					LSM_z = pay_load[n+2]

				elif n==20:
					SHT_t = (pay_load[n])<<8
					SHT_t|= pay_load[n+1]
					pSHT_t = float(SHT_t)
					pSHT_t = -45+(175*pSHT_t/65535.0)

					SHT_h = (pay_load[n+2])<<8
					SHT_h|= pay_load[n+3]
					pSHT_h = float(SHT_h)
					pSHT_h*= 100.0/65535.0
					
					print(pSHT_t,pSHT_h)
				#print(float(pay_load[n]))
			#print(float(pay_load[5]))
			#for n in range(0,n_bytes):
				

