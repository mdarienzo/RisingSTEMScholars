import numpy as np
import matplotlib.pyplot as plt

vis_control = 
nir_control = 
control = np.concatenate((vis_control,nir_control))
control[5],control[6]=control[6],control[5]

yvis_a = np.array([835.04, 826.30, 2016.81, 1622.64, 1540.93, 492.79])
yvis_b = np.array([843.60, 832.82, 2032.48, 1633.51, 1555.93, 498.54])
yvis_c = np.array([836.26, 826.30, 2016.81, 1619.67, 1538.93, 491.83])
yvis_d = np.array([841.15, 830.21, 2030.24, 1631.53, 1554.93, 496.62])
yvis_e = np.array([839.93, 830.21, 2020.17, 1622.64, 1542.93, 493.74])
yvis = (yvis_a + yvis_b + yvis_c + yvis_d + yvis_e) / 5

ynir_a = np.array([1377.03, 326.05, 254.72, 161.78, 123.69, 61.50])
ynir_b = np.array([1377.03, 326.05, 254.72, 161.78, 123.69, 61.50])
ynir_c = np.array([1377.03, 326.05, 254.72, 161.78, 123.69, 61.50])
ynir_d = np.array([1378.18, 326.05, 254.72, 161.78, 123.69, 61.50])
ynir_e = np.array([1373.59, 326.05, 253.12, 160.92, 123.69, 61.50])
ynir = (ynir_a + ynir_b + ynir_c + ynir_d + ynir_e) / 5

reflectance = np.concatenate((yvis,ynir))
reflectance[5],reflectance[6]=reflectance[6],reflectance[5]

wavelengths = np.array([450,500,550,570,600,610,650,680,730,760,810,860])
x_pos = np.arange(len(wavelengths))

plt.bar(x_pos,reflectance,
        color=['darkviolet','blue','green','yellow',
               'orange','crimson','red','firebrick',
               'maroon','lightgray','darkgray','gray'],
        edgecolor='black')
plt.xticks(x_pos,wavelengths)
plt.title("Spectrum")
plt.ylabel("Reflectance")
plt.xlabel("Wavelength (nm)")

plt.show()