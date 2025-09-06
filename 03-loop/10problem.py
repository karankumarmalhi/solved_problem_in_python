import time 

attemps = 0;
max_retries = 5
wait_time = 1

while attemps < max_retries:
    print("Attemp:", attemps +1, "-wait:", wait_time)
    attemps+=1
    time.sleep(wait_time)
    wait_time *= 2