import sys
import datetime
if len(sys.argv) > 1:
    try:
        myDate = str(sys.argv[1])
        datetime_object = datetime.datetime.strptime(myDate, '%d.%m.%Y %H:%M')
        print(int(datetime_object.timestamp()))
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
else:
    print(sys.argv[0],'"dd.mm.yyyy HH:MM"')