#!/usr/bin/python
import sys
from common import PAGE_MAX_QUESTIONS

def generate_header():
  print "\documentclass[12pt,notitlepage,a4paper]{article}"
  print "\\begin{document}"

def generate_tail():
  print "\end{document}"

def generate_newpage():
  print "\\newpage"

def generate_one_page(qs):
  i = 0
  print "{\\LARGE"
  print "\\begin{tabular}{| l| l| l|}"
  print "\\hline"
  for q in qs:   	  
    print "{0}\\_\\_\\_\\_".format(q),
    if i%3 == 2:
      print "\\\\  \\hline"
    else:
      print "&",
    i = i+1
  if i%3 != 0:
    print "\\\\",
    print "\\hline"
  print "\n\\end{tabular}"
  print "}"

questions_line = sys.stdin.readline()
questions_line = questions_line[:-1]
questions =  questions_line.split(';')

generate_header()

pages = len(questions)/PAGE_MAX_QUESTIONS
for i in range(0, pages):
  generate_one_page(questions[i*PAGE_MAX_QUESTIONS:(i+1)*PAGE_MAX_QUESTIONS])
  generate_newpage()

generate_tail()

