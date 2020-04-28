import sys

# print(sys.argv)

sum_of_args = 0
for a in sys.argv[1:]:
    sum_of_args += int(a)
print(sum_of_args)