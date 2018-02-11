# Decision Trees

Code for implementing Decision Trees with Information Gain and Variance Purity heuristics in Python 3. 

Code written by Ishan Sharma (ixs171130@utdallas.edu) as part of CS6375 (Spring 2018) class assignment 
at University of Texas at Dallas. 

## How to Run

Make sure that you have [Python 3](https://www.python.org) and [Pandas](http://pandas.pydata.org) installed.  
At least Python 3.2 is required. 

[PIP](https://pip.readthedocs.io/en/stable/installing/) is required to install Pandas. 

1. Open the project folder in terminal and run `pip install pandas`
2. Run using `python3 ./decision_tree <L> <K> <training-set> <validation-set> <test-set> <to-print>`
    - `L`, `K` are arguments for random pruning
    - `training-set` is absolute or relative path to the training set
    - `validation-set` is absolute or relative path to the training set
    - `test-set` is absolute or relative path to the test set
    - `to-print` should be 'y' or 'n' depending on whether you want to see the pruned trees printed or not

You can also see the argument descriptions by entering `python3 ./decision_tree -h` in terminal. 

#### Copyright 2018 Ishan Sharma

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.