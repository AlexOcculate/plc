from pdfminer.pdfparser import PDFParser, PDFDocument, PDFNoOutlines, PDFSyntaxError
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure, LTImage, LTTextLineHorizontal, LTTextBoxHorizontal, LTChar, LTRect, LTLine, LTAnon
from binascii import b2a_hex
from operator import itemgetter



cin = StringIO.StringIO()
cin.write(pdfbin)
cin.seek(0)

parser = PDFParser(cin)
doc = PDFDocument()
parser.set_document(doc)
doc.set_parser(parser)

doc.initialize("")
rsrcmgr = PDFResourceManager()
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)

for n, page in enumerate(doc.get_pages()):
    interpreter.process_page(page)
    layout = device.get_result()
    ParsePage(layout)

xset, yset = set(), set()
tlines = [ ]
objstack = list(reversed(layout._objs))
while objstack:
    b = objstack.pop()
    if type(b) in [LTFigure, LTTextBox, LTTextLine, LTTextBoxHorizontal]:
        objstack.extend(reversed(b._objs))  # put contents of aggregate object into stack
    elif type(b) == LTTextLineHorizontal:
        tlines.append(b)
    elif type(b) == LTLine:
        if b.x0 == b.x1:
            xset.add(b.x0)
        elif b.y0 == b.y1:
            yset.add(b.y0)
        else:
            print "sloped line", b
    elif type(b) == LTRect: 
        if b.x1 - b.x0 < 2.0:
            xset.add(b.y0)
        else:
            yset.add(b.x0)
    else:
        assert False, "Unrecognized type: %s" % type(b)