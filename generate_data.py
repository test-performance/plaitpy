# python main.py --csv --num 1000 templates\finance\transaction_equal_distro.yaml

from src import template
import csv
t = template.Template("templates/finance/transaction.yaml")
data = t.gen_records(1000)
keys = data[0].keys()

with open('data.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(data)