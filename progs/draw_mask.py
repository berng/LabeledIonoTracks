# Draw labeled ionogram parameters
# usage: python draw_mask.py filename.npz

import numpy as np
import matplotlib.pyplot as plt
import sys
fname=sys.argv[1]
d=np.load(fname)['data']
plt.figure(figsize=(8,8),constrained_layout=True)
plt.subplot(3,2,1)
cb=plt.scatter(d[:,0],d[:,1],c=d[:,4],s=5)
plt.colorbar(cb,label='Amplitude')
plt.xlabel('Frequency(MHz)')
plt.ylabel('Range(km)')

plt.subplot(3,2,2)
cb=plt.scatter(d[:,0],d[:,1],c=d[:,2],s=5)
plt.colorbar(cb,label='Polarization(deg)')
plt.xlabel('Frequency(MHz)')
#plt.ylabel('Range(km)')

plt.subplot(3,2,3)
cb=plt.scatter(d[:,0],d[:,1],c=d[:,5],s=5)
plt.colorbar(cb,label='Doppler drift(m/s)')
plt.xlabel('Frequency(MHz)')
#plt.ylabel('Range(km)')

plt.subplot(3,2,4)
cb=plt.scatter(d[:,0],d[:,1],c=d[:,6],s=5)
plt.colorbar(cb,label='Azimuth(deg.)')
plt.xlabel('Frequency(MHz)')
#plt.ylabel('Range(km)')

plt.subplot(3,2,5)
cb=plt.scatter(d[:,0],d[:,1],c=d[:,7],s=5)
plt.colorbar(cb,label='Zenith angle(deg.)')
plt.xlabel('Frequency(MHz)')
#plt.ylabel('Range(km)')

plt.subplot(3,2,6)
cb=plt.scatter(d[:,0],d[:,1],c=d[:,-1],s=5)
plt.xlabel('Frequency(MHz)')
#plt.ylabel('Range(km)')
plt.colorbar(cb,label='Cluster #')
#plt.savefig('out/'+fname+'.png')
plt.show()
