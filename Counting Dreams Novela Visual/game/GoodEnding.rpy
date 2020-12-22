image side annie ok = im.Scale('Annie_Act1_01.png', 540, 910, xoffset=-130, yoffset=600)
image side annie feliz = im.Scale('Annie_Act1_02.png', 540, 910, xoffset=-130, yoffset=600)
image side annie muchofeliz = im.Scale('Annie_muyfeliz.png', 540, 910, xoffset=-130, yoffset=600)
image side annie= im.Scale('Nada.png', 0, 0, xoffset=-130, yoffset=600)

label GoodEnding:
    'Te diriges al Patio del Cañón, donde las pistas te dijeron que era el lugar indicado'
    $PistaLugar = 'Nada.png'
    scene canonfiesta with fade
    'Tu y Annie llegan a la hora indicada al lugar, pero esta muy oscuro...'
    $PistaHora = 'Nada.png'
    prota 'Se siente un poco vacío...'
    show annie normal with easeinright:
        xzoom 0.40 yzoom 0.40
        xpos 500 ypos 150
    annie 'Ya estamos en el cañón y a la hora indicada'
    prota '¿Dónde está el resto?'
    hide annie with dissolve
    'Te paseas un rato, pero no ves a nadie'
    prota 'Que raro, si esto es lo que indican las pistas'
    'En ese momento escuchas la voz grave viniendo de atrás'
    nadie '¿Encontraron las pistas?'
    'No puedes distinguir totalmente, pero la silueta que se dibuja parece bastante alta'
    prota 'Si, como puedes ver, llegamos al lugar indicado y a la hora indicada'
    'La persona se acerca un poco más y la figura es un poco más visible'
    show cedric serio with dissolve:
        xzoom 0.40 yzoom 0.40
        xpos 450 ypos 70
    annie ok 'Ah, es Cedric, Hola!'
    show cedric normal with dissolve
    cedric 'oh, Annie, sabría que vendrías, no dejarías pasar una “investigación” ¿Cómo estás?'
    prota '¿De dónde se conocen?'
    annie feliz 'Éramos grupo de laboratorio, hasta que nos cambiaron.'
    cedric 'Sep, ojala te trate bien tu nuevo equipo, pero volviendo al tema, ¿Tienen la contraseña?'
    show cedric escuchando with dissolve
    prota 'Claro, claro'
    annie muchofeliz 'La contraseña es “Prestigio”'
    $PistaPassw = 'Nada.png'
    show cedric escuchandofeliz with dissolve
    cedric 'Excelente trabajo, entren y disfruten de los frutos de su búsqueda'
    'Cedric les muestra el camino hacia en verdadero lugar de la fiesta'
    stop music fadeout 5.0

    scene fiesta with fade
    play music "fiesta.mp3"
    'Entras con Annie al salón, hay un ambiente bastante motivador'
    'La música te lleva a dimensiones que ni sabias que existían'
    show derek hablando with easeinright:
        xzoom 0.50 yzoom 0.50
        xpos 650 ypos 100
    derek 'Hola Chicos, que bueno verlos por aquí'
    annie ok '¡Derek! estás aquí, que lindo que nos encontramos'
    prota 'Si... Gracias a ti pudimos encontrar una de las pistas y logramos decifrar la hora'
    show derek feliz with dissolve
    derek 'No fue nada, era parte de mi trabajo jeje'
    'En medio de la conversación ves como se acerca una figura conocida'
    show cedric normal with easeinleft:
        xzoom 0.50 yzoom 0.50
        xpos 150 ypos 50
    cedric '¡Hey! acabo de conseguir un tiempo de descanso de la portería'
    cedric '¿Me dejarían pasar el rato con ustedes?'
    show derek hablando with dissolve
    prota 'Por supuesto, quedate con nosotros este es Derek'
    annie feliz 'Mientras más, mejor'
    show cedric feliz with dissolve
    cedric 'Genial... Hola mi nombre es Cedric, un gusto'
    show derek mostrando with dissolve
    derek 'El placer es mio'
    annie muchofeliz 'Esta noche será maravillosa, no es así [MiNombre]?'
    prota 'Tienes razón Annie... Lo será'
    scene fiesta with dissolve
    'Las horas pasan volando, y bailaste cada segundo que pudiste'
    'El ambiente ya se esta tranquilizando'
    show annie normal with dissolve:
        xzoom 0.50 yzoom 0.50
        xpos 500 ypos 150
    annie 'Wow, esto fue muy entretenido'
    prota 'Siii... sirvió harto para relajarnos de los certámenes'
    show annie happy_bien with dissolve
    annie 'Ojala hicieran esto de buscar pistas mas seguido'
    prota 'No creo que todos tengan nuestro tiempo'
    annie 'Cierto, en todo caso, ya como que es la hora de irnos'
    'Revisas tu celular, tiene poca batería y es casi de madrugada'
    prota 'Cierto, retirémonos por ahora'
    'Te despides de los amigos que hiciste en esta travesia, sales del salón con Annie y ambos parten una caminata hacia sus hogares'
    stop music fadeout 5.0
    play music 'night.mp3'
    scene final with fade

    'La noche esta tranquila y tienes una conversación placentera con Annie'
    'Al momento de separar caminos, Annie se despide con un beso en la mejilla'
    'Llegas a tu hogar y te recuestas en tu cama, tienes que esa fue una noche para recordar'
    scene negro with fade
    stop music fadeout 5.0
    'Y así mismo te quedas dormido lleno de emocion y felicidad para afrontar lo que sea...'
    

