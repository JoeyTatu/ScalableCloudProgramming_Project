import time
seconds= int(time.time())
print("Seconds since epoch = ", seconds)
print("milliseconds since epoch = ", seconds * 1000)
print("1 hour ago", (seconds - 3600)*1000)
print("5 minutes ago", (seconds - 300)*1000)
