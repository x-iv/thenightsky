from lightkurve import search_targetpixelfile
import numpy as np
import matplotlib.pyplot as plt
pixelfile = search_targetpixelfile("KIC 6922244", quarter=4).download();

pixelfile.plot(frame=1000)
plt.savefig('framep1000')


