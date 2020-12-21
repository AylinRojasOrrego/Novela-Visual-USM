label hora_mal:
    $ hora= 'no'

    "Decides ir a una plaza cerca de la universidad con Annie en busca de pistas"
    annie "Vamos entonces"
    scene plaza with fade
    "Sientes como el viento acaricia tu pelo y ves cómo se mueve el de Annie"
    show annie normal with easeinright:
        xzoom 0.40 yzoom 0.40
        xpos 400 ypos 100
    prota "No hay mucho a quien preguntar, separémonos en busca de algún papel pegado con información"
    annie "Detective Annie en camino"
    hide annie with easeoutright
    "Te separas de Annie, en busca de alguna pista que te ayude a entrar a la fiesta."
    "Pasa un rato, y has revisado todas las cercanías de la plaza"
    "Los únicos papeles que encuentras te hablan de sitios para arrendar"
    "Decides volver al centro de la plaza, donde Annie parece estar esperando por ti"
    show annie sad_mal with easeinright:
        xzoom 0.40 yzoom 0.40
        xpos 400 ypos 100
    annie "¿Cómo te fue [MiNombre], encontraste algo?"
    prota "Nop, tuve mala suerte, ¿tu?"
    show annie muymal with dissolve
    annie "Nada tampoco,parece que no fue buena idea venir a buscar a la plaza"
    prota "Seh…"
    if decisiones==1:
        show annie happy_bien with dissolve
        annie "¿Cual buscaremos ahora?"
        jump primera_pista
    elif decisiones==2:
        show annie happy_bien with dissolve
        annie "Busquemos otra pista"
        jump segunda_pista
    elif decisiones==3:
        show annie sad_mal
        annie "No quedan más pistas que buscar, veamos que podemos hacer con lo que tenemos"
        jump tercera_pista
