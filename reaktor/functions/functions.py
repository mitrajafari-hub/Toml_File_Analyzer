import toml
from reaktor.models import List_package
from reaktor.models import Pkg_Ind

def handle_uploaded_file(f):
    with open('reaktor/static/upload/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# TOML File is opening and it's content is saving to database.
# Package Information (Name and Description) is saving to pname and pdesc fields in List_package Table.
# Package Dependency (Package ID, Package Name and Package version) is saving to pack_id,depend_name and
# depend_version fields in Pkg_Ind Table


    with open('reaktor/static/upload/'+f.name) as file:
        con_file = toml.load(file)
        for key, value in con_file.items():
            if key == 'package':
                for info in value:
                    post = List_package()
                    post.pname = info["name"]
                    post.pdesc = info["description"]
                    post.save()
                    latest_id = List_package.objects.latest('id').id
                    if 'dependencies' in info:
                        for k, v in info["dependencies"].items():
                            p_dep = Pkg_Ind()
                            p_dep.pack_id = latest_id
                            p_dep.depend_name = k
                            p_dep.depend_version = v
                            p_dep.save()