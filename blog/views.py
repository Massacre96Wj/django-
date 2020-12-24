from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def photo(request):
    return render(request, 'photo.html')

def xixi(request):
    return render(request, 'xixi.html')

def new_year(request):
    return render(request, 'new_year.html')

def photos(request):
    return render(request, 'photos.html')

def ElectronAlbum(request):
    return render(request, 'html/ElectronAlbum.html')

def FullPhoto(request):
    return render(request, 'html/FullPhoto.html')

def PhotoWall(request):
    return render(request, 'html/PhotoWall.html')

def WindowShades(request):
    return render(request, 'html/WindowShades.html')

def threePhoto(request):
    return render(request, 'html/3dPhoto.html')

def cube(request):
    return render(request, 'html/cube.html')
