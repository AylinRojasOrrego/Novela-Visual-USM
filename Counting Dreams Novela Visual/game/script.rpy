# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define annie = Character("Annie", color="#00ff04")
define prota = DynamicCharacter("MiNombre", color="#ff4d00")
image annie_normal="Annie_Act1_01.png"
image annie_happy_bien="Annie_Act1_02.png"
image annie_sad_mal="Annie_Act1_01_Sad.png"
image annie_phone="Annie_Act1_01_Phone.png"
image confesion="confesion.jpg"

image biblioteca="Stage_01.png"
image inicio= "inicio1.png"


$ MiNombre= ''
# The game starts here.

label start:
    scene inicio
    "Bienvenid@ a $Nombre Novela$"
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
    
    show annie_normal with easeinright:
        xzoom 0.40 yzoom 0.40
        xpos 500 ypos 100
    # These display lines of dialogue.
    annie "[MiNombre] ¿Cómo te fue en las pruebas?."

    menu:
        "Bien":
            "¡Bien! creo..."
            $ estado= "Bien"

        "Mal":
            "Mal, creo..."
            $ estado= "Mal"
    
    if estado=="Bien":
        show annie_happy_bien with dissolve:
            xzoom 0.40 yzoom 0.40
            xpos 500 ypos 100
        annie "¡Genial!, para celebrar, ¿qué te parece si me ayudas a resolver este acertijo que salió en las confesiones? "
        prota "¿A qué acertijo te refieres?"
        hide annie_happy_bien with dissolve
        show annie_phone with dissolve:
            xzoom 0.40 yzoom 0.40
            xpos 500 ypos 100

    elif estado=="Mal":
        show annie_sad_mal with dissolve:
            xzoom 0.40 yzoom 0.40
            xpos 500 ypos 100
        annie "Pucha que mal, oye, para animarte, ¿Y si me ayudas a resolver este juego de acertijos que salió en la página de confesiones? "
        prota "¿A qué acertijo te refieres?"
        hide annie_sad_mal with dissolve
        show annie_phone with dissolve:
            xzoom 0.40 yzoom 0.40
            xpos 500 ypos 100

    
    show confesion with dissolve:
        xpos 450 ypos 0
        xzoom 0.65 yzoom 0.62
    "..."
    hide confesion with dissolve

    hide annie_phone with dissolve
    show annie_happy_bien with dissolve:
        xzoom 0.40 yzoom 0.40
        xpos 500 ypos 100
    
    annie "¿Viste? Va a ser entretenido,vamos."
    prota "Está bien, está bien, vamos" 
    prota "Pero ¿Por dónde quieres empezar a buscar?"
    #inserte annie pensativa ajshdj
    annie "Uy, cierto, esto…"

    hide annie_happy_bien with dissolve
    show annie_normal with dissolve
    annie "no se escoge tú"

    menu:
        "❃Lugar❃":
            jump lugar
        "Hora[ℎ]":
            jump hora
        "Contraseña☶":
            jump contraseña



    # This ends the game.

    return
