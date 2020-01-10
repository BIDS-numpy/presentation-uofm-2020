# IPython log file

from pycbc.catalog import Merger
m = Merger('GW150914')
data = {
    ifo : m.strain(ifo) for ifo in ('H1', 'L1')
}
ligo_data = dat['L1']
ligo_data = data['L1']
ligo_data
type(ligo_data)
import pycbc
get_ipython().run_line_magic('pinfo', 'pycbc.types.timeseries.TimeSeries')
pycbc.types.timeseries.TimeSeries.__bases__
pycbc.types.timeseries.Array.__bases__
get_ipython().run_line_magic('pinfo2', 'pycbc.types.timeseries.TimeSeries')
get_ipython().run_line_magic('pinfo2', 'pycbc.types.timeseries.Array')
get_ipython().run_line_magic('pinfo', 'ligo_data._data')
type(ligo_data._data)
get_ipython().run_line_magic('pinfo', 'ligo_data._data')
type(ligo_data._data)
pycbc.types.aligned.ArrayWithAligned.__bases__
get_ipython().run_line_magic('pinfo2', 'ligo_data.highpass_fir')
get_ipython().run_line_magic('pinfo', 'pycbc.filter.highpass_fir')
import pycbc.filter
get_ipython().run_line_magic('pinfo', 'pycbc.filter.highpass_fir')
get_ipython().run_line_magic('pinfo2', 'pycbc.filter.highpass_fir')
get_ipython().run_line_magic('pinfo2', 'ligo_data.highpass_fir')
freq = 15
get_ipython().run_line_magic('pinfo2', 'ligo_data.highpass_fir')
get_ipython().run_line_magic('pinfo2', 'pycbc.filter.highpass_fir')
import scipy.signal
get_ipython().run_line_magic('pinfo', 'scipy.signal.lfilt')
get_ipython().run_line_magic('pinfo', 'scipy.signal.lfilter')
get_ipython().run_line_magic('pinfo', 'scipy.signal.butter')
b, a = scipy.signal.butter(3, freq)
get_ipython().run_line_magic('pinfo', 'scipy.signal.butter')
b, a = scipy.signal.butter(3, freq, analog=True)
get_ipython().run_line_magic('pinfo', 'scipy.signal.butter')
sos = signal.butter(10, 15, 'hp', fs=1000, output='sos')
get_ipython().run_line_magic('pinfo', 'scipy.signal.butter')
order = 512
ligo_data.delta_t
int(1 / ligo_data.delta_t)
1 / ligo_data.delta_t
1 / ligo_data.delta_t / 2
k = freq / float((int(1.0 / ligo_data.delta_t) / 2))
k
k = freq / (1 / ligo_data.delta_t) / 2
k
k = freq / ((1 / ligo_data.delta_t) / 2)
k
beta = 5.0
coeff = scipy.signal.firwin(order * 2 + 1, k, window=('kaiser', beta), pass_zero=False)
ligo_data
ligo_data.numpy()
npld = ligo_data.numpy()
hp_res = scipy.signal.lfilter(coeff, npld)
hp_res = scipy.signal.lfilter(coeff, 1.0, npld)
hp_res
np_res.shape
hp_res.shape
npld.shape
m
m.time
ligo_data.time_slice(m.time - 0.5, m.time + 0.5)
ligo_data.time_slice(m.time - 0.5, m.time + 0.5).shape
plt.plot(npld)
import matplotlib.pyplot as plt
plt.plot(npld)
plt.show()
ligo_data.time_slice
ligo_data.data
m.time
get_ipython().run_line_magic('pinfo', 'ligo_data.time_slice')
get_ipython().run_line_magic('pinfo2', 'ligo_data.time_slice')
ligo_data.start_time
m.time
start_idx = int((m.time - ligo_data.start_time) * ligo_data.sample_rate)
start_idx
start_idx = int((m.time - 0.5 - ligo_data.start_time) * ligo_data.sample_rate)
end_idx = int((m.time + 0.5 - ligo_data.start_time) * ligo_data.sample_rate)
ligo_data.sample_times
ligo_data.sample_times.numpy()
ligo_data.sample_times > start_idx
npld[start_idx:end_idx]
plt.plot(npld[start_idx:end_idx])
plt.show()
plt.ion()
plt.plot(npld[start_idx:end_idx])
plt.plot(hp_res[start_idx:end_idx])
plt.plot(hp_res[start_idx:end_idx])
get_ipython().run_line_magic('pinfo', 'ligo_data.whiten')
psd = ligo_data.psd(4)
hp_res
high_data = ligo_data.highpass_fir(15, 512)
hp_psd = high_data.psd(4)
plt.loglog(psd.sample_frequencies, psd)
plt.loglog(hp_psd.sample_frequencies, hp_psd)
plt.xlim(10, 2048)
plt.loglog(psd.sample_frequencies, psd)
plt.loglog(hp_psd.sample_frequencies, hp_psd)
plt.xlim(10, 2048)
get_ipython().run_line_magic('pinfo', 'ligo_data.whiten')
get_ipython().run_line_magic('pinfo2', 'ligo_data.whiten')
white = ligo_data.whiten(4)
white = ligo_data.whiten(4, 4)
plt.loglog(psd.sample_frequencies, psd)
white, wpsd = ligo_data.whiten(4, 4, return_psd=True)
plt.loglog(wpsd.sample_frequencies, wpsd)
plt.xlim(10, 2048)
get_ipython().run_line_magic('pinfo', 'ligo_data.psd')
get_ipython().run_line_magic('pinfo2', 'ligo_data.psd')
import pycbc.psd
get_ipython().run_line_magic('pinfo', 'pycbc.psd.welch')
get_ipython().run_line_magic('pinfo2', 'pycbc.psd.welch')
npld
get_ipython().run_line_magic('pinfo', 'ligo_data.psd')
get_ipython().run_line_magic('pinfo', 'pycbc.psd.welch')
npld.shape
npld.shape[0] / 4096
get_ipython().system('pip install scikit-image')
from skimage import util
M = 4096
step = 2048
slices = util.view_as_windows(npld, window_shape=(M,), step=100)
slices.shape
import numpy as np
win = np.hanning(M + 1)[:-1]
slices *= win
slices = slices.T
spectrum = np.fft.fft(slices, axis=0)[:M // 2 + 1: -1]
spectrum = np.abs(spectrum)
S = 20 * np.log10(S / np.max(S))
S = 20 * np.log10(spectrum / np.max(S))
S = 20 * np.log10(spectrum / np.max(spectrum))
plt.imshow(S, origin='lower', cmap='viridis')
ligo_data.sample_times.min()
ligo_data.sample_times.max()
freqs, times, Sx = scipy.signal.spectrogram(npld, fs=ligo_data.sample_rate, window="hanning", nperseg=4096, overlap=4096-100, detrend=False, scaling='spectrum')
freqs, times, Sx = scipy.signal.spectrogram(npld, fs=ligo_data.sample_rate, window="hanning", nperseg=4096, noverlap=4096-100, detrend=False, scaling='spectrum')
plt.pcolormesh(times, freqs, 10 * np.log10(Sx))
freqs, times, Sx = scipy.signal.spectrogram(npld, fs=ligo_data.sample_rate, window="hanning", nperseg=4096, noverlap=32, detrend=False, scaling='spectrum')
plt.pcolormesh(times, freqs, 10 * np.log10(Sx))
freqs, times, Sx = scipy.signal.spectrogram(npld, fs=ligo_data.sample_rate, window="hanning", nperseg=4096, noverlap=2048, detrend=False, scaling='spectrum')
plt.pcolormesh(times, freqs, 10 * np.log10(Sx))
freqs, times, Sx = scipy.signal.spectrogram(npld, fs=ligo_data.sample_rate, window="hanning", nperseg=4096, noverlap=4096, detrend=False, scaling='spectrum')
freqs, times, Sx = scipy.signal.spectrogram(npld, fs=ligo_data.sample_rate, window="hanning", nperseg=4096, noverlap=4096-100, detrend=False, scaling='spectrum')
plt.pcolormesh(times, freqs, 10 * np.log10(Sx))
freqs.shape
times.shape
Sx.shape
times
M = 2048
freqs, times, Sx = scipy.signal.spectrogram(npld, fs=ligo_data.sample_rate, window="hanning", nperseg=M, noverlap=M-100, detrend=False, scaling='spectrum')
plt.pcolormesh(times, freqs, 10 * np.log10(Sx))
npld
npld[start_idx:end_idx]
freqs, times, Sx = scipy.signal.spectrogram(npld[start_idx:end_idx], fs=ligo_data.sample_rate, window="hanning", nperseg=M, noverlap=M-100, detrend=False, scaling='spectrum')
plt.pcolormesh(times, freqs, 10 * np.log10(Sx))
M = 1024
freqs, times, Sx = scipy.signal.spectrogram(npld[start_idx:end_idx], fs=ligo_data.sample_rate, window="hanning", nperseg=M, noverlap=M-100, detrend=False, scaling='spectrum')
plt.pcolormesh(times, freqs, 10 * np.log10(Sx))
Sx
Sx.shape
plot(Sx.sum(axis=1))
plt.plot(Sx.sum(axis=1))
M = 4096
freqs, times, Sx = scipy.signal.spectrogram(npld[start_idx:end_idx], fs=ligo_data.sample_rate, window="hanning", nperseg=M, noverlap=M-100, detrend=False, scaling='spectrum')
plot(Sx.sum(axis=1))
plt.plot(Sx.sum(axis=1))
npld
get_ipython().run_line_magic('history', '')
get_ipython().run_line_magic('pinfo', 'signal.butter')
get_ipython().run_line_magic('pinfo', 'scipy.signal.butter')
get_ipython().run_line_magic('logstart', 'deobfusc_pycbc_log.py')
exit()
