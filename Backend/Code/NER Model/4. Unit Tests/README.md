**# Unit testing**

to run unit testing call the function `python unitTesting.py` from this directory after installing all the requirements.

We first created equalvance partiiton on the test inputs. Eg for `calc_score`, we had partitions of  [-inf, -1], (-1, 1) and [1, inf]. Inputs from each parition will be tested.
More emphasis will be placed on the actual boundaries (called Boundary Value Analysis) since errors tend to occur there.

For multiple input function such as `get_skill2mod_score`, we will have both positive and negative test cases. Negative test cases will only fill up one of the parameters 
and not the other to make sure we know which input is causing the error.

Gaurd Clauses will be added to the functions to prevent bad inputs from affecting the funciton
