import os
from django.conf import settings
from django.shortcuts import render
import datetime
from rembg import remove
from PIL import Image
from .models import ImageDetails

def gotohome(request):
    return render(request,'index.html')

def removebgpage(request):
    if request.method == 'GET':
        return render(request, 'bgremove.html')
    else:
        file_name = request.FILES['image']
        current_time = datetime.datetime.now()
        current_time = str(current_time).replace(
            " ", "_").replace(".", "_").replace(":", "_")

        saving_directory = os.path.join(
            settings.MEDIA_ROOT+f"images_{current_time}")
        os.makedirs(saving_directory+"", exist_ok=True)

        # print(saving_directory, (str(file_name.name))
        file_path = os.path.join(saving_directory, file_name.name)

        with open(file_path, 'wb')as destination:
            for chunk in file_name.chunks():
                destination.write(chunk)

        filename = str(str(file_name.name).split(".").pop())

        input_path = file_path
        output_path = saving_directory+"\\remove_bg__"+filename+".png"
        input = Image.open(input_path)
        output = remove(input)
        output.save(output_path)

        real_image_name = file_name.name
        remove_image_name = "remove_bg__"+filename+".png"
        real_image_link = "images__"+current_time+"\\"+file_name.name

        remove_image_link = "images_"+current_time+"\\"+remove_image_name
        print("Image Link: "+remove_image_link)
        print("THis is hot:  ")
        servername = (request.META.get('HTTP_HOST'))
        print(remove_image_link.replace('\\', '/'))
        return render(request, 'bgremove.html', {'imagelink': "../media/" + remove_image_link.replace('\\', '/')})


def download_image(request):

    print(request.POST.get('imagepath'))

    pass
