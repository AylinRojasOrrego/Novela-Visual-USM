# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define annie = Character("Annie", color="#00ff04")
define prota = DynamicCharacter("MiNombre", color="#ff4d00")
image annie_normal="Annie_Act1_01.png"
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
    prota "*Suspiro*"
    prota "Ha sido una semana difícil"
    prota "Quizá deba tomarme un descanso, ir a caminar o…"
    "A la distancia, puedes ver que Annie, tu compañera de carrera se acerca a ti"
    prota "Ah mira, ahí viene Annie, ¿le habrá ido bien en su presentación?"
    "Annie, se acerca a ti con su celular en la mano, parece que desea mostrarte algo"
    show annie_normal with dissolve:
        xzoom 0.40 yzoom 0.40
        xpos 500 ypos 200
    # These display lines of dialogue.
    annie "Wena [MiNombre] ¿Cómo te fue en las pruebas?."
    menu:
        "Bien, espero.":
            annie "¡Genial!, para celebrar, ¿qué te parece si me ayudas a resolver este acertijo que salió en las confesiones?"
        "Mal, creo.":
            annie "Pucha que mal, oye, para animarte, ¿Y si me ayudas a resolver este acertijo que salió en la página de confesiones?"

    # This ends the game.

    return
