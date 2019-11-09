#
# Copyright 2008,2009 Free Software Foundation, Inc.
#
# This application is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This application is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

# The presence of this file turns this directory into a Python package

'''
gr-satellites deframer components

The deframers transform soft symbols into frames, detecting packet
boundaries and performing error correction and checking as needed.

The input to these hierarchical blocks is a stream of soft symbols
and the output are PDUs with the frames. 
'''

from .astrocast_fx25_deframer import astrocast_fx25_deframer
from .ax100_deframer import ax100_deframer
from .ax25_deframer import ax25_deframer
from .sat_3cat_1_deframer import sat_3cat_1_deframer
