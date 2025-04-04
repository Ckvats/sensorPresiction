import numpy as np
import pandas as pd


df = pd.read_csv('modified_data.csv')

time = df['time']
temperature = df['temperature']
Pressure = df['pressure']
Compress_alarm = df['compress_alarm']
Cooling_alarm = df['cooling_alarm']
Final_alarm = df['final_alarm']
Critical_alarm = []
warning = []
attention = []
AnsAlarm = []
tempThreeshold = 45
pressureThreeshold = 800
thermalSensor = 'HE130_TT20_Z_PV [F]'
pressureSensor = 'EC3_PID_MIN_PT3_P_SP [Psi]'

for i in range(len(time)):
    if temperature[i]>tempThreeshold and Pressure[i]>pressureThreeshold:
        Critical_alarm.append("{} {} {}".format(time[i],thermalSensor,pressureSensor))
    elif temperature[i]>tempThreeshold:
        warning.append("{} {}".format(time[i],thermalSensor))
    elif Pressure[i]>pressureThreeshold:
        warning.append("{} {}".format(temp[i],pressureSensor))
    elif temperature[i]==tempThreeshold or Pressure[i]==pressureThreeshold:
        if(temperature[i]==tempThreeshold):
            attention.append("{} {}".format(time[i],thermalSensor))
        elif Pressure[i]==pressureThreeshold:
            attention.append("{} {}".format(time[i],pressureSensor))
        else:
            attention.append("{} {} {}".format(time[i],thermalSensor,pressureSensor))
    

Max = max(len(Critical_alarm),len(warning),len(attention))
Critical_alarm += ['']*(Max-len(Critical_alarm))
warning += ['']*(Max-len(warning))
attention += ['']*(Max-len(attention))
dg = pd.DataFrame({'Critical_Alarm':Critical_alarm,'Warning':warning,'Attention':attention})
dg.to_csv('alarm_final_data.csv',index=False)
print(dg.head)
print(Critical_alarm)
print(warning)
print(attention)

