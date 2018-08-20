

import time

new_year_time = time.mktime(time.strptime("1 DEC 19", "%d %b %y"))

print((new_year_time - time.time())/ (60 * 60 * 24))
