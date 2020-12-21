
label lugar_mal:
    $ lugar= 'no'

    "Decides ir a la playa con Annie en busca de pistas para resolver el acertijo" 
    hide annie happy_bien with dissolve
    #cambio de escena a una playa
    scene playa with fade
    show annie normal with dissolve:
        xzoom 0.40 yzoom 0.40
        xpos 500 ypos 100
    "El viento sopla gentilmente y la temperatura esta agradable"
    "Sientes ganas de quedarte acá un rato, pero Annie te mira"
    show annie sad_mal with dissolve
    annie "Oye [MiNombre] te quedaste pegado viendo la nada, así no vamos a encontrar la pista"
    prota "Oh, perdona, es que el ambiente es tranquilizador"
    show annie normal with dissolve
    annie "Tienes razón pero vinimos en busca de algo"
    prota "Claro, separémonos un rato, y así encontraremos la pista más rápido"
    hide annie with easeoutright
    "Un tiempo considerable pasa, y ni Annie ni tu han encontrado nada"
    "Decides parar de buscar, y te reúnes con ella"
    show annie sad_mal with easeinright:
        xzoom 0.40 yzoom 0.40
        xpos 500 ypos 100
    prota "Quede un poco cansado de eso"
    show annie muymal with dissolve
    annie "Seh, yo también, lo peor es que no conseguimos ni una sola pista"
    prota "Parece la playa no era la respuesta a ese acertijo, ¿Lo intentamos resolver de nuevo?"
    annie "nah, volvamos a la universidad, y tratemos de resolver el resto de acertijos"
    prota "“¿Porque te rindes así? "
    show annie sad_mal with dissolve
    annie "Es que a pasado el tiempo volando mientras buscábamos esto, y a este paso, no conseguiremos el resto de las pistas"
    prota "Tienes razón Annie, volvamos a la Universidad y probemos otra cosa"
    "A pesar de tener un ambiente agradable, la playa no era la respuesta al acertijo"
    
    if decisiones==1:
        annie "Bueno... nos quedan 2 cosas por buscar"
        jump primera_pista
    elif decisiones==2:
        annie "Bueno... nos queda 1 pista por encontar"
        jump segunda_pista
    elif decisiones==3:
        annie "Rayos... no hay nada mas por investigar"
        jump tercera_pista
