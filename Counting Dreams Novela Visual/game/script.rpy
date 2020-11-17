# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define annie = Character("Annie", color="#FF5C00")
image annie_normal="Annie_Act1_01.png"
image biblioteca="Stage_01.png"

# The game starts here.

label start:
    scene biblioteca

    show annie_normal:
        xzoom 0.40 yzoom 0.40
        xpos 500 ypos 200
    # These display lines of dialogue.
    annie "Wena,¿Cómo estás? ¿Cómo te fue en las pruebas?."

    # This ends the game.

    return
