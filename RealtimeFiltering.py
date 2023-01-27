#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import webcam2rgb
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy import signal
from scipy.fft import fft, ifft
import iir_filter
import time
class RealtimePlotWindow:
def __init__(self, channel: str):
    # create a plot window
    self.fig, self.ax = plt.subplots()
    plt.title(f"Channel: {channel}")
    self.title = self.ax.text(0.5,0.85, "", bbox={’facecolor’:’w’, ’alpha’:0.5, ’pad’:5},
    transform=self.ax.transAxes, ha="center")
    # that’s our plotbuffer
    self.plotbuffer = np.zeros(500)
    # create an empty line
    self.line, = self.ax.plot(self.plotbuffer)
    # axis
    self.ax.set_ylim(0, 1)
    # That’s our ringbuffer which accumluates the samples
    # It’s emptied every time when the plot window below
    # does a repaint
    self.ringbuffer = []
    # add any initialisation code here (filters etc)
    # start the animation
    self.ani = animation.FuncAnimation(self.fig, self.update, interval=100)
    # updates the plot
def update(self, data):
    # add new data to the buffer
    self.plotbuffer = np.append(self.plotbuffer, self.ringbuffer)
    # only keep the 500 newest ones and discard the old ones
    self.plotbuffer = self.plotbuffer[-500:]
    self.ringbuffer = []
    # set the new 500 points of channel 9
    self.line.set_ydata(self.plotbuffer)
    self.ax.set_ylim(0, max(self.plotbuffer)+1)
    return self.line,
    # appends data to the ringbuffer
def addData(self, v, sr, flag):
    self.ringbuffer.append(v)
    self.title.set_text(f"{flag} | Sampling Rate: {round(sr, 2)}")
    realtimePlotWindowRedOg = RealtimePlotWindow("Red (Original)")
    realtimePlotWindowBlueOg = RealtimePlotWindow("Blue (Original)")
    realtimePlotWindowGreenOg = RealtimePlotWindow("Green (Original)")
    realtimePlotWindowBlue = RealtimePlotWindow("Blue (Filtered)")

    realtimePlotWindowGreen = RealtimePlotWindow("Green (Filtered)")
    realtimePlotWindowRed = RealtimePlotWindow("Red (Filtered)")
    redd = []
    greenn = []
    bluee = []
    reddf = []
    greennf = []
    blueef = []
    #sos1 = signal.butter(2, [0.4, 1], ’bandpass’, fs=30, output=’sos’) #band pass
    sos2 = sos1 = signal.butter(2, [1, 4], ’bandpass’, fs=30, output=’sos’) #band pass
    #iir1 = iir_filter.IIR2_filter(sos1[0])
    iir2 = iir_filter.IIR2_filter(sos2[0])
    start_time = time.time()
def create_wavelet(N, fs):
    duration = N / fs
    t = np.linspace(-duration/2, duration/2, N)
    wavelet = np.sinc(t*fs)
    return wavelet
    wavelet = create_wavelet(30, 30)
    iir3 = iir_filter.IIR2_filter(wavelet)
def detect_ambulance(rf, bf, gf):
    if rf > 0.2 or bf > 0.2:
    return "Ambulance Light Detected"
    else:
    return "Ambulance Light Not Detected"
    #create callback method reading camera and plotting in windows
def hasData(retval, data):
    b = data[0]
    g = data[1]
    r = data[2]
    dataF = iir2.filter(data) #Band pass Filtering the input signal
    dataFR = iir3.filter(dataF) #Adding wavelet to detect peaks
    dataFR = dataFR * dataFR #squaring to remove noise
    bf = dataFR[0]
    gf = dataFR[1]
    rf = dataFR[2]
    flag = detect_ambulance(rf, bf, gf)
    redd.append(r)
    elapsed_time = time.time() - start_time #tracking elapsed time to check sampling rate
    sr = len(redd)/elapsed_time #ACTUAL SAMPLING RATE OF THE CAMERA
    realtimePlotWindowRedOg.addData(r, sr, flag)
    realtimePlotWindowBlueOg.addData(b, sr, flag)
    realtimePlotWindowGreenOg.addData(g, sr, flag)
    realtimePlotWindowBlue.addData(bf, sr, flag)
    realtimePlotWindowGreen.addData(gf, sr, flag)
    realtimePlotWindowRed.addData(rf, sr, flag)
    #create instances of camera
    camera = webcam2rgb.Webcam2rgb()
    #start the thread and stop it when we close the plot windows
    camera.start(callback = hasData, cameraNumber=0, directShow = True)

    print("camera samplerate: ", camera.cameraFs(), "Hz")
    plt.show()
    camera.stop()
    print(’finished’)
