import matplotlib.pyplot as plt
import numpy as np
import serial
import time

Ts = 0.1
t = np.arange(0,10,Ts) # time vector; create Fs samples between 0 and 10.0 sec.
x = np.arange(0,10,Ts) # signal vector; create Fs samples
y = np.arange(0,10,Ts) # signal vector; create Fs samples
z = np.arange(0,10,Ts) # signal vector; create Fs samples
tilt = np.arange(0,10,Ts) # signal vector; create Fs samples

serdev = '/dev/ttyACM0'
s = serial.Serial(serdev, 115200)

for i in range(0, int(100)):
    x0=s.readline()
    x[i] = float(x0)
    y0=s.readline()
    y[i] = float(y0)
    z0=s.readline()
    z[i] = float(z0)
    t0=s.readline()
    tilt[i] = int(t0)
    

fig, ax = plt.subplots(2, 1)
ax[0].plot(t,x, label = 'x', color = 'b')
ax[0].plot(t,y, label = 'y', color = 'r')
ax[0].plot(t,z, label = 'z', color = 'g')
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Acc Vector')
ax[0].legend()
ax[1].stem(t, tilt, use_line_collection=True)
ax[1].set_xlabel('Time')
ax[1].set_ylabel('Tilt')
plt.show()
s.close()