import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from spacepy import pycdf
fname = "/home/ross/Downloads/psp_swp_spc_l2i_20181108_v01.cdf"
cdf = pycdf.CDF(fname)
t = cdf['Epoch'][:]
mv_lo = cdf['mv_lo'][:,:].T
mv_hi = cdf['mv_hi'][:,:].T
dcfd = cdf['diff_charge_flux_density'][:,:].T
for arr in (mv_lo, mv_hi, dcfd):
    arr[arr == -1e31] = np.nan
bad_data = np.any(~np.isfinite(mv_lo[:31,:]), axis=0)
def elliptic(x):
    a1 = 0.44325141463
    a2 = 0.06260601220
    a3 = 0.04757383546
    a4 = 0.01736506451
    b1 = 0.24998368310
    b2 = 0.09200180037
    b3 = 0.04069697526
    b4 = 0.00526449639
    return 1 + x*(a1 + x*(a2 + x*(a3 + x*a4))) + x*(b1 + x*(b2 + x*(b3 + x*b4)))*np.log(1/x)
    
V = (mv_hi + mv_lo) / 2
dV = (mv_hi - mv_lo) / 2
q = 1.602e-19
mp = 1.673e-27
v = np.sqrt(2 * q * mv_hi / mp) * (2 / np.pi) * elliptic(mv_lo / mv_hi)
dv = (((4*q*V) / mp) - v**2)**(0.5)
Fv = (dcfd/(q * v * 10**8)) * (1 / dv)
v = v[:, ~bad_data]
t = t[~bad_data]
Fv = Fv[:, ~bad_data]
plt.pcolormesh(t[np.newaxis,:], v[:31,:]/1000, Fv[:31,:], norm=colors.LogNorm(vmin=1, vmax=200), cmap=plt.cm.plasma);
plt.colorbar();
plt.show();
