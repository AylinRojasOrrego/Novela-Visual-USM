﻿# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the
# name of the character.
define prota = DynamicCharacter("MiNombre", color="#ff4d00")

define annie = Character("Annie", color="#00ff04",image='annie')
image annie normal="Annie_Act1_01.png"
image annie happy_bien="Annie_Act1_02.png"
image annie sad_mal="Annie_Act1_01_Sad.png"
image annie phone="Annie_Act1_01_Phone.png"
image annie muyfeliz ="Annie_Act1_02_Buena Desicion.png"
image annie muymal = 'Annie_Act1_02_Mala Desicion.png'
image annie pensativa ='Annie_Act1_02_Pensativa.png'
image annie sorprendida ='Annie_Act1_02_Sorprendida.png'
image annie mirando_cel='Annie_ActLugar_VerCelular.png'

define derek = Character('Derek',color ='#8E0A38', image='derek')
image derek flexiones='Dereck_ActHora_DespuesFlexiones.png'
image derek sorprendido='Dereck_ActHora_Sorprendido.png'
image derek hablando='Dereck_ActHora_Respondiendo.png'
image derek feliz='Dereck_ActHora_RespondiendoFeliz.png'
image derek mostrando='Dereck_ActHora_Señalando.png'
image derek pensando='Dereck_ActHora_Pensando.png'

define kylie = Character('Kylie', color='EE54FF', image='kylie')
image kylie leyendo='Kylie_ActHora_Leyendo.png'
image kylie hablando='Kylie_ActHora_Hablando.png'
image kylie ignorando ='Kylie_ActHora_Ignorando.png'
image kylie mirando='Kylie_ActHora_Mirando.png'
image kylie riendo='Kylie_ActHora_Riendo.png'
image kylie negando='Kylie_ActHora_Negando.png'

image confesion="confesion.jpg"

image Hora='Hora.png'
image Lugar='Lugar.png'
image Pass='Contraseña.png'

define PistaHora ='Nada.png'
define PistaLugar ='Nada.png'
define PistaContraseña ='Nada.png'

image biblioteca="Stage_01.png"
image inicio= "inicio1.png"
image playa= "playita.png"
image piscina = "piscina.png"
image pasillo1= "pasillo_piscina.png"
image cancha='Cancha.png'
image cancha_bancas='Cancha_bancas.png'
image cancha_gradas='Cancha_gradas.png'
image plaza='Hora_plaza.png'
image calle="Terraza.png"
image canon='cañon.png'
image avenida=''

$ desicion1= ''
$ desicion2= ''
$ desicion3= ''  
$ MiNombre= ''

#  Desiciones erradas
$Hora=True
$Lugar=True
$Contraseña=True


# The game starts here.

label start:
    $ items=[]
    $ showitems= False
    scene inicio
    
    "Bienvenid@ a Una fiesta entre pistas"
    "Antes de comenzar con la historia, debemos hacerte unas preguntas..."
    "¿Eres Chica o Chico?"
    menu:
        "♀️ Chica ♀️":
            'Bien. Por ultimo...'
            $ genero= 'Chica'
        "♂️ Chico ♂️":
            "Bien. Por ultimo..."
            $ genero= "Chico"
    "¿Cómo te llamas?"
    $ MiNombre = renpy.input(" ")
    prota "Me llamo [MiNombre]"
    
    "Muy bien [MiNombre], comencemos con esta aventura"

    scene biblioteca
    prota "Ha sido una semana difícil, pero he logrado pasar mis certámenes"
    prota "Quizá deba tomarme un descanso, ir a caminar o…"
    prota "Ah mira, ahí viene Annie, ¿le habrá ido bien en su presentación?"
    
    show annie normal with easeinright:
        xzoom 0.40 yzoom 0.40
        xpos 500 ypos 100
    # These display lines of dialogue.

    annie "Wena [MiNombre] ¿Cómo te fue en las pruebas?."
    menu:
        "Bien":
            "¡Bien! creo..."
            $ estado= "Bien"

        "Mal":
            "Mal, creo..."
            $ estado= "Mal"
    
    if estado=="Bien":
        show annie happy_bien with dissolve
        annie "¡Genial!, para celebrar, ¿qué te parece si me ayudas a resolver este acertijo que salió en las confesiones? "
        prota "¿A qué acertijo te refieres?"
        show annie phone with dissolve

    elif estado=="Mal":
        show annie sad_mal with dissolve
        annie "Pucha que mal, oye, para animarte, ¿Y si me ayudas a resolver este juego de acertijos que salió en la página de confesiones? "
        prota "¿A qué acertijo te refieres?"
        show annie phone with dissolve

    show screen MI

    show confesion with dissolve:
        xpos 450 ypos 0
        xzoom 0.65 yzoom 0.62
    "..."
    hide confesion with dissolve

    show annie happy_bien with dissolve
        
    annie "¿Viste? Va a ser entretenido,vamos."
    prota "Está bien, está bien, vamos"
    $showitems= True
    prota "Pero ¿Por dónde quieres empezar a buscar?"

    show annie pensativa with dissolve
    annie "Uy, cierto, esto…"

    show annie normal with dissolve
    annie "No se, escoge tú."
                

    menu: 
        "❃Lugar❃":
            $ decision1= "lugar"
            $ decisiones=1
            $ pista=0
            jump lugar
        "Hora[ℎ]":
            $ decision1= "hora"
            $ decisiones=1
            $ pista=0
            jump hora 
        "Contraseña☳":
            $ decision1= "contraseña"
            $ decisiones=1
            $ pista=0
            jump contraseña 
    
    label primera_pista:
        if pista==1:
            prota "Ahora, ¿Qué podemos buscar?"
            annie "Escogiste bien ahora, escoge de nuevo"
        elif pista==0:
            annie "Vaya, no pudimos encontrar nada, pasemos a otro acertijo."

        if decision1=="lugar":
                menu:
                    annie"Tenemos estas opciones"
                    "Hora[ℎ]":
                        $ decision2= "hora"
                        $ decisiones+=1
                        jump hora
                    "Contraseña☳":
                        $ decision2= "contraseña"
                        $ decisiones+=1
                        jump contraseña
        elif decision1=="hora":
                menu:
                    annie"tenemos estas opciones"
                    "❃Lugar❃":
                        $ decision2= "lugar"
                        $ decisiones+=1
                        jump lugar
                    "Contraseña☳":
                        $ decision2= "contraseña"
                        $ decisiones+=1
                        jump contraseña
        elif decision1=="contraseña":
                menu:
                    annie"Tenemos estas opciones"
                    "❃Lugar❃":
                        $ decision2= "lugar"
                        $ decisiones+=1
                        jump lugar
                    "Hora[ℎ]":
                        $ decision2= "hora"
                        $ decisiones+=1
                        jump hora

    label segunda_pista:
        if pista==2:
            annie "Vas muy bien, sigamos así"
        elif pista<2:
            annie "Vaya, no pudimos encontrar nada, pasemos a otro acertijo."
        if (decision2=="lugar" and decision1=='hora') or (decision1=="lugar" and decision2=='hora'):
                menu:
                    annie"Tenemos esta opción"
                    "Contraseña☳":
                        $ decision3= "contraseña"
                        $ decisiones+=1
                        jump contraseña
        elif (decision2=="lugar" and decision1=='contraseña') or (decision1=="lugar" and decision2=='contraseña'):
                menu:
                    annie"Tenemos esta opción"
                    "Hora[ℎ]":
                        $ decision3= "hora"
                        $ decisiones+=1
                        jump hora

        elif (decision2=="hora" and decision1=='contraseña') or (decision1=="hora" and decision2=='contraseña'):
                menu:
                    annie"Tenemos esta opción"
                    "❃Lugar❃":
                        $ decision3= "lugar"
                        $ decisiones+=1
                        jump lugar
    label tercera_pista:
        prota "Ya hemos revisado todo"
        annie "Veamos que podemos hacer con lo que tenemos"
        if pista==3:
            annie "Genial, lo tenemos todo"
            prota "¡Sí!, lo logramos, fue bastante entretenido"
            annie "Me divertí mucho, gracias por acompañarme"
            prota "Bueno, a usar nuestras pistas, vamos a la fiesta"
            annie "Claro, vamos en camino"
        elif pista==2:
            show annie sad_mal with dissolve
            annie "Vaya, parece que no tenemos más tiempo para buscar más pistas"
            'En conjunto van a la entrada de la Universidad'
            scene avenida with fade
            show annie sad_mal with easeinright:
                xzoom 0.50 yzoom 0.50
                xpos 700 ypos 150
            protA '¿Crees que lo lograremos con lo que tenemos?'
            show annie pensativa with dissolve
            annie 'Hmm, estaba pensando la última'
            annie 'Cuando nos separamos pude encontrar la que nos faltaba'
            show annie happy_bien with dissolve
            annie 'Aquí la tengo'

            if Hora==False:
                show Hora:
                    align (0.2 , 0.2)
                with dissolve

                $PistaHora = 'Hora.png'
                $pista+=1

                prota '¡Que lista eres Annie!'
                show annie muyfeliz with dissolve
                annie 'No es nada [MiNombre], detective Annie al rescate'
                prota 'Bueno detective, tenemos una fiesta a la que atender'
                jump GoodEnding


            elif Lugar==False:
                show Lugar:
                    align (0.2 , 0.2)
                with dissolve

                $PistaLugar = 'Lugar.png'
                $pista+=1

                prota '¡Que lista eres Annie!'
                show annie muyfeliz with dissolve
                annie 'No es nada [MiNombre], detective Annie al rescate'
                prota 'Bueno detective, tenemos una fiesta a la que atender'
                jump GoodEnding

            elif Contraseña==False:
                show Pass:
                    align (0.2 , 0.2)
                with dissolve

                $PistaLugar = 'Contraseña.png'
                $pista+=1
                prota '¡Que lista eres Annie!'
                show annie muyfeliz with dissolve
                annie 'No es nada [MiNombre], detective Annie al rescate'
                prota 'Bueno detective, tenemos una fiesta a la que atender'
                jump GoodEnding
                


        elif pista<=1:
            prota "Vaya, nos fue bastante mal"
            annie "Si..."
            prota "Quiza deberiamos haber buscado en otros lugares"
            annie "Que mal, no pude sacar a luz mis habilidades de detective"
            prota "Oye Annie, no te preocupes tanto por eso"
            prota "Puede que no podamos ir a la fiesta, pero recuerda que tenemos una serie pendiente"
            annie "Oh ,cierto, estábamos en la mejor parte"
            prota "¿Quién crees que sea el asesino?"
            show annie pensativa with dissolve
            annie " Así como está la historia ahora…y las pistas que han dejado en las escenas post créditos.., siento que puede ser…."
            "A pesar de no poder ir a la fiesta, decides pasar la noche en casa de Annie, resolviendo crímenes de una serie de televisión"
            "Puedes volver a jugar esta historia, para resolver el acertijo e ir a la fiesta"
            "Suerte!"
            return
        
    # This ends the game.

    return
