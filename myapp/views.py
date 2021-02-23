from django.shortcuts import render

def default_map(request):
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'default.html', 
                  { 'mapbox_access_token': mapbox_access_token })

    #return render(request, 'default.html', {})