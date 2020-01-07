import csv
import jinja2

filename = "models.csv"
env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
template = env.get_template('template.md')

with open(filename) as csvfile:
    reader = csv.DictReader(csvfile)
    models = list(reader)
    print(template.render(models = models))

