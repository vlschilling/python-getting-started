import math
signal_power = 1
noise_power = 1
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
print decibels
#print ratio