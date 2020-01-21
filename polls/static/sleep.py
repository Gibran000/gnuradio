#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2018 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr
from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import ieee802_11
import rftap
import sip
import sys
import time
import pmt

class sleep(gr.sync_block,gr.top_block, Qt.QWidget,Range):
    """
    docstring for block sleep
    """
    
    def __init__(self,schedule):
		#self.uhd_usrp_sink_0.set_normalized_gain(rx_gain, 0)
		self.schedule=schedule
		#self.gain = gain = 0.75
		gr.sync_block.__init__(self,
            name="sleep",
            in_sig=[numpy.complex64],#cambiar entrada por un tipo pmt header (SYNC y RTS) int8 quiza
            out_sig=[numpy.complex64])
    
    def get_gain(self):
        return self.__gain

    def set_gain(self, gain):
        self.__gain = gain
        self.__uhd_usrp_source_0.set_normalized_gain(self.gain, 0)
            
    def start_zzz(self,muestras):

    	if self.schedule==0:
    		time.sleep(5)
    		#setg=self.set_gain.__gain(0)
    		#print(get_gain.__gain())
    		#checa la cabecera (rftap, compara si es el primer horario y se va a dormir)
    		#RangeWidget.Slider(None, self.var_rx_r, self.var_rx_g, float).changed(0.0)
    		print("primer schedule")
        	time.sleep(self.schedule)
    		#RangeWidget.Slider(None, self.var_rx_r, self.var_rx_g, float).changed(0.9)
    		print("segundo schedule")
    		return muestras
    		
    	else:
    		#RangeWidget.Slider(None, self.var_rx_r, self.var_rx_g, float).changed(0.0)
    		print("Periodo de sensado")
    		time.sleep(self.schedule)
    		#setg=self.set_gain.__gain(0)
    		#print(get_gain.__gain())
    		#RangeWidget.Slider(None, self.var_rx_r, self.var_rx_g, float).changed(0.9)
    		print(muestras)
    		return 1


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        for i in range(0,len(in0)):
        	muestras=in0[i]
        	out[i] = self.start_zzz(muestras)
        	#print("out: ",out)
        return len(output_items[0])
        


