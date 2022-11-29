import re
def find_shortest(s):
  return min(list(map(len,re.findall(r"[a-zA-Z]+",s))),default=0)