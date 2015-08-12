#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (c) 2015 by Klaus Kappel

from ID3 import *

fn = '/media/kkappel/3d89ef03-190d-4d5a-8855-1860aac881f5/Spielfilme/Der_Mann_mit_dem_goldenen_Arm_2015-08-05_2315_323458.mp4'


try:
  id3info = ID3(fn)
  print id3info
  for k, v in id3info.items():
    print k, ":", v
except InvalidTagError, message:
  print "Invalid ID3 tag:", message
