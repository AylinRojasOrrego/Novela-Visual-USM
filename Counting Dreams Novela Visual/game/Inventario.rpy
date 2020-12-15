screen MI:
    frame:
        align (0, 0) #posicion
        textbutton "Abrir   " action [Show ("Inventario"), Hide ("MI")]
    

    

screen Inventario:
    #add "gui/overlay/confirm.png" #opcional overlay
    
    add "Inventario.png" xzoom 0.5 yzoom 0.5 align (0, 0.05)
    modal True
    
    
    
    frame:
        align (0, 0)
        textbutton "Cerrar " action [ Hide ("Inventario"), Show ("MI")]
        
    frame:
        align (0, 0.3)
        text "Inventario"  
    #seccion izquierda
    add "[PistaHora]" xpos 0.02 ypos 0.075 xzoom 0.4 yzoom 0.4
    add "[PistaLugar]" xpos 0.141 ypos 0.075 xzoom 0.4 yzoom 0.4
    add "[PistaContraseña]" xpos 0.27 ypos 0.075 xzoom 0.4 yzoom 0.4