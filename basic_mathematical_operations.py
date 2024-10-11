def basic_op(operator, value1, value2):
         operator_dict = {"+" : lambda x,y:x+y,"*" : lambda x,y:x*y,"-" : lambda x,y:x-y,"/": lambda x,y: x/y,}
         return operator_dict[operator](value1,value2)