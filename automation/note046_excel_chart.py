#note046_excel_chart.py
#prepare libraries and settings

from openpyxl import load_workbook
wb = load_workbook("sample.xlsx") 
ws = wb.active


########## 1. PACKAGE & DOCUMENTATION 
# in order to draw a chart, openpyxl.chart package is needed as below.
# check the link for documentation: https://openpyxl.readthedocs.io/en/stable/charts/introduction.html 

from openpyxl.chart import BarChart, LineChart, Reference


########## 2. BARCHART
# define range (from cell B2 to C11); since min_row!=1, legend will just show Series 1 and Series 2
bar_value = Reference(ws, min_row=2, max_row=11, min_col=2, max_col=3)
bar_chart = BarChart()            #assign chart type as bar chart
bar_chart.add_data(bar_value)     #adding data to the chart
ws.add_chart(bar_chart, "E1")     #insert chart to E1


########## 3. LINE CHART
# good read for ref: https://www.pylenin.com/blogs/line-charts-openpyxl/
# define range (from cell B2 to C11) including title, so that legend will show eng/math
line_value = Reference(ws, min_row=1, max_row=11, min_col=2, max_col=3) 
line_chart = LineChart()                                    #assing chart type as line chart
line_chart.add_data(line_value, titles_from_data = True)    #titles_from_data enable legend to be pulled from titles (B1, C1)

line_chart.title = "Scores"           #assign title to the chart
line_chart.style = 20                 #assign style to the chart (20 is pre-defined style code)
line_chart.y_axis.title = "Scores"    #add y axis' title
line_chart.x_axis.title = "ID"        #add x axis' title
ws.add_chart(line_chart, "E1")        #insert chart to E1

wb.save("sample_chart.xlsx")          #save!
  
  
