# You can place the script of your game in this file.
# - Puedes colocar el 'script' de tu juego en este archivo.

# Declare images below this line, using the image statement.
# - Declara imágenes bajo esta línea, usando 'image' como
#   en el ejemplo.
# eg. image eileen happy = "eileen_happy.png"

image m = "mart.png"
image c = "Clara.png"
image d = "daniel.png"
image habitacion = "habitacion.jpg"
image cole = "colegio.jpg"
image clase = "clase.jpg"
image casa = "casa.jpg"

# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el 
#   ejemplo.

define m=Character('Mart', color="#FFFFFF")
define c=Character('Clara', color="#FF0000")
define d=Character('Daniel',color="#9966CC")





# The game starts here.
# - El juego comienza aquí.
label start:
    
    stop music
    
    scene habitacion
    play music "art1.mp3"
    
    show m
    with dissolve 
    
    
    m"Hola"
    show m:
        ypos 750 xpos 1100
        
    with dissolve
    
    m "Mira esta es mi habitacion"
    
    m "AAAAAAH voy tarde al colegio."
    
    m "¿Voy a colegio o mejor me quedo?"
    
menu:
        
    "Ire al colegio porque soy responsable.":
                    jump a
    "Me quedo a domir.":
                    jump b
                    
label a:
         m "Bueno ire al colegio n_n"
         
         hide m
         
         scene cole
         with dissolve
         
         show m
         with dissolve
         
         m "Hace calor."
         m "Pero me siento bien y con energias de ir a clases ^.^"
         hide m
         scene clase
         with vpunch
         
         show m:
             ypos 50 xpos 500
         with dissolve
         m "Waaaaaaa terremoto."
         m"Esto fue muy raro"
         
         show d:
             ypos 50 xpos -400
         with dissolve
         d"¿Oye estas bien?"
         m "Si gracias ^.^"
         
         hide d
         hide m
         
         scene casa
         with dissolve
         
         show m
         with dissolve
         m "Fue un dia normal."
         m "Excepto por el terremoto."
         m "Espero que no vuelva a pasar."
         m "Bueno nos vemos."
         
       
        
        
return
         
        
        
      
            
            
         

         
         
         

         
         
label b:
    
        show c:
            ypos 100 xpos -500 
        
        with vpunch
        c "NOOOOOOOO"
        
        
        c "Hermano tienes que ir al colegio "
        
        m "¿Tu otra vez? e.e"
        
        c "Le dire a mama si no vas al colegio."
        
        m "Esta bien tranquila."
        
        m "Ire al colegio."
        
        hide c
        hide m
        
        

        
        scene cole
        with dissolve
        
        show m
        with dissolve
         
        m "Que calor! D:"
        m "Espero que este dia pase rapido"
        m "Waaaaa esta cancion ya me aburrio."
        m "Pondre otra >.<"
         
        stop music 
        
        play music "art2.mp3"
        
        pause 
         
        m "Mucho mejor ^.^"
        
        m "Ahora si vamos al cole"
        
        hide m
        
        scene clase
        with dissolve
        
        show d
        with vpunch
        
        
        d "OYE HICISTE LA TAREA? D:" 
        hide d
        show d:
            ypos 50 xpos -400
        with dissolve
        
        show m:
            ypos 50 xpos 500
        
        with dissolve
        
        m "¿Habia tarea ? e.e "
        
        d "Bueno espero que nadie le recuerde al profesor que habia tarea."
        
        hide d
        hide m
        scene casa
        with dissolve
        show m 
        m "Bueno un dia muy aburrido."
        m "Pero por fin estoy en casa."
        m "Nos vemos >.< "
        m "Cuidense."
        
        
        
        
        
        
        
        return
        
        
        
        
        
        
        
        
        
        
       
        
        
        
    
    
    
        
        
        

        
        
    
    

    
        
        
    
return
    
