
label lugar_bien:
    annie "La piscina ¿eh?, si le encuentro un poco de sentido vamos"
    "Vas con Annie a la piscina de la universidad en busca de pistas."
    scene piscina
    show annie_normal with dissolve:
        xzoom 0.40 yzoom 0.40
        xpos 500 ypos 150
    "El ambiente esta fresco, sientes ganas de meterte a la piscina a nadar un rato."
    show annie_happy_bien with dissolve:
        xzoom 0.40 yzoom 0.40
        xpos 500 ypos 150
    annie "Oye, despierta, no te quedes mirando a la piscina, que me dan ganas de empujarte dentro."
    prota "Si me mojas ahora, no tendré ropa para ir a la fiesta"
    hide annie_happy_bien with dissolve
    show annie_muyfeliz with dissolve:
        xzoom 0.40 yzoom 0.40
        xpos 500 ypos 150
    annie "Con eso me tientas aún más, pero tienes razón, la fiesta"
    show annie_normal with dissolve:
        xzoom 0.40 yzoom 0.40
        xpos 500 ypos 150
    prota "Busquemos algún poster informativo con eso"
    hide annie_muyfeliz with dissolve
    hide annie_normal with dissolve
    scene pasillo1
    "Te separas de Annie un rato, observando el lugar en busca de algo que de té más información"
    show annie_happy_bien with easeinright:
        xzoom 0.50 yzoom 0.50
        xpos 500 ypos 200
    annie "¡[MiNombre]! ya lo encontré, parece que se despegó y por eso nos costó encontrarlo"
    prota "Genial, ¿Cuál es la respuesta entonces?"
    show annie_normal with dissolve:
        xzoom 0.50 yzoom 0.50
        xpos 500 ypos 200
    annie "Decia 'Patio el Cañón', bastante autoexplicatorio"
    prota "Buena, tenemos una respuesta"
    $ pista =1
    jump primera_pista



    