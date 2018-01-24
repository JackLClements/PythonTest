# -*- coding: utf-8 -*-
"""
@author: Jack L. Clements
"""

import sys, winpexpect 
#Note - I wanted to use winpexpect to run a test script that would, similar to a unit test, attempt to test various aspects of this script
#Either due to compatability or library issues, winpexpect clearly has other ideas, appending extraneous characters to inputs
#It also mangles all non-expect strings into a jumbled half-readable mess
#Due to a lack of a linux testing environment at present
child = winpexpect.winspawn('Python -u PasswordCheck.py')
child.logfile = sys.stdout
prompt = 'test'
child.expect('Please enter your username: \n')
child.sendline('User01') #appends newline and treats User01, a login attempt, as a whole new 
child.expect_exact('User01, please enter your old password.')
child.expect_exact('Please enter your old password: \n')
child.sendline(str('Password1'))
child.expect_exact('Please enter a new password: \n')
child.sendline(str('TestPass3'))
child.expect_exact('Please enter the password again for verification: \n')
child.sendline(str('TestPass3'))
child.expect_exact('User password changed.')
child.close()

#code such as this could theoretically be used for unit testing, but I cannot seem to get any implementation to work properly and as such have left it here

