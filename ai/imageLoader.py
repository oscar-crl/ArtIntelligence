import os
from google_images_search import GoogleImagesSearch

gis = GoogleImagesSearch(os.environ["DEV_KEY"], os.environ["SEARCH_CX"])


def imageLoader(query):

    _search_params = {
        'q': query,
        'num': 10,
        'safe': 'off',
        'fileType': 'jpg',
        'imgType': 'photo'
    }

    gis.search(search_params=_search_params)
    for image in gis.results():
        image.download('./download/' + query.replace(' ', '_'))
        image.resize(500, 500)
        print(image.path)

    return gis.results()
