import sys
import PyPluMA
import PyIO

class CSVJoinPlugin:
 def input(self, inputfile):
  self.parameters = PyIO.readParameters(inputfile)
 def run(self):
     pass
 def output(self, outputfile):
  infile1 = open(PyPluMA.prefix()+"/"+self.parameters["csv1"], 'r')
  infile2 = open(PyPluMA.prefix()+"/"+self.parameters["csv2"], 'r')

  firstline = infile1.readline().strip()
  firstcontents = firstline.split(',')

  infile2.readline()
  mylist = []
  for line in infile2:
    line = line.strip()
    contents2 = line.split(',')
    mylist.append(contents2[0])

  keep = [1]
  newfirstcontents = []
  for i in range(len(firstcontents)):
    if (firstcontents[i] in mylist):
        newfirstcontents.append(firstcontents[i])
        keep.append(1)
    else:
        keep.append(0)
  
  outfile = open(outputfile, 'w')
  for i in range(len(newfirstcontents)):
     outfile.write(newfirstcontents[i])
     if (i != len(newfirstcontents)-1):
         outfile.write(',')
     else:
         outfile.write('\n')

  for line in infile1:
    contents3 = line.strip().split(',')
    element = contents3[0]
    if (element in mylist):
        contents4 = []
        for i in range(len(contents3)):
            if (keep[i] == 1):
                contents4.append(contents3[i])
        for i in range(len(contents4)):
            outfile.write(contents4[i])
            if (i != len(contents4)-1):
                outfile.write(',')
            else:
                outfile.write('\n')
