raw_data    ="""Filesystem Size Used Avail Use% Mounted on
tmpfs 3.9G 0 3.9G 0% /dev/shm
tmpfs 3.9G 26M 3.8G 1% /run
tmpfs 3.9G 0 3.9G 0% /sys/fs/cgroup"""

# print raw_data
# print type(raw_data)
list = raw_data.splitlines()
for i in range(len(list)):
    result = list[i].split()
    print result[0],":",result[1],":",result[4]