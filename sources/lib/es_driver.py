from string import Template
from ..config import es_base_url, index, type
import requests

__author__ = 'roy'


def construct_es_url(_es_base_url=es_base_url, _index=index, _type=type):
    url = Template("${es_base_url}/${index}/${type}")
    url = url.substitute(es_base_url=_es_base_url, index=_index, type=_type)
    return url


def post_to_es(url, data):
    r = requests.post(url, data)
    response = r.text
    return response



if __name__ == "__main__":
    my_url = construct_es_url("a", "b", "c")
    print(my_url)
