import csv
with open('csv_w.csv', 'w')as w:          #check the pwd file is there or not
    x = csv.writer(w)
    x.writerow(['pyhton', 'java', 'R', ])
    x.writerows([['pyhton', 'java', 'R'], ['apple', 'banana', 'coconut'], ['biriyani', 'dosa', 'idli']])

