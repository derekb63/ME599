#!usr/bin/env python

# Derek Bean
# ME 599
# 1/31/2017


from msd import MassSpringDamper as msd
import matplotlib.pyplot as plt

mass = 1.0
spring_const = 200.0
damper_const = 3.0

smd = msd(mass, spring_const, damper_const)
state, t = msd.simulate(smd, mass, spring_const, damper_const)


plt.figure(1)
plt.plot(t, [x[0] for x in state], 'k')
plt.xlabel('time (s)')
plt.ylabel('displacement')
plt.show()
