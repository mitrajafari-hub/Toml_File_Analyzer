from django.shortcuts import render
from django.http import HttpResponse
from reaktor.functions.functions import handle_uploaded_file
from reaktor.forms import TomlForm
from reaktor.models import List_package
from reaktor.models import Pkg_Ind
import pkg_resources


def index(request):
    if request.method == 'POST':
        tomldata = TomlForm(request.POST, request.FILES)
        if tomldata.is_valid():
            handle_uploaded_file(request.FILES['file'])
            page = '<html lang="en"><head><meta charset="UTF-8"><title>Package List in TOML File</title>'
            page = page + '</head><body style="background-color:FloralWhite;"><br><center><h3>'
            page = page + '<< Package List in TOML File >></h3></center><br><table align="center" width="50%" border="2">'
            page = page + '<tr><td height="100" align="center"><p style="font-family:verdana;font-size:100%;">'
            page = page + 'File uploaded successfuly. <a href="show">Package List</a></p></td></tr></table></body></html>'
            return HttpResponse(page)
    else:
        tomldata = TomlForm()
        return render(request, "index.html", {'form': tomldata})


def view_info(request):
    pdata = List_package.objects.all()

    ddata = Pkg_Ind.objects.all()

    installed_packages = pkg_resources.working_set
    installed_packages_list = sorted(["%s" % (i.key) for i in installed_packages])

    stu = {
        "display_data": pdata,
        "display_ddata": ddata,
        "installed_packages": installed_packages_list
    }
    return render(request, "show.html", stu)