# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 22:37:27 2021

@author: Brahian
"""

from numpy import matrix,zeros,size
from numpy.linalg import det

A=matrix([[-2,-6,2],[0,1,3],[0,0,6]])
MC=matrix(zeros((3,3))) # Matriz de cofactores
idx=matrix(range(3))
for i in range(size(A,0)):
    for j in range(size(A,1)):
        fix=idx[idx!=i]
        cox=idx[idx!=j]
        cof=A[[[fix[0,0]],[fix[0,1]]],cox]
        MC[i,j]=pow(-1,i+j)*det(cof)

MACJ=MC.transpose() # Matriz adjunta 
print ("Matriz de cofactores\n",MC)
print ("Matriz adjunta\n",MACJ)