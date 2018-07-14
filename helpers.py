from datetime import datetime
from dateutil.relativedelta import relativedelta

AGE_IN_THIRD_GRADE = 5

def validateAndInferAge(age, graduationDate):
    try:
        age = int(age)
    except ValueError:
        if graduationDate:
            gradDate = datetime.strptime(graduationDate, "%m/%d/%y")
            currentDate = datetime.strptime(str(datetime.now()), "%Y-%m-%d  %H:%M:%S.%f")
            age = relativedelta(currentDate, gradDate).years + AGE_IN_THIRD_GRADE
        else:
            age = ''
    return age
