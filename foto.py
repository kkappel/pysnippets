#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (c) 2015 by Klaus Kappel

from PIL import Image
import glob
import os

size = 128, 128

for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(file + "-tn.jpg", "JPEG")

