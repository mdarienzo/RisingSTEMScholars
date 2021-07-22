import numpy as np
import matplotlib.pyplot as plt

vis_bg_a = np.array([511.05, 396.21, 435.37, 474.34, 523.98, 321.17])
vis_bg_b = np.array([512.27, 396.21, 436.49, 474.34, 523.98, 321.17])
vis_bg_c = np.array([513.49, 397.51, 436.49, 475.33, 523.98, 322.13])
vis_bg_d = np.array([513.49, 397.51, 436.49, 475.33, 523.98, 322.13])
vis_bg_e = np.array([513.49, 397.51, 436.49, 475.33, 523.98, 322.13])
vis_bg = (vis_bg_a + vis_bg_b + vis_bg_c + vis_bg_d + vis_bg_d) / 5

nir_bg_a = np.array([1161.47, 277.70, 76.90, 43.03, 89.09, 55.91])
nir_bg_b = np.array([1161.47, 277.70, 76.90, 43.03, 89.09, 55.91])
nir_bg_c = np.array([1161.47, 277.70, 76.90, 43.03, 89.09, 55.91])
nir_bg_d = np.array([1161.47, 277.70, 76.90, 43.03, 89.09, 55.91])
nir_bg_e = np.array([1161.47, 277.70, 76.90, 43.03, 89.09, 55.91])
nir_bg = (nir_bg_a + nir_bg_b + nir_bg_c + nir_bg_d + nir_bg_d) / 5

bg = np.concatenate((vis_bg,nir_bg))
bg[5],bg[6]=bg[6],bg[5]

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

reflectance = reflectance-bg

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