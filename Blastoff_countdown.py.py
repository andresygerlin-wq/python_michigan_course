# FOR loop version - uses predefined list
import time
countdown = [5, 4, 3, 2, 1]
for i in countdown:
    if i > 0:
        print(i)
        time.sleep(1)
        
print("Blastoff!!","\U0001F680")

print("----------")

# WHILE loop version, uses counter variable
import time
x = 5
while x > 0:
    print(x)
    x = x - 1
    time.sleep(1)
    
print("Blastoff!!","\U0001F680")
