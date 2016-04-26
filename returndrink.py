# age_response = {
# Kids drink toddy. 0 - 13 (13) /7 0 - 1
# Teens drink coke. 14 - 17 (3) / 7
# Young adults drink beer. 18 - 20 (2)
# Adults drink whisky. 21 +
#
# }

from __future__ import division

def people_with_age_drink(age):
    test_age = age / 7
    if test_age < 2:
        return "drink toddy"
    elif test_age < 2.5714285714285716:
        return "drink coke"
    elif test_age < 3:
        return "drink beer"
    else:
        return "drink whiskey"



for i in range(1, 22):
    print(i)
    print(people_with_age_drink(i))
