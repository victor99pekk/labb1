from collections import deque
import sys
#import queue
# -*- coding: utf-8 -*-


class Algo:
    def __init__(self):
        self.contents = sys.stdin.read()
          

    def run(self):
         #Get the input in a good format
        a = self.contents
        Lines = a.splitlines()
        n = int(Lines[0])
        del Lines[0]
        array = Lines
        txt = ""


        txt=" ".join(Lines)
            

        array = [int(x) for x in txt.split()]        
        lines2 = [array[i*(n+1):i*(n+1)+1+n] for i in range(2*n)]

        students = []
        companies = []
        added = []
        for line in lines2:
            nbr = line[0]
            if nbr in added:
                line = line + [1]
                students.append(line) 
            else:
                companies.append(line)
                added.append(nbr)

       
        #copy of studentlist

        deq = deque()

        for i in range(len(students)):
            deq.append(students[i])

        #Map with pairs (company,student)
        pairs = {}
        for var in range(n+1):
            pairs[var] = None


        #create a list the index of every student

        """ inte klar !!
        indexList = [None]*(2*n)
        for company in companies:
            for i in range(1, len(company)):
                index = company[i]
                indexList[index] = i
        print(indexList)
             """

    
        
        #while loop until plist is empty
        while len(deq) != 0:

            #company is the company, and student is the student. 
            # CompanyNbr is the number of the company
            student = deq.pop()
            index = student[len(student)-1]
            companyNbr = student[index]


            #get the wanted company
            indexCompany = added.index(companyNbr)
            company = companies[indexCompany]
            student[n+1] += 1


            #if company is empty -> add student to company
            #"companyNbr not in pairs"
            if pairs.get(companyNbr) is None:
                pairs[companyNbr] = student
            

            #else if c prefers student over current applicant -> remove current pair and replace
            # add the old applicant to plist
            elif company[1:].index(student[0]) < company[1:].index((pairs[companyNbr])[0]):
            #elif 
                oldStudent = pairs[companyNbr]
                pairs[companyNbr] = student
                deq.append(oldStudent)
                
            #else -> add student to plist
            else:
                deq.append(student)
        

        #prints out the students
        for var in range(1, n+1):
            student = pairs.get(var)
            print(student[0])

      

      
if __name__ == '__main__':
    algo = Algo()
    algo.run()

