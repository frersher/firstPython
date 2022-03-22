import os
from os import path

# 当前位置的绝对路径
print(path.abspath('.'))
# 当前位置上一个路径的绝对路径
print(path.abspath('..'))

# 判断某个路径是否存在
print(path.exists('/Users'))

# 判断是否为文件
print(path.isfile('/Users'))


path.join('/tmp/a','b/c')

from pathlib import Path

p = Path('.')
print(p.resolve())
