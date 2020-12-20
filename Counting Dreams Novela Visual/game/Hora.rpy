label hora:
    prota '¿Por donde empezamos?'
    show annie happy_bien with dissolve
    annie 'Revisemos una publicación una vez más'
    prota '¿Crees que nos dejaron pistas ahí?'
    show annie normal with dissolve
    annie 'Es lo más probable'
    show annie phone with dissolve   
    show confesion with dissolve:
        xpos 450 ypos 0
        xzoom 0.65 yzoom 0.62
    show annie mirando_cel with dissolve
    annie 'A ver... Escucha esto'
    annie 'Un campo abierto veras y entre el verde buscaras'
    hide confesion with dissolve

    show annie happy_bien with dissolve
    prota 'Ah, una rima, ¿A qué se referirá?'
    show annie pensativa with dissolve
    annie 'Quizá se refiere a la cancha'
    prota 'Yo estaba pensando en alguna plaza cercana'
    show annie happy_bien with dissolve
    annie 'Tú decides esta vez'
    menu Desición_hora:
        annie '¿A dónde deberíamos buscar?'
        'Quizas tienes razón... ¡Vamos a la cancha!':
            show annie muyfeliz with dissolve
            jump hora_bien
        'Debe ser alguna plaza de aquí cerca!':
            show annie muymal with dissolve
            jump hora_mal