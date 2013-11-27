import sys
from pdfminer.pdfparser import PDFDocument, PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter, process_pdf
from pdfminer.pdfdevice import PDFDevice, TagExtractor
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams
import os
 
# main
def main(outfile, fname):
    # debug option
    debug = 0
    # input option
    password = ''
    pagenos = set()
    maxpages = 0
    # output option
    outtype = 'text'
    layoutmode = 'normal'
    codec = 'utf-8'
    pageno = 1
    scale = 1
    caching = True
    showpageno = True
    laparams = LAParams()
 
    PDFDocument.debug = debug
    PDFParser.debug = debug
    CMapDB.debug = debug
    PDFResourceManager.debug = debug
    PDFPageInterpreter.debug = debug
    PDFDevice.debug = debug
 
    rsrcmgr = PDFResourceManager(caching=caching)
    outtype = 'text'
    if outfile:
        outfp = file(outfile, 'w')
    else:
        outfp = sys.stdout
    if outtype == 'text':
        device = TextConverter(rsrcmgr, outfp, codec=codec, laparams=laparams)
 
    fp = file(fname, 'rb')
    process_pdf(rsrcmgr, device, fp, pagenos, maxpages=maxpages, 
                password=password, caching=caching, 
                check_extractable=True)
    fp.close()
    device.close()
    outfp.close()
    print maxpages
 
indir = '/Users/mattstringer/Dropbox/ProyectoLaCumbre/DataClean/pdfs'
for root, dirs, filenames in os.walk(indir):
    for fname in filenames:
        print fname
        if (fname.endswith(".pdf")):
            main(os.path.join(root, fname) + ".txt", os.path.join(root, fname))