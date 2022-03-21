import re

p = re.compile('ca*t')
print(p.match('caaaaat'))

# $以什么结尾
# * 某个字符出现了0次或多次
# ？某个字符出现了0次或1次
# 具体可以详细看下正则表达式的学习
