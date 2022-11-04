def save_log (dir, func, num1, num2, result) :
    cal_log = open(dir,'a')

    cal_log.write("Selected operation : "+ func + "\n")
    cal_log.write("first number : "+ num1 + "\n")
    cal_log.write("second number : "+ num2 + "\n")
    cal_log.write("result : "+ result + "\n")
    cal_log.write("formula : " + num1 +" "+ func +" "+ num2 + ' = ' + result + "\n\n\n")
    cal_log.close()