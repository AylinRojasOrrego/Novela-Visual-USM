image side annie normal = im.Scale('Annie_Act1_01.png', 540, 910, xoffset=-130, yoffset=600)
image side annie triste = im.Scale('Annie_Act1_01_Sad.png', 540, 910, xoffset=-130, yoffset=600)
image side annie feliz = im.Scale('Annie_Act1_02.png', 540, 910, xoffset=-130, yoffset=600)

label hora_bien:
    #"aqui comienza la escena de la hora_bien"
    annie '¿Qué esperamos entonces? En marcha'
    'Te diriges con Annie hacia la cancha de la universidad'
    hide inicio with dissolve
    scene cancha with fade
    show annie_normal with dissolve:
        xzoom 0.50 yzoom 0.50
        xpos 700 ypos 150
    'Es bastante espaciosa, te preguntas como lo harán para encontrar un poster acá'
    prota 'Que amplio todo'
    show annie_pensativa with dissolve:
        xzoom 0.50 yzoom 0.50
        xpos 700 ypos 150
    hide annie_normal with dissolve
    annie 'Cierto, ¿cómo encontraremos una pista acá?, es mucho donde buscar.'
    prota 'Preguntemos a los alumnos que están acá en la cancha'
    show annie_sorprendida with dissolve:
        xzoom 0.50 yzoom 0.50
        xpos 700 ypos 150
    hide annie_pensativa with dissolve
    annie '¡Es verdad!'
    show annie_happy_bien with dissolve:
        xzoom 0.50 yzoom 0.50
        xpos 700 ypos 150
    hide annie_sorprendida with dissolve
    annie 'Quizá ellos vieron a alguien que pusiera la información'
    'Miras alrededor, hay un grupo trotando alrededor de la cancha, parecen ocupados, prefieres no molestarlos'
    annie 'Vayamos a preguntar al chico que está sentado bajo ese árbol, 
    no estará en la cancha en sí, pero está en sus cercanías, debe de haber visto algo.'
    'Aparte de chico, que parece estar estudiando o escuchando música, ves a alguien haciendo flexiones cerca de las banca'
    prota 'Yo quería preguntarle al de las gradas, parece que lleva un tiempo acá'
    annie 'Tú lideras, ¿A quién le preguntamos?'
    menu desición_pregunta:
        '¿A quién te dirigirás?'

        'Al de las bancas':
            'Vas con Annie a hablar con el chico de las flexiones'
            scene cancha_gradas with fade
            show derek flexiones with dissolve:
                xzoom 0.40 yzoom 0.40
                xpos 500 ypos 100
            annie normal 'Hola, disculpa si te molestamos, mi nombre es Annie'
            show derek sorprendido with dissolve
            derek '¡Oh! Hola, Me llamo Derek... y tú eres?'
            prota 'Mi nombre es [MiNombre]'
            show derek hablando with dissolve
            derek 'Un gusto. Justo estaba terminando ya. ¿Qué necesitan?'
            prota 'Mira, vimos que hay una fiesta, pero para entrar necesitas resolver algunos acertijos'
            annie normal 'Uno de estos acertijos nos trajo a la cancha, ¿sabrías algo tu?'
            show derek pensando with dissolve
            derek 'Fiesta... Acertijos...'
            annie triste '¿Se te ocurre algo?'
            show derek hablando with dissolve
            derek 'Si, de hecho, es mi amigo es que organizo esa fiesta'
            prota 'Genial, ¿sabrías cuál es la pista de la hora entonces?'
            show derek mostrando with dissolve
            derek 'En efecto, yo era el encargado de colocar la pista cerca de la cancha'
            'Annie le entrega su celular y Derek escribe la pista'
            derek 'Dereck: Ahí está escrita la pista'
            annie feliz '¡Oh!, muchas gracias '
            show derek hablando with dissolve
            derek 'No hay problema, ahora si me disculpan, debo colocar esta información'
            prota 'Muchas gracias, Dereck'
            show derek feliz with dissolve
            derek 'Encerio no es nada'
            derek 'espero nos veamos en la fiesta, estaré esperando!'
            show dereck feliz with easeoutright:
                xzoom 0.50 yzoom 0.50
                xpos 500 ypos 200
            'Dereck se marcha con una risa en su cara.'

            show annie_muyfeliz with dissolve:
                xzoom 0.40 yzoom 0.40
                xpos 500 ypos 150

            annie 'Genial, lo conseguimos'



            
            

return