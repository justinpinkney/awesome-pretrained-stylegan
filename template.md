{% for model in models %}

## {{ model.name }}

![](images/{{ model.name }}.jpg)

{{ model.description }}

{{ model.dataset }} - {{ model.resolution }}

by {{ model.author }}

[Download link]({{ model.download_url }})
Licence - {{ model.license }}
[Source]({{ model.source_url }})

{% endfor %}

