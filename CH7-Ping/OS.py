import os
hostname = "google.com"
response = os.system("ping " + hostname + " -t")
print response
if response == 0:
    print hostname, 'up'
else:
    print hostname, 'down'