def setup():
    size(600, 400)
    fill(0,153 ,153)
    rect(0, 350, 50, 50)  #this is the first boxx
    fill(0,215 ,153)
    rect(0, 300, 50, 50)#this is the second box
    fill(253, 100, 50)
    rect(50, 300, 50, 50) #this is the third box
    fill(50, 220, 115)
    rect(50, 350, 50, 50)
def mouseClicked():
   if mouseX <50 and mouseY >350:
       stroke(0, 153, 153)
   elif mouseX <50 and mouseY >300:
       stroke(0, 215, 153)
   elif mouseX >50 and mouseY >300:
       stroke(253, 100, 50)
   elif mouseX <50 and mouseY >350:
       stroke(50, 220, 115)
def draw():
     if mousePressed:
         line(pmouseX, pmouseY, mouseX, mouseY)
    
         

        
