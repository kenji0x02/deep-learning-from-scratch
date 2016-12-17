# coding: utf-8
import sys, os
sys.path.append(os.curdir)
from common.util import im2col
import numpy as np

# 7.4.3 Convolutionレイヤの実装よりim2colの例
x1 = np.random.rand(1, 3, 7, 7)
col1 = im2col(x1, 5, 5, stride=1, pad=0)
print(col1.shape)

x2 = np.random.rand(10, 3, 7, 7)
col1 = im2col(x2, 5, 5, stride=1, pad=0)
print(col1.shape)