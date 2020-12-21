image annie muymal = 'Annie_Act1_02_Mala Desicion.png'
image annie sad_mal="Annie_Act1_01_Sad.png"
label contraseña_mal:
    $ passw= 'no'

    "Decides con Annie ir a unos bares no tan lejos de la universidad"
    #escena de una calle (no la he buscado todavia, no se enojen TwT)
    #encontre una, pero ta mala la resolucion, y no me gusta del todo como escena, era pa que no 
    #quedara vacia, gomen ;-;
    scene calle with fade
    show annie normal with dissolve:
        xzoom 0.50 yzoom 0.50
        xpos 700 ypos 150
    "La calle esta poco concurrida  hoy y la temperatura es aceptable"
    "Perfecto para buscar pistas"
    show annie happy_bien with dissolve
    annie "¿Qué te parece si nos separamos para buscar las pistas?"
    prota "Buena Idea"
    hide annie with easeoutright
    "Luego de cruzar la calle, empiezas a revisar los locales cercanos"
    "Entras a un par de ellos a preguntar, pero nadie sabe nada"
    "Ves a Annie viendo los otros locales, decides descansar un rato y te le acercas"
    show annie muymal with easeinright:
        xzoom 0.50 yzoom 0.50
        xpos 700 ypos 150
    prota "¿Cómo te ha ido?"
    annie "No muy bien que digamos, nadie por acá sabe nada"
    prota "Lo más cercano que conseguí, fueron cupones para una happy hour"
    "Ves a Annie suspirar"
    show annie sad_mal with dissolve:
    if decisiones==1:
        annie "nos quedan 2 cosas por buscar"
        jump primera_pista
    elif decisiones==2:
        annie "nos queda 1 pista por encontar"
        jump segunda_pista
    elif decisiones==3:
        annie "No hay nada mas por buscar"
        jump tercera_pista
    