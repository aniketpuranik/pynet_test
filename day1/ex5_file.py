#!usr/bin/env python

with open("test_file") as f:
    for line in f:
         print line.strip()

f = open ("new_test_file.txt", "w")
f.write("test\n")
f.close()

f = open ("new_test_file.txt", "a")
f.write("appended\n")
f.close

with open ("new_test_file.txt") as f:
    for line in f:
        print line.strip()
