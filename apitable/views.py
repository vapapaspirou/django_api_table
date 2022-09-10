import pandas as pd
import requests
from django.core.paginator import Paginator
from django.shortcuts import render
import json

from pandas.io.common import urlopen


def table(request):
    url = ('https://api.artic.edu/api/v1/artworks')
    response = requests.get(url)
    json_obj = urlopen(url)
    decoded_data = json.load(json_obj)
    # Paginator is for the paging
    p = Paginator(decoded_data['data'], 5)
    page = request.GET.get('page')
    paging = p.get_page(page)
    # We save the data at dataframe so we could display it like table
    df = pd.DataFrame(paging)
    print(df)
    return render(request, 'index1.html',   {'data': decoded_data['data'], 'paging': paging, 'df': df})




