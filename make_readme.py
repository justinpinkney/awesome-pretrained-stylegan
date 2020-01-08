import csv
import jinja2

model_file = "models.csv"
output_file = "README.md"
env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
template = env.get_template('template.md')

with open(model_file) as csvfile:
    reader = csv.DictReader(csvfile)
    models = list(reader)
    content = template.render(models = models)

with open(output_file, "w") as readme:
    readme.write(content)

