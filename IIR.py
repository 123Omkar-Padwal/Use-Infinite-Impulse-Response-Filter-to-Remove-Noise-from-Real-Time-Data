import numpy as np
from scipy import signal
import numpy as np
class IIR2_filter:
  """2nd order IIR filter"""
  def __init__(self,s):
    """Instantiates a 2nd order IIR filter
    s -- numerator and denominator coefficients
    """
    self.numerator0 = s[0]
    self.numerator1 = s[1]
    self.numerator2 = s[2]
    self.denominator1 = s[4]
    self.denominator2 = s[5]
    self.buffer1 = 0
    self.buffer2 = 0
  def filter(self,v):
    """Sample by sample filtering
    v -- scalar sample
    returns filtered sample
    """
    input = v - (self.denominator1 * self.buffer1) - (self.denominator2 * self.buffer2)
    output = (self.numerator1 * self.buffer1) + (self.numerator2 * self.buffer2) + input * self.numerself.buffer2 = self.buffer1
    self.buffer1 = input
    return output
  def lowPassTest(self, s, input):
    x_sos_filt = np.round(signal.sosfilt(s, input), 2)
    x_iir2_filt = []
    for i in input:
      x_iir2_filt.append(np.round(self.filter(i), 2))
    print("Low Pass Filter O/P SOSFilt= ", x_sos_filt)
    print("Low Pass Filter O/P IIR2 = ", x_iir2_filt)
    try:
      if np.testing.assert_equal(x_iir2_filt, x_sos_filt, err_msg=’Not matching’, verbose=True) ==return "Test Successfull. IIR filter performing as expected."
    except AssertionError:
      return "Test Unsuccessfull. IIR filter not performing as expected."
  def bandPassTest(self, s, input):
    x_sos_filt = np.round(signal.sosfilt(s, input), 2)
    x_iir2_filt = []
    for i in input:
      x_iir2_filt.append(np.round(self.filter(i), 2))
    print("Band Pass Filter O/P SOSFilt= ", x_sos_filt)
    print("Band Pass Filter O/P IIR2 = ", x_iir2_filt)
    try:
      if np.testing.assert_equal(x_iir2_filt, x_sos_filt, err_msg=’Not matching’, verbose=True) ==return "Test Successfull. IIR filter performing as expected."
    except AssertionError:
      return "Test Unsuccessfull. IIR filter not performing as expected."
  def bandStopTest(self, s, input):
    x_sos_filt = np.round(signal.sosfilt(s, input), 2)
    x_iir2_filt = []
    for i in input:
      x_iir2_filt.append(np.round(self.filter(i), 2))
    print("Band Stop Filter O/P SOSFilt= ", x_sos_filt)
    print("Band Stop Filter O/P IIR2 = ", x_iir2_filt)
    try:
      if np.testing.assert_equal(x_iir2_filt, x_sos_filt, err_msg=’Not matching’, verbose=True) ==return "Test Successfull. IIR filter performing as expected."
    except AssertionError:
      return "Test Unsuccessfull. IIR filter not performing as expected."
  def highPassTest(self, s, input):
    x_sos_filt = np.round(signal.sosfilt(s, input), 2)
    x_iir2_filt = []
    for i in input:
      x_iir2_filt.append(np.round(self.filter(i), 2))
    print("High Pass Filter O/P SOSFilt= ", x_sos_filt)
    print("High Pass Filter O/P IIR2 = ", x_iir2_filt)
    try:
      if np.testing.assert_equal(x_iir2_filt, x_sos_filt, err_msg=’Not matching’, verbose=True) ==return "Test Successfull. IIR filter performing as expected."
    except AssertionError:
      return "Test Unsuccessfull. IIR filter not performing as expected."
  def chainTestIIR(self, input):
    x_iir_filt = []
    for i in input:
      x_iir_filt.append(np.round(self.filter(i), 2))
    return x_iir_filt
class IIR_filter:
  """IIR filter"""
  def __init__(self,sos):
    """Instantiates an IIR filter of any order
    sos -- array of 2nd order IIR filter coefficients
    """
    self.cascade = []
    for s in sos:
      self.cascade.append(IIR2_filter(s))
  def filter(self,v):
    """Sample by sample filtering
    v -- scalar sample
    returns filtered sample
    """
    for f in self.cascade:
    v = f.filter(v)
    return v
    def lowPassTest(self, s, input):
    x_sos_filt = np.round(signal.sosfilt(s, input), 2)
    x_iir_filt = []
    10
    for i in input:
    x_iir_filt.append(np.round(self.filter(i), 2))
    print("Low Pass Filter O/P SOSFilt= ", x_sos_filt)
    print("Low Pass Filter O/P IIR = ", x_iir_filt)
    try:
    if np.testing.assert_equal(x_iir_filt, x_sos_filt, err_msg=’Not matching’, verbose=True) == Nreturn "Test Successfull. IIR filter performing as expected."
    except AssertionError:
    return "Test Unsuccessfull. IIR filter not performing as expected."
  def bandPassTest(self, s, input):
    x_sos_filt = np.round(signal.sosfilt(s, input), 2)
    x_iir_filt = []
    for i in input:
      x_iir_filt.append(np.round(self.filter(i), 2))
    print("Band Pass Filter O/P SOSFilt= ", x_sos_filt)
    print("Band Pass Filter O/P IIR = ", x_iir_filt)
    try:
      if np.testing.assert_equal(x_iir_filt, x_sos_filt, err_msg=’Not matching’, verbose=True) == Nreturn "Test Successfull. IIR filter performing as expected."
    except AssertionError:
      return "Test Unsuccessfull. IIR filter not performing as expected."
  def bandStopTest(self, s, input):
    x_sos_filt = np.round(signal.sosfilt(s, input), 2)
    x_iir_filt = []
    for i in input:
      x_iir_filt.append(np.round(self.filter(i), 2))
    print("Band Stop Filter O/P SOSFilt= ", x_sos_filt)
    print("Band Stop Filter O/P IIR = ", x_iir_filt)
    try:
      if np.testing.assert_equal(x_iir_filt, x_sos_filt, err_msg=’Not matching’, verbose=True) == Nreturn "Test Successfull. IIR filter performing as expected."
    except AssertionError:
      return "Test Unsuccessfull. IIR filter not performing as expected."
  def highPassTest(self, s, input):
    x_sos_filt = np.round(signal.sosfilt(s, input), 2)
    x_iir_filt = []
    for i in input:
      x_iir_filt.append(np.round(self.filter(i), 2))
    print("High Pass Filter O/P SOSFilt= ", x_sos_filt)
    print("High Pass Filter O/P IIR = ", x_iir_filt)
    try:
      if np.testing.assert_equal(x_iir_filt, x_sos_filt, err_msg=’Not matching’, verbose=True) == Nreturn "Test Successfull. IIR filter performing as expected."
    except AssertionError:
      return "Test Unsuccessfull. IIR filter not performing as expected."
  def chainTestIIR(self, input):
    x_iir_filt = []
    for i in input:
      x_iir_filt.append(np.round(self.filter(i), 2))
    return x_iir_filt
