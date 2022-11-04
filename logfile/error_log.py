def save_error (dir, errortxt, position, input) :
    error_log = open( dir ,'a' )
    error_log.write("error location : "+ position +"\n")
    error_log.write("input data : "+ input +"\n")
    error_log.write("error : "+errortxt +"\n\n\n")
    error_log.close()

    