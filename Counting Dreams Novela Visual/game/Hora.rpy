label hora:
    #"aqui comienza la escena de la hora"
    prota '¿Por donde empezamos?'
    annie 'Revisemos una publicación una vez más'
    prota '¿Crees que nos dejaron pistas ahí?'
    annie 'Es lo más probable'
    show annie phone with dissolve:
        xzoom 0.40 yzoom 0.40
        xpos 500 ypos 100    
    show confesion with dissolve:
        xpos 450 ypos 0
        xzoom 0.65 yzoom 0.62
    annie 'A ver... Escucha esto'
    annie 'Un campo abierto veras y entre el verde buscaras'
    hide confesion with dissolve

    show annie happy_bien with dissolve
    prota 'Ah, una rima, ¿A qué se referirá?'
    #hide annie_happy_bien
    #show annie_pensativa (I guess)
    annie 'Quizá se refiere a la cancha'
    prota 'Yo estaba pensando en alguna plaza cercana'
    #hide annie_pensativa
    #show annie_happy_bien
    annie 'Tú decides esta vez'
    menu Desición_hora:
        annie '¿A dónde deberíamos buscar?'
        'Quizas tienes razón... ¡Vamos a la cancha!':
            show annie muyfeliz with dissolve
            #block of code to run
            jump hora_bien
        'Debe ser alguna plaza de aquí cerca!':
            show annie muymal with dissolve
            #block of code to run
            jump hora_mal