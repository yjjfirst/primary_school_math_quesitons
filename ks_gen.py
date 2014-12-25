#!/usr/bin/python
import random
import sys
import getopt
from common import PAGE_MAX_QUESTIONS

class ks_generator:
  def generate_question(self):
    q = {}
    sum = random.randint(self.min_number, self.max_number)
    q['sum'] = sum
  #  print(sum)

    operand = random.randint(1, sum - 1)
    q['operand'] = operand
  #  print(operand_1)

    if (random.randint(0,1) == 0):
      operator = '+'
    else:
      operator = '-'
    q['operator'] = operator
  #  print (operator)

    return q
  
  def create_equation_string(self, q):
    eq_str = ''
    if (q['operator'] == '+'):
      eq_str = '%3d %s %3d =' % (q['operand'], q['operator'], q['sum'] - q['operand'])      
    else:
      eq_str = '%3d %s %3d =' % (q['sum'], q['operator'], q['operand'])
    return eq_str

  def create_output_file(self):
    quests = []
    equations = []

    for x in range(self.count):
      quests.append(self.generate_question())
    for x in range(self.count):
      equations.append(self.create_equation_string(quests[x]))
    for x in range (self.count):
      sys.stdout.write(equations[x] +";")

  def __init__(self, max_number, min_number, pages):
    self.max_number = max_number
    self.min_number = min_number
    self.count = pages * PAGE_MAX_QUESTIONS

def main(argv):
  max_num = 100
  min_num = 1
  pages = 1
  try:
    opts, args = getopt.getopt(argv, "m:n:p:", ["max=", "min=", "pages="])
  except getopt.GetoptError:
    print "ks_gen.py -i <inputfile> -o <outputfile>"
    sys.exit(2)
    
  for opt, arg in opts:
    if opt in ("-m", "--max"):
      max_num = int(arg)
    elif opt in ("-n", "--min"):
      min_num = int(arg)
    elif opt in ("-p", "--pages"):
      pages = int(arg)
#  print max_num, min_num, count
      
  ks = ks_generator(max_num, min_num, pages)
  ks.create_output_file()

if __name__ == "__main__":
  main(sys.argv[1:])
