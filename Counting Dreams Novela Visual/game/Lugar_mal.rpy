image annie_sad_mal="Annie_Act1_01_Sad.png"
image annie_normal="Annie_Act1_01.png"
label lugar_mal:
    "Decides ir a la playa con Annie en busca de pistas para resolver el acertijo" 
    hide annie_happy_bien with dissolve
    #cambio de escena a una playa
    show playa with fade
    hide biblioteca
    hide annie_normal
    show annie_normal with dissolve:
        xzoom 0.40 yzoom 0.40
        xpos 500 ypos 100
    "El viento sopla gentilmente y la temperatura esta agradable"
    "Sientes ganas de quedarte acá un rato, pero Annie te mira"
    annie "Oye [MiNombre] te quedaste pegado viendo la nada, así no vamos a encontrar la pista"
    prota "Oh, perdona, es que el ambiente es tranquilizador"
    annie "Tienes razón pero vinimos en busca de algo"
    prota "Claro, separémonos un rato, y así encontraremos la pista más rápido"
    hide annie_normal with dissolve
    "Un tiempo considerable pasa, y ni Annie ni tu han encontrado nada"
    "Decides parar de buscar, y te reúnes con ella"
    show annie_sad_mal with dissolve:
        xzoom 0.40 yzoom 0.40
        xpos 500 ypos 100
    prota "Quede un poco cansado de eso"
    annie "Seh, yo también, lo peor es que no conseguimos ni una sola pista"
    prota "Parece la playa no era la respuesta a ese acertijo, ¿Lo intentamos resolver de nuevo?"
    annie "nah, volvamos a la universidad, y tratemos de resolver el resto de acertijos"
    prota "“¿Porque te rindes así? "
    annie "Es que a pasado el tiempo volando mientras buscábamos esto, y a este paso, no conseguiremos el resto de las pistas"
    prota "Tienes razón Annie, volvamos a la Universidad y probemos otra cosa"
    "A pesar de tener un ambiente agradable, la playa no era la respuesta al acertijo"
    "Te devuelves con Annie a la universidad"
    hide annie_sad_mal with dissolve
    show biblioteca with fade
    hide playa 
    show annie_normal with dissolve:
        xzoom 0.40 yzoom 0.40
        xpos 500 ypos 100
    $ pista=0
    jump primera_pista
