# function generates all subsets of a
def sub_sets (a, b, lo):
  hi = len(a)
  if (lo == hi):
    print (b)
    return
  else:
    c = b[:]
    b.append (a[lo])
    sub_sets (a, b, lo + 1)
    sub_sets (a, c, lo + 1)

def main():
  a = ['A', 'B', 'C', 'D', 'E']
  b = []
  sub_sets (a, b, 0)

main()