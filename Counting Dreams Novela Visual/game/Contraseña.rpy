
label contraseña:
    "Decides buscar la contraseña para entrar a la fiesta"
    prota "¿En qué parte buscamos?"
    annie "Veamos..."
    "Annie saca su celular, para revisar si la publicación da algún indicio"
    show annie phone with dissolve   
    show confesion with dissolve:
        xpos 450 ypos 0
        xzoom 0.65 yzoom 0.62
    annie "Escucha esto, “Todos me conocen, pues soy un buen referente, en los viejos tiempos lancé frases como municiones y ahora el silencie me defiende pues no puedo encenderme”"
    hide confesion with dissolve
    show annie happy_bien with dissolve
    prota "Parece la descripción de un lugar"
    prota "¿Dónde será?"
    annie "Quiero creer que es por algún bar cercano"
    prota "Podría ser el patio del Cañón"
    menu Desición_contraseña:
        show annie pensativa with dissolve
        annie '¿En dónde deberíamos buscar?'
        'Dirijámonos al Cañon':
            jump contraseña_bien
        'Revisemos en los bares':
            jump contraseña_mal