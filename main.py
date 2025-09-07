def in_autotests_we_trust(a, b):
    if a == b:
        print('Test passed')
    else:
        print('Test failed')

in_autotests_we_trust(10, '10')

in_autotests_we_trust(0, False)
# /Why does the second function call display Test passed? In Python, Boolean values True and False also equal the following:
#
# False == 0 or 0.0
# # True == 1