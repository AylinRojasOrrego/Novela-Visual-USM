label lugar:
    #"Aquí comienza la escena de lugar"
    "Con Annie decides ir en búsqueda del lugar de la fiesta"
    prota "¿Por dónde empezamos?"
    annie "Mejor veamos la publicación de nuevo"
    prota "¿Crees que habrán pistas ahí?"
    annie "No creo que nos dejen sin pista alguna"
    show annie_phone with dissolve:
        xzoom 0.40 yzoom 0.40
        xpos 500 ypos 100    
    show confesion with dissolve:
        xpos 450 ypos 0
        xzoom 0.65 yzoom 0.62
    annie "Ya seas mechón o egresado, sus celestes ondas te han abrazado, dejado incoloras perlas por todo tu costado"
    hide confesion with dissolve

    hide annie_phone with dissolve
    show annie_happy_bien with dissolve:
        xzoom 0.40 yzoom 0.40
        xpos 500 ypos 100
    prota "Ah, un poema, ¿A qué se referirá?"
    hide annie_happy_bien
    show annie_pensativa
    annie "Bueno, creo que se puede referir a la playa"
    prota "Hmm, yo estaba pensando en la piscina de la universidad"
    hide annie_pensativa
    show annie_happy_bien
    annie "Bueno, tu escoges ahora, ¿Dónde quieres ir a buscar?"
    menu Decision_lugar:
        annie "Bueno, tu escoges ahora, ¿Dónde quieres ir a buscar?"
        "Puede que tengas razón, vayamos a la Playa":
            #block of code to run
            jump lugar_mal
        "¿Qué tal si mejor vamos a la piscina?":
            #block of code to run
            jump lugar_bien
        
