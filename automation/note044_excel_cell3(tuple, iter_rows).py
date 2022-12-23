#note044_excel_cell3(iter_rows).py
#prepare libraries and settings

from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active


########## 1. CHECK VALUES (PER ROW, PER COLUMN WITH TUPLE)
#1) ws.rows
print(ws.rows)              #result: <generator object Worksheet._cells_by_row at 0x0000021560F7B610>

#2) tuple(ws.rows)
print(tuple(ws.rows))       #result: ((<Cell 'Sheet'.A1>, <Cell 'Sheet'.B1>,<Cell 'Sheet'.C1>), (<Cell 'Sheet'.A2> ...

for row in tuple(ws.rows):  #result: (<Cell 'Sheet'.A1>, <Cell 'Sheet'.B1>,<Cell 'Sheet'.C1>), (<Cell 'Sheet'.A2> ...
  print(row)

#3) tuple(ws.columns)   
print(tuple(ws.columns))    #result: same as above, but tuple will group data per column

#4) checking values


########## 2. CHECK VALUES (PER ROW, PER COLUMN WITH ITER_ROWS, ITER_COLS)
