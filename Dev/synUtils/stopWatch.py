import time
imp

print('Starting Timer')
now = time.time()
print(now)

time.sleep(3)
print('Stoping timer')
then = time.time()
print(then)
print(then - now)
print('Total Time Taken: ' + str(then - now))

