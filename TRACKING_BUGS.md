## CREATING NOTES TO TRACK ERRORS AND BUGS 

### 1. Type Error: list object is not callable
----
- Date: Dec 4, 2022
- Note: note038_scatterplot.py
- Reference: [stake overflow case](https://stackoverflow.com/questions/35030659/unexpected-python-typeerror-list-object-is-not-callable)
----

- A. Situation: I was trying to create scatterplot using below code 
```python
plt.scatter(df['eng'], df['math'])
plt.xlabel('eng scores')
plt.ylabel('math scores')
```

- B. Mistake: At some point, I made mistakes in assigning label as below
```python
plt.scatter(df['eng'], df['math'])
plt.xlabel=['eng scores']
plt.ylabel=['math scores']
```

- C. 1st Fix: graph was still generated so I did not know that I made mistakes.  
At some point, I found erorrs so I changed B to A.
But even after that no labels were generated. Error message said "Type Error: list object is not callable" 
but I did not have any other list.

- D. 2nd Fix: restart & run.  
Somewhere in the system, plt.xlabel was treated like list. So even after changing B to A, system still showed an error. 
Only when I restarted & run all for jupyter, lables were showing up.


### 2. [Errno 13] Permission denied
----
- Date: Dec 14, 2022
- Note: note041_excel_cell.py
----
- A. Situation: I was saving changes to excel as below
```python
ws["A1"] = 2
ws["A2"] = 3
ws["A3"] = 4
wb.save("sample.xlsx")
```  

- B. Error: 
```python
# PermissionError: [Errno 13] Permission denied: 'sample.xlsx'
```  

- C. Try:
Excel file was open hence changes could not have been made.  
When I closed the file and re-run the code, 
all changes have been made.
