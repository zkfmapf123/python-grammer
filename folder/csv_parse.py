import csv

# with open('public/salon.csv','w') as csvfs:
#     field_names = ["Name","Amount","Employee_count"]
#     w = csv.DictWriter(csvfs, fieldnames=field_names)
#     w.writeheader()
#     w.writerow({"Name" : "salon_a", "Amount" : 100, "Employee_count" : 11})
#     w.writerow({"Name" : "salon_b", "Amount" : 100, "Employee_count" : 11})
#     w.writerow({"Name" : "salon_c", "Amount" : 100, "Employee_count" : 11})
#     w.writerow({"Name" : "salon_d", "Amount" : 100, "Employee_count" : 11})

with open('public/salon.csv', 'r') as csvfs:
    lines = csv.DictReader(csvfs)
    for row in lines:
        print(row)
