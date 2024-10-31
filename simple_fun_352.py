def isValid(formula):
     if (1 in formula and 2 in formula):
          print("condition 1 executed")
          return False
     if(3 in formula and 4 in formula):
          print("condition 2 executed")
          return False
     if ((5 in formula and 6 not in formula) or (6 in formula and 5 not in formula)):
          print("condition 3 executed")
          return False
     if ((8 not in formula) and (7 not in formula)):
        print("condition 4 executed")
        return False
     return True