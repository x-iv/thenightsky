from lightkurve import search_targetpixelfile
import matplotlib.pyplot as plt
import numpy as np
pixelfile = search_targetpixelfile("KIC 6922244", quarter=4).download();

pixelfile.plot(frame=1000)
plt.savefig('framep1000')

lc = pixelfile.to_lightcurve(aperture_mask=pixelfile.pipeline_mask)
lc.plot();
plt.savefig('nonlinedplot')


#flat_lightcurve
flat_lc = lc.flatten(window_length=401)
flat_lc.plot();
plt.savefig('flattenlightcurve')

#fold light curve
#when we fold we put the lines together i.e each period which is 3.522
#to identify period we use the periodogram
folded_lc = flat_lc.fold(period=3.522)
folded_lc.plot()
plt.savefig('folded')

