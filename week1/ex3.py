#!/usr/bin/env python

"""Create three different variables the first variable should use all lower case characters with underscore ( _ ) as the word separator. The second variable should use all upper case characters with underscore as the word separator. The third variable should use numbers, letters, and underscore, but still be a valid variable Python variable name.

Make all three variables be strings that refer to IPv6 addresses.

Use the from future technique so that any string literals in Python2 are unicode.

compare if variable1 equals variable2
compare if variable1 is not equal to variable3"""

my_str = "2001::1"
My_Str = "2002::1"
MY_STR = "2003::1"

my_str == My_Str

my_str != MY_STR