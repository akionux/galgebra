#!/usr/bin/env python

from sympy import symbols, Function
from sympy.galgebra.printing import xdvi
from sympy.galgebra.ga import *

Format()

X = (x1,x2,x3) = symbols('1 2 3')
metric = '1 0 0,'+ \
         '0 1 0,'+ \
         '0 0 1,'
(e_1,e_2,e_3,grad) = MV.setup('e_1 e_2 e_3',metric=metric,coords=X)
f = MV('f','scalar',fct=True)
V = MV('V','vector',fct=True)
B = MV('B','bivector',fct=True)
T = MV(base='T,3',mvtype='grade',fct=True)
A = MV('A','mv')

print r'\text{Geometric Algebra on 3-dimensional Euclidean space}'

print r'\text{metric}'
print r'g_{ij} =',MV.metric

print r'\text{base}'
print r'\bm{e_1*e_2*e_3} =',e_1*e_2*e_3
print r'\star(\bm{e_1*e_2*e_3}) = (\bm{e_1*e_2*e_3})*(\bm{e_1*e_2*e_3}) =',e_1*e_2*e_3*e_1*e_2*e_3

print r'\text{Scalar(0-vector)}'
print r'\bm{f} =',f
print r'grad*\bm{f} =',grad*f
print r'grad|\bm{f} =',grad|f
print r'grad^\bm{f} =',grad^f
print r'\star \bm{f} =',f*e_1*e_2*e_3

print r'\text{Vector(1-vector)}'
print r'\bm{V} =',V
print r'grad*\bm{V} =',grad*V
print r'grad|\bm{V} =',grad|V
print r'grad^\bm{V} =',grad^V
print r'\star \bm{V} =',V*e_1*e_2*e_3

print r'\text{Bivector(2-vector)}'
print r'\bm{B} =',B
print r'grad*\bm{B} =',grad*B
print r'grad|\bm{B} =',grad|B
print r'grad^\bm{B} =',grad^B
print r'\star \bm{B} =',B*e_1*e_2*e_3

print r'\text{Pseudo-Scalar(3-vector)}'
print r'\bm{T} =',T
print r'grad*\bm{T} =',grad*T
print r'grad|\bm{T} =',grad|T
print r'grad^\bm{T} =',grad^T
print r'\star \bm{T} =',T*e_1*e_2*e_3

print r'\text{Multi Vector}'
print r'\bm{A} =',A
print r'grad*\bm{A} =',grad*A
print r'grad|\bm{A} =',grad|A
print r'grad^\bm{A} =',grad^A
print r'\star \bm{A} = \bm{A}*\bm{e_1*e_2*e_3} =',A*(e_1*e_2*e_3)
#print r'grad|\bm{A} =',grad|A
#print r'grad*\bm{A} =',grad*A
#A.Fmt(2,r'\bm{A}')
#A.Fmt(3,r'\bm{A}')

xdvi()
