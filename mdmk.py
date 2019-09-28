import sys
import argparse
from subprocess import check_output
from os import path
from time import sleep

parser = argparse.ArgumentParser(description="")
parser.add_argument("-pdf_engine",default="xelatex")
parser.add_argument("-highlight_style",default="zenburn")
parser.add_argument("-urlcolor",default="NavyBlue")
parser.add_argument("-file",default=None)
parser.add_argument("-o",default=None)
parser.add_argument("-CJKmainfont",default="Kai")
#parser.add_argument("-mainfont",default="")
parser.add_argument("-geometry",default='top=2cm, bottom=1.5cm, left=2cm, right=2cm')
parser.add_argument("-per",type=int,default=5)

args = parser.parse_args()

if args.file is None:
    raise Exception("No file specified")

if args.o is None:
    outpath = args.file[:-2]+"pdf"
else:
    outpath = args.o

#command = ['pandoc','--pdf-engine='+args.pdf_engine,'--highlight-style',args.highlight_style,'-V','colorlinks','-V','urlcolor='+args.urlcolor,'-V','CJKmainfont="'+args.CJKmainfont+'"','-V','geometry:"'+args.geometry+'"',args.file,'-o',outpath]
command = ['pandoc','--pdf-engine='+args.pdf_engine,'--highlight-style',args.highlight_style,'-V','colorlinks','-V','urlcolor='+args.urlcolor,'-V','CJKmainfont="'+args.CJKmainfont+'"','-V geometry:'+'"'+args.geometry+'"',args.file,'-o',outpath]

timestamp = path.getmtime(args.file)
timestampp = None
while True:
    if timestampp != timestamp:
        print("Generate pdf file")
        timestamp = timestampp
        check_output(command)
    sleep(args.per)
    timestampp = path.getmtime(args.file)
