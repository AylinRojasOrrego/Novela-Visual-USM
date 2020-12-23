image annie muymal = 'Annie_Act1_02_Mala Desicion.png'
image annie sad_mal="Annie_Act1_01_Sad.png"
image side annie= im.Scale('Nada.png', 0, 0, xoffset=-130, yoffset=600)
label contrasena_bien:
    "Decides ir al cañón con Annie"
    scene canon with fade
    show annie happy_bien with dissolve:
        xzoom 0.40 yzoom 0.40
        xpos 500 ypos 150
    "La plaza del cañón esta tan tranquila como siempre, y el viento es bastante acogedor"
    "Te preguntas donde puede estar la pista"
    annie "Separémonos un rato, para buscar la información"
    "Cada uno toma una dirección opuesta, y se colocan a buscar algo que parezca una pista."
    hide annie with easeoutright
    "Luego de un rato, decides tomar un descanso la centro de la plaza"
    "Te sientas un rato en el pasto, que fresquito se siente"
    "Por el rabillo del ojo, ves que Annie se acerca"
    show annie sad_mal with easeinright:
        xzoom 0.40 yzoom 0.40
        xpos 500 ypos 150
    annie "¿Qué tal te fue?"
    prota "Nada relacionado con la fiesta, ¿y a ti?"
    annie "Nada tampoco"
    prota "¿Nos habremos equivocado en la pista?"
    show annie pensativa with dissolve
    annie "No creo, que la respuesta fuera el cañón tenía mucho sentido"
    prota "El cañón..."
    "Piensas algo, que suena hasta ridículo"
    show annie normal with dissolve
    annie "¿Se te ocurrió algo interesante?"
    prota "Esto…., sé que te sonara ridículo, pero…¿Qué tal si la respuesta es el cañón?"
    show annie sorprendida with dissolve
    annie "¿A qué te refieres con eso?"
    prota "A que la respuesta esté en el cañón, o dentro, algo así"
    show annie muyfeliz with dissolve
    annie "Wow, no lo había pensado así, no perdemos nada intentando, vamos"
    "Te levantas y te acercas al cañón"
    scene canon2 with fade
    "A su alrededor no hay nada, esperable"
    show annie pensativa with easeinleft:
        xzoom 0.40 yzoom 0.40
        xpos 200 ypos 150
    annie "¿Y si metes la mano dentro?"
    prota "¿Crees qué si este dentro?"
    show annie normal with dissolve
    annie "No pierdes nada, dale nomás"
    "Algo dudoso aún, metes la mano dentro de la boca del cañón"
    "Al llegar al fondo, sientes algo entre tus dedos"
    "Temeroso, lo tomas, perece un papel"
    prota "Encontré algo"
    
    #musiquita de tloz please
    show annie sorprendida with dissolve
    show annie muyfeliz:
        yoffset 0
        easein 0.25 yoffset -100
        easeout 0.25 yoffset 0
        easein 0.2 yoffset -30
        easeout 0.2 yoffset 0
        easein 0.15 yoffset -10
        easeout 0.15 yoffset 0
        easein 0.1 yoffset -4
        easeout 0.1 yoffset 0
    "Annie parece estar saltando de la emoción"
    "Tomas el papel y lo abres"
    show annie muyfeliz with dissolve
    annie '¿Ah sí?, a ver, quiero verlo'
    "“Felicidades por encontrar esto, tu recompensa es la contraseña para la fiesta“"
    "Antes de llevarte el papel al bolsillo, lees:"
    "“Por favor deja el papel en el mismo lugar, para que otros aventureros como tú lo puedan encontrar“"
    "Haces como dice el papel y lo pones en la boca del cañón"
    "Le dices a Annie la contraseña y ella la anota"
    play sound "musiquita-pistas.mp3"
    show Pass:
        align (0.05 , 0.2)
    with dissolve
    show annie mirando_cel with dissolve
    annie "Listo, ya lo escribí"
    $PistaPassw = 'Contraseña.png'
    $pista+=1
    hide Pass with dissolve
    show annie happy_bien with dissolve
    if decisiones==1:
        annie "Nos quedan 2 cosas por buscar"
        jump primera_pista
    elif decisiones==2:
        annie "Nos queda 1 pista por encontar"
        jump segunda_pista
    elif decisiones==3:
        annie "No hay nada mas por buscar"
        jump tercera_pista

