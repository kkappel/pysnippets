#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (c) 2015 by Klaus Kappel

SRC='/media/kkappel/Seagate Expansion Drive/'
SRC=u'/home/kkappel/Videos/'

import glob
import shutil
from os import path
from hachoir_core.error import HachoirError
from hachoir_core.cmd_line import unicodeFilename
from hachoir_parser import createParser
from hachoir_core.tools import makePrintable
from hachoir_metadata import extractMetadata
from hachoir_core.i18n import getTerminalCharset
from sys import argv, stderr, exit
from hurry.filesize import size


a = []

def ReadMpeg4(fn):
    # filename = unicodeFilename(fn)
    realname = fn
    parser = createParser(realname)
    print fn
    try:
        metadata = extractMetadata(parser)
        text = metadata.exportPlaintext()
        w = metadata.get('width')
        h = metadata.get('height')
        dim = '%dx%dpx' % (w, h) 
        d = metadata.get('duration')
        pt = int(d.total_seconds() / 60.0)        
        fsize = size(path.getsize(fn))
        print (dim, pt, fsize)

    except HachoirError, err:
        print "Metadata extraction error: %s" % unicode(err)
        w = h = d = 0



def ReadExif(fn):
    print fn
    import exifread
    f = open(fn, 'rb')
    tags = exifread.process_file(f)
    for tag in tags.keys():
        if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
            print "Key: %s, value %s" % (tag, tags[tag])


def ReadId3(fn):
    import mutagen
    f = mutagen.File(fn, options=None, easy=False)
    print f.StreamInfo()
    print f.Metadata()


for fn in glob.iglob(path.join(SRC, "*")):
    ext = fn[-3:]
    ext = ext.lower()
    if ext == 'mp4':
        ReadMpeg4(fn)
    elif ext == 'jpg':
        ReadExif(fn)
    elif ext == 'mp3':
        ReadId3(fn)

