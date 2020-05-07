import sys

# try:
#     sys.exit('sys.exit()也會拋出例外')
# except SystemExit as e:
#     print(e.args)
#     print(e)
#     print('印出例外')
# finally:
#     print('結束')

try:
    sys.exit('sys.exit()也會拋出例外')
except Exception as e:
    print(e.args)
    print(e)
    print('印出例外')
finally:
    print('結束')
