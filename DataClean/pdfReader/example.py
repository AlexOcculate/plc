#!/usr/bin/env python
#coding: utf8 
import os
import glob

from nltk.corpus import cess_esp as cess
import nltk, re, pprint
from nltk import UnigramTagger as ut

import string
import cPickle as pickle
from collections import defaultdict

import pdfminer

print pdfminer.__version__



file_path = '/Users/mattstringer/Dropbox/ProyectoLaCumbre/DataClean/pdfs/example_finca.pdf'

DIRECTORY = '/Users/mattstringer/Dropbox/ProyectoLaCumbre/DataClean/pdfs'
os.chdir(DIRECTORY)
text_files = [DIRECTORY + "/" + files for files in glob.glob("*.pdf")]

def convert_pdf(path):
    from pdfminer.pdfparser import PDFDocument, PDFParser
    from pdfminer.pdfinterp import PDFResourceManager, process_pdf, PDFPageInterpreter
    from pdfminer.converter import TextConverter
    from pdfminer.layout import LAParams
    from cStringIO import StringIO
    from pdfminer.converter import PDFPageAggregator


    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()




    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)


    fp = file(path, 'rb')
    parser = PDFParser(fp)


    process_pdf(rsrcmgr, device, fp)

    fp.close()
    device.close()

    text_str = retstr.getvalue()
    retstr.close()
    serialize_object(text_str, 'corpus.pkl')
    tokenized_text = tonkenier(text_str)

    serialize_object(tokenized_text, 'tokenized_corpus.pkl')
    return tokenized_text


def serialize_object(obj,filename):
    pkl_file = open(filename, 'wb')
    pickle.dump(obj, pkl_file)
    pkl_file.close()


def tonkenier(text):
    cess_sents = cess.tagged_sents()
    uni_tag = ut(cess_sents)
    words = text.replace(",", "").replace(".", "").replace("\n", "").replace("\t", "").split(" ")
    annotated_text = uni_tag.tag(words)
    return annotated_text


def main():
    x = None
    if os.path.isfile("tokenized_corpus.pkl") == False:
        text = convert_pdf(file_path)
    else:
        print 'loading from pickle file ....'
        text = pickle.load(open("corpus.pkl", "rb"))
        tokenized_text = pickle.load(open("tokenized_corpus.pkl", "rb"))



        for i, word in enumerate(tokenized_text):

            if 'Latitud:' in word[0]:
                lat = tokenized_text[i+4][0] + tokenized_text[i+5][0]
                print lat

            if 'Longitud:' in word[0]:
                lat = tokenized_text[i+4][0] + tokenized_text[i+5][0]
                print lat


        words = defaultdict(list)


        for i in tokenized_text:
            if i[1]  != None:
                words[i[1]].append(i[0])




        # for key, value in words.items():
        #     print key, value






        




if __name__ == '__main__':
    main()
    print "done."
