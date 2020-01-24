# Awesome Pretrained StyleGAN

A collection of pre-trained [StyleGAN](https://github.com/NVlabs/stylegan) models trained on different datasets at different resolution.

{% for model in models %}
[![](images/thumbs/{{ model.name | replace(" ", "%20") }}.jpg)](#{{ model.name | replace(" ", "-")}}){% endfor %}

If you have a publically accessible model which you know of, or would like to share please see the [contributing](#contributing) section. _Hint: the simplest way to submit a model is to fill in this [form](https://forms.gle/rUU9kJf2YaAUhSJ66)._

### Table of Contents

- Models
{% for model in models %}
    - [{{ model.name }}](#{{ model.name | replace(" ", "-")}}){% endfor %}
- [Contributing](#contributing)

{% for model in models %}
## {{ model.name }}

![](images/{{ model.name | replace(" ", "%20")}}.jpg)
- Dataset: {{ model.dataset }}
- Resolution: {{ model.resolution }}
- Author: [{{ model.author }}]({{ model.author_url }})
- [Download link]({{ model.download_url }})
- StyleGAN implementation: {{ model.implementation }}
- Licence: {{ model.license }}
- [Source]({{ model.source_url }})

{% endfor %}

## Contributing

__TLDR: You can either edit the [models.csv](models.csv) file or fill out this [form](https://forms.gle/rUU9kJf2YaAUhSJ66).__

This readme is automatically generated using Jinja, please do not try and edit it directly. Information about the models is stored in `models.csv` please add your model to this file. Preview images are generated automatically and the process is used to test the link so please only edit the csv file.