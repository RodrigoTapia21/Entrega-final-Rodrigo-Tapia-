from TodoAnime.models import Otaku
for _ in range(0,10):
    Otaku(Nombre_anime="Attack on titan", 
    Descripcion="Una joya",
    Tipo_anime="Shonen",
    creado_el="",
    ).save()