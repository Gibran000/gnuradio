
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

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from sleep import sleep
import numpy, pmt

class qa_sleep (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # set up fg
        muestras=True
        src_data=([1.01+0j,1.01+0j])
        expected_data=[1,1]
        #print("src: ",src_data)
        src=blocks.vector_source_c(src_data)      
        sqr=sleep(5)
        dst=blocks.vector_sink_c()
        self.tb.connect(src,sqr)
        self.tb.connect(sqr,dst)
        self.tb.run ()
        result_data=dst.data()
        self.assertFloatTuplesAlmostEqual(expected_data,result_data,4)
        print("el horario siguiente es: ",expected_data[0])
        # check data


if __name__ == '__main__':
    gr_unittest.run(qa_sleep, "qa_sleep.xml")
