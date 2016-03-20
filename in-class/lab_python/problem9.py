# Author: Josiah Campbell
# Version: Winter 2016
import pickle
import time

file_cant_open = "err_file"
file_name = "admin_pickle"
file_name_err = "admin_pickahl"
admins = ["Lawrence", "Ira", "Carl"]

print "Admins to pickle:"
for admin in admins:
    print "Admin: " + admin

try:
    # Append 'b' to the mode to open the file in binary mode
    fileObject = open(file_cant_open, 'wb')
except IOError:
    print "Error: Write permissions are not enabled for " + file_cant_open
except OSError:
    print "Error: Write permissions are not enabled for " + file_cant_open

obj = open(file_name, 'wb')
pickle.dump(admins, obj)
obj.close()


print "\nThe pickling has begun\n"

time.sleep(2)
try:
    obj = open(file_name_err, 'r')
except IOError:
    print "Error: Read permissions are not enabled for " + file_cant_open
except OSError:
    print "Error: Read permissions are not enabled for " + file_cant_open
except NameError:
    print "Error: File not found"

unpickled_admins = pickle.load(open(file_name, 'r'))

time.sleep(2)
print "\nUnpickled admins:"
for admin in unpickled_admins:
    print "Admin: " + admin
