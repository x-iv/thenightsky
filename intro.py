#import the library and download the data
#to save images and plot use matplotlib
import matplotlib.pyplot as plt
from lightkurve import search_targetpixelfile
pixelfile = search_targetpixelfile("KIC 8462852", quarter=16).download(quality_bitmask='hardest');

pixelfile.plot(frame=1);
plt.savefig('frame1')
