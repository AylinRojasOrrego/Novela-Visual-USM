
label lugar_bien:
    $ lugar= 'si'
    annie "La piscina ¿eh?, si le encuentro un poco de sentido vamos"
    "Vas con Annie a la piscina de la universidad en busca de pistas."
    scene piscina with fade
    show annie normal with dissolve:
        xzoom 0.40 yzoom 0.40
        xpos 500 ypos 150
    "El ambiente esta fresco, sientes ganas de meterte a la piscina a nadar un rato."
    show annie happy_bien with dissolve
    annie "Oye, despierta, no te quedes mirando a la piscina, que me dan ganas de empujarte dentro."
    prota "Si me mojas ahora, no tendré ropa para ir a la fiesta"
    show annie muyfeliz with dissolve
    annie "Con eso me tientas aún más, pero tienes razón, la fiesta"
    show annie normal with dissolve
    prota "Busquemos algún poster informativo con eso"

    scene pasillo1 with fade
    "Te separas de Annie un rato, observando el lugar en busca de algo que de té más información"
    show annie happy_bien with easeinright:
        xzoom 0.50 yzoom 0.50
        xpos 500 ypos 200
    annie "¡[MiNombre]! ya lo encontré, parece que se despegó y por eso nos costó encontrarlo"
    prota "Genial, ¿Cuál es la respuesta entonces?"

    show Lugar:
        align (0.2 , 0.2)
    with dissolve    

    $Lu ='22:30[hrs]'

    $PistaLugar = 'Lugar.png'

    $pista +=1

    show annie normal with dissolve
    annie "Decia 'Patio el Cañón', bastante autoexplicatorio"


    prota "Buena, tenemos una respuesta"
    show annie muyfeliz with dissolve
    if decisiones==1:
        annie "Nos quedan 2 cosas por buscar"
        jump primera_pista
    elif decisiones==2:
        annie "Nos queda 1 pista por encontar"
        jump segunda_pista
    elif decisiones==3:
        annie "No hay nada mas por buscar"
        jump tercera_pista


    