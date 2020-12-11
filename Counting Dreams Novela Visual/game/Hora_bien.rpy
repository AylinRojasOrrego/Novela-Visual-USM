image side annie ok = im.Scale('Annie_Act1_01.png', 540, 910, xoffset=-130, yoffset=600)
image side annie triste = im.Scale('Annie_Act1_01_Sad.png', 540, 910, xoffset=-130, yoffset=600)
image side annie feliz = im.Scale('Annie_Act1_02.png', 540, 910, xoffset=-130, yoffset=600)
image side annie = im.Scale('Annie_Act1_02.png', 0, 0, xoffset=-130, yoffset=600)
label hora_bien:
    #"aqui comienza la escena de la hora_bien"
    annie '¿Qué esperamos entonces? En marcha'
    'Te diriges con Annie hacia la cancha de la universidad'
    hide inicio with dissolve
    scene cancha with fade
    show annie normal with dissolve:
        xzoom 0.50 yzoom 0.50
        xpos 700 ypos 150
    'Es bastante espaciosa, te preguntas como lo harán para encontrar un poster acá'
    prota 'Que amplio todo'
    show annie pensativa with dissolve
    annie 'Cierto, ¿cómo encontraremos una pista acá?, es mucho donde buscar.'
    prota 'Preguntemos a los alumnos que están acá en la cancha'
    show annie sorprendida with dissolve
    annie '¡Es verdad!'
    show annie happy_bien with dissolve
    annie 'Quizá ellos vieron a alguien que pusiera la información'
    'Miras alrededor, hay un grupo trotando alrededor de la cancha, parecen ocupados, prefieres no molestarlos'
    show annie muyfeliz with dissolve
    annie 'Vayamos a preguntar la chica que está leyendo bajo ese árbol, 
    no estará en la cancha en sí, pero está en sus cercanías, debe de haber visto algo.'
    'Aparte de la joven, que parece estar estudiando, ves a alguien haciendo flexiones cerca de las gradas'
    prota 'Yo quería preguntarle al de las gradas, parece que lleva un tiempo acá'
    annie 'Tú lideras, ¿A quién le preguntamos?'
    menu desición_pregunta:
        '¿A quién te dirigirás?'

        'Al de las gradas':
            'Vas con Annie a hablar con el chico de las flexiones'
            scene cancha_gradas with fade
            show derek flexiones with dissolve:
                xzoom 0.40 yzoom 0.40
                xpos 500 ypos 100
            annie ok 'Hola, disculpa si te molestamos, mi nombre es Annie'
            show derek sorprendido with dissolve
            derek '¡Oh! Hola, Me llamo Derek... y tú eres?'
            prota 'Mi nombre es [MiNombre]'
            show derek hablando with dissolve
            derek 'Un gusto. Justo estaba terminando ya. ¿Qué necesitan?'
            prota 'Mira, vimos que hay una fiesta, pero para entrar necesitas resolver algunos acertijos'
            annie ok 'Uno de estos acertijos nos trajo a la cancha, ¿sabrías algo tu?'
            show derek pensando with dissolve
            derek 'Fiesta... Acertijos...'
            annie triste '¿Se te ocurre algo?'
            show derek hablando with dissolve
            derek 'Si, de hecho, es mi amigo es que organizo esa fiesta'
            prota 'Genial, ¿sabrías cuál es la pista de la hora entonces?'
            show derek mostrando with dissolve
            derek 'En efecto, yo era el encargado de colocar la pista cerca de la cancha'
            'Annie le entrega su celular y Derek escribe la pista'

            show Hora:
                align (0.2 , 0.2)
            with dissolve

            $hr ='22:30[hrs]'

            $PistaHora = 'Hora.png'

            $pista+=1

            annie feliz '¡Oh!, muchas gracias '

            hide Hora with dissolve

            show derek hablando with dissolve
            derek 'No hay problema, ahora si me disculpan, debo colocar esta información'
            prota 'Muchas gracias, Dereck'
            show derek feliz with dissolve
            derek 'Encerio no es nada'
            derek 'espero nos veamos en la fiesta, estaré esperando!'
            hide derek with easeoutright
            'Dereck se marcha con una risa en su cara.'

            show annie muyfeliz with easeinleft:
                xzoom 0.40 yzoom 0.40
                xpos 500 ypos 150
            
            annie 'Genial, lo conseguimos'
            prota "Buena, tenemos la respuesta"
            show annie muyfeliz with dissolve
            if decisiones==1:
                annie "nos quedan 2 cosas por buscar"
                jump primera_pista
            elif decisiones==2:
                annie "nos queda 1 pista por encontar"
                jump segunda_pista
            elif decisiones==3:
                annie "No hay nada mas por buscar"
                jump tercera_pista
        


        'A la que estudia':
            'Crees que la chica que está estudiando haya visto pasar más gente que puede haber colocado la información...'
            scene cancha_bancas with fade
            show kylie leyendo with dissolve:
                xzoom 0.40 yzoom 0.40
                xpos 400 ypos 100
            prota 'Disculpa'
            'La chica no te escucha'
            annie ok 'Oye, ¿te molestamos?'
            show kylie mirando with dissolve
            'La chica parece haber escuchado eso, pues te mira directamente'
            show kylie hablando with dissolve
            kylie '¿Qué quieren?'
            prota 'Queremos saber si has visto a alguien colocando información sobre una fiesta'
            show kylie riendo with dissolve
            kylie 'Pff... fiestas ¿Quién tiene tiempo para eso?'
            annie triste '¿Es eso un no?'
            show kylie negando with dissolve
            kylie '¡Exacto! Ahora por favor vayanse'
            show kylie ignorando with dissolve
            kylie 'Que matemáticas no se pasa solo'
            hide kylie with dissolve
            'Dejan tranquila a la joven'
            show annie sad_mal with easeinright:
                xzoom 0.40 yzoom 0.40
                xpos 400 ypos 100
            annie 'Parece que no la pillamos en su mejor día'
            prota 'todavía le podemos preguntar al otro chico'
            'Miras a donde estaba el otro chico, ni él ni sus cosas están'
            show annie muymal with dissolve
            annie 'Vaya, parece que se ha ido'
            prota 'Supongo que no encontramos esta pista entonces'
            if decisiones==1:
                show annie happy_bien with dissolve
                annie "Continuemos con el resto entonces"
                jump primera_pista
            elif decisiones==2:
                show annie happy_bien with dissolve
                annie "Continuemos con el resto entonces"
                jump segunda_pista
            elif decisiones==3:
                show annie sad_mal
                annie "Ya no queda más que investigar"
                jump tercera_pista
        





            
            

return