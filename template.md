# Awesome Pretrained StyleGAN

{% for model in models %}

## {{ model.name }}

![](images/{{ model.name  | replace(" ", "%20")}}.jpg)
- Dataset: {{ model.dataset }}
- Resolution: {{ model.resolution }}
- Author: {{ model.author }}
- [Download link]({{ model.download_url }})
- Licence: {{ model.license }}
- [Source]({{ model.source_url }})

{% endfor %}

