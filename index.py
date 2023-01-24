import random
import string 
def randomname(n):
    ranpass=[random.choice(string.ascii_letters + string.digits) for i in range(n)]
    result="".join(ranpass)
    print(result)
randomname(12)
