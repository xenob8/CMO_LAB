from tabulate import tabulate

table = [['First Name', 'Last Name', 'Age'],
         ['John', 'Smith', 39], ['Mary', 'Jane', 25],
         ['Jennifer', 'Doe', 28]]

rows = []
rows.append([1,2,3])
print(rows)
print(tabulate(table, headers='firstrow', tablefmt='grid'))