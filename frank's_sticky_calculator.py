def sticky_calc(operation, val1, val2):
    val3 = float(str(round(val1))+ str(round(val2)))
    calculation_dic = {'+': lambda a,b: a+b,'-': lambda a,b: a-b, '*':lambda a,b: a*b,'/':lambda a,b: a/b}
    return round(calculation_dic[operation](val3,round(val2)))