#import the library and download the data
#to save images and plot use matplotlib
import numpy as np
import matplotlib.pyplot as plt
from lightkurve import search_targetpixelfile
pixelfile = search_targetpixelfile("KIC 8462852", quarter=16).download(quality_bitmask='hardest');

pixelfile.plot(frame=1000);
plt.savefig('frame1000')

lc = pixelfile.to_lightcurve(aperture_mask='all');
#objects
time_values = lc.time.value
flux_values = lc.flux.value

# Write lc.time and lc.flux to a text file
np.savetxt('lc_data.txt', np.column_stack((time_values, flux_values)), header='Time Flux', fmt='%f %f', comments='')
# 'lc_data.txt' is the name of the file where data will be saved
# header='Time Flux' specifies the column headers in the text file
# fmt='%f %f' specifies the format of data (floating-point numbers)
# comments='' specifies that no comment string will be prepended to each line

lc.plot();
plt.savefig('Boyajian star')
