# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define annie = Character("Annie", color="#FF5C00")
define prota = DynamicCharacter("MiNombre", color="#00ffbb")
image annie_normal="Annie_Act1_01.png"
image biblioteca="Stage_01.png"

$ MiNombre= ''
# The game starts here.

label start:
    scene biblioteca
    
    "Bienvenid@ a $Nombre Novela$"
    "Antes de comenzar con la historia, debemos hacertes unas preguntas"
    "¿Eres Chica o Chico?"
    menu:
        "Chica":
            'Bien. Por ultimo...'
            $ genero= 'Chica'
        "Chico":
            "Bien. Por ultimo..."
            $ genero= "Chico"
    "¿Cómo te llamas?"
    $ MiNombre = renpy.input(" ")
    prota "Me llamo [MiNombre]"
    show annie_normal:
        xzoom 0.40 yzoom 0.40
        xpos 500 ypos 200
    # These display lines of dialogue.
    annie "[MiNombre],¿Cómo estás? ¿Cómo te fue en las pruebas?."

    # This ends the game.

    return
