#!/usr/bin/env python

from sympy.galgebra.printing import xdvi
from sympy.galgebra.ga import *

Format()

#X = (x,y,z) = symbols('x_1 x_2 x_3')
metric = '1 0 0,'+ \
         '0 1 0,'+ \
         '0 0 1,'
(e_1,e_2,e_3) = MV.setup('e_1 e_2 e_3',metric=metric)
A = MV('A','mv')

print r'g_{ij} =',MV.metric
print r'\bm{A} =',A
print r'\star \bm{A} = \bm{A}*(\bm{e}_1*\bm{e}_2*\bm{e}_3) =',A*(e_1*e_2*e_3)
#print r'grad|\bm{A} =',grad|A
#print r'grad*\bm{A} =',grad*A
#A.Fmt(2,r'\bm{A}')
#A.Fmt(3,r'\bm{A}')

xdvi()
