
### Info

Tableau offers a connection to python or R to extend the data science capabilities using [Tabpy](https://github.com/tableau/TabPy). TabPy executes Python code on the fly and display results in Tableau visualizations.

### Setup

Install tableau server in an environment.

``` sh
virtualenv ~/.virtualenv/TableauTabpy     
pip install tabpy
```

Start tableau server. This will start a webserver where tableau server will listen any connection from Tableau Desktop application. 

``` sh
tabpy
```

Once it starts, check in your browser at the following address to confirm the server is running.

> http://localhost:9004/


### Setup Tableau Workbook

Open [TableautoPython](TableautoPython.twb) and add data source as [airbnb](airbnb.xlsx) excel file.

### Simple Example

Use `` function to run a python code in the server. The python code that runs gets `_argn` (with a leading underscore) as an argument to pass values from Tableau to script.

``` py
SCRIPT_REAL("
import numpy  as np
def aaa(values_list):
    values = (2*np.array(values_list)).tolist()
    print(values)
    return values

print(_arg1)
return aaa(_arg1)
",
SUM([Beds])
)
```

### Complex Example

``` py
(SCRIPT_REAL("
# -------------------- #
# code in `code.py` here
# -------------------- #

# this part is what tableau needs
# the `return` statement is the key part of the program
print('Start')
return run_code(_arg1, _arg2, _arg3, _arg4[0], _arg5[0])
",
AVG([Price]),
MEDIAN([Review Scores Rating]),
MEDIAN([Beds]),
[Cluster Numbers],
[Clustering Algorithm]
)
```

### References

- [Using SCRIPT_REAL in Data Source Tab in Tableau](https://stackoverflow.com/questions/43374490/using-script-real-in-data-source-tab-in-tableau)
- [`SCRIPT_REAL` function in Tableau](https://help.tableau.com/current/pro/desktop/en-us/functions_functions_tablecalculation.htm#scriptreal)
- [TabPy: Combining Python and Tableau](https://towardsdatascience.com/tabpy-combining-python-and-tableau-511b10da8175)