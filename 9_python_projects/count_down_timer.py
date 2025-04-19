import time

def CountdownTimer(seconds):
    for i in range(seconds,0,-1):
        min , sec = divmod(i,60)
        timer = f"{min:02d}:{sec:02d}"
        print(timer, end="\r")
        time.sleep(1)

seconds = int(input("Enter the time in seconds: "))
CountdownTimer(seconds)
print("Time's up!        ")