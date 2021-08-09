cupcake=open("CupcakeInvoices.csv")
# for row in cupcake:
#   print(row)

# for row in cupcake:
#   spliced=row.rstrip("\n").split(",")
#   for item in spliced:
#     if item== "Strawberry":
#       print(item)
#     if item == "Chocolate":
#       print(item)
#     if item == "Vanilla":
#       print(item)

# for row in cupcake:
#   spliced=row.rstrip("\n").split(",")
#   total=int(spliced[3])*float(spliced[4])
#   print(total)
# total=0
# for row in cupcake:
#   spliced=row.rstrip("\n").split(",")
#   total+=int(spliced[3])*float(spliced[4])
# print(total)

# print(round(total, 2))

from bokeh.plotting import figure, show

x = []
y = []

a=[]
b=[]

c=[]
d=[]

num=0
num1=0
num2=0
for row in cupcake:
  spliced=row.rstrip("\n").split(",")
  for item in spliced:
    print(item)
    if item == "Strawberry":
      x.append(num)
      y.append(int(spliced[3])*float(spliced[4]))
      num+=1
    if item == "Chocolate":
      a.append(num1)
      b.append(int(spliced[3])*float(spliced[4]))
      num1+=1
    if item == "Vanilla":
      c.append(num2)
      d.append(int(spliced[3])*float(spliced[4]))
      num2+=1


# prepare some data


# create a new plot with a title and axis labels
p = figure(title="Cupcakes", x_axis_label="invoice", y_axis_label="profit")

# add a line renderer with legend and line thickness
p.line(x, y, legend_label="strawberry", line_width=3, line_color="pink")
p.line(a,b, legend_label="chocolate", line_width=3, line_color="brown")
p.line(c,d, legend_label="vanilla", line_width=3, line_color="blue")
# show the results
show(p)

cupcake.close()