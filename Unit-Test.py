import iir_filter
from scipy import signal
import numpy as np
class IIRTest:
fs = 250
fc = 10
input = [-1.0, 0.5, 1.0]
def lowPassTest(self):
  print("Commencing low pass unit test for the filters!")
  sos = signal.butter(1, self.fc, fs = self.fs, output=’sos’)
  iir1 = iir_filter.IIR_filter(sos)
  iir2 = iir_filter.IIR2_filter(sos[0])
  print(iir1.lowPassTest(sos, self.input))
  print(iir2.lowPassTest(sos, self.input))
  print("low pass test ended!")
def bandPassTest(self):
  print("Commencing band pass unit test for the filters!")
  sos = signal.butter(1, [6, 8], fs = self.fs, btype=’bandpass’, output=’sos’)
  iir1 = iir_filter.IIR_filter(sos)
  iir2 = iir_filter.IIR2_filter(sos[0])
  print(iir1.bandPassTest(sos, self.input))
  print(iir2.bandPassTest(sos, self.input))
def bandStopTest(self):
  print("Commencing band stop unit test for the filters!")
  sos = signal.butter(1, [6, 8], fs = self.fs, btype=’bandstop’, output=’sos’)
  iir1 = iir_filter.IIR_filter(sos)
  iir2 = iir_filter.IIR2_filter(sos[0])
  print(iir1.bandStopTest(sos, self.input))
  print(iir2.bandStopTest(sos, self.input))
def highPassTest(self):
  print("Commencing high pass unit test for the filters!")
  sos = signal.butter(1, self.fc, fs = self.fs, btype=’highpass’, output=’sos’)
  iir1 = iir_filter.IIR_filter(sos)
  iir2 = iir_filter.IIR2_filter(sos[0])
  print(iir1.highPassTest(sos, self.input))
  print(iir2.highPassTest(sos, self.input))
def chainTestIIR(self):
  sos1 = signal.butter(1, self.fc, fs = self.fs, output=’sos’)
  sos2 = signal.butter(1, 4, fs = self.fs, btype=’highpass’, output=’sos’)
  sos3 = signal.butter(1, [6, 8], fs = self.fs, btype = ’bandstop’, output=’sos’)
  x_sos_filt = np.round(signal.sosfilt(sos3, signal.sosfilt(sos2, signal.sosfilt(sos1, self.input))iir1_1 = iir_filter.IIR_filter(sos1)
  iir1_2 = iir_filter.IIR_filter(sos2)
  iir1_3 = iir_filter.IIR_filter(sos3)
  iir2_1 = iir_filter.IIR2_filter(sos1[0])
  iir2_2 = iir_filter.IIR2_filter(sos2[0])
  iir2_3 = iir_filter.IIR2_filter(sos3[0])
  x_iir1_filt = iir1_3.chainTestIIR(iir1_2.chainTestIIR(iir1_1.chainTestIIR(self.input)))
  x_iir2_filt = iir2_3.chainTestIIR(iir2_2.chainTestIIR(iir2_1.chainTestIIR(self.input)))
  print("Chain Butterworth Filter O/P SOSFilt= ", x_sos_filt)
  print("Chain IIR Filter O/P = ", x_iir1_filt)
  print("Chain 2nd order IIR Filter O/P = ", x_iir2_filt)
  try:
    if np.testing.assert_equal(x_iir1_filt, x_sos_filt, err_msg=’Not matching’, verbose=True) ==print("Test Successfull. IIR filter chain performing as expected.")
  except AssertionError:
    print("Test Unsuccessfull. IIR filter chain not performing as expected.")
  try:
    if np.testing.assert_equal(x_iir1_filt, x_sos_filt, err_msg=’Not matching’, verbose=True) ==print("Test Successfull. IIR filter chain performing as expected.")
  except AssertionError:
    print("Test Unsuccessfull. IIR filter chain not performing as expected.")
iirTest = IIRTest()
iirTest.lowPassTest()
iirTest.bandPassTest()
iirTest.bandStopTest()
iirTest.highPassTest()
iirTest.chainTestIIR()
