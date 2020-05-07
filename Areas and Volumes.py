def arearectangle(w,h): #Area of rectangle input
      
      if float (w) < float(0): #Check to see if the imput is less than 0
         print ("Please try again with a positive number for width")
         
      elif float (h) < float(0): #Check to see if the imput is less than 0
         print ("Please try again with a positive number for height")

      else:
         area = float (w) * float (h) #Formula
         print ("The area of rectangle is:", str(area))


         
def areatriangle(w,h): #Area of triangle input

      if float (w) < float (0): #Check to see if the imput is less than 0
         print ("Please try again with a positive number for width")
         
      elif float (h) < float(0): #Check to see if the imput is less than 0
         print ("Please try again with a positive number for height")
                  
      else:
         area = float (w) * float (h) / 2 #Formula
         print ("The area of triangle is:", str(area))



def areacircle(r): #Area of circle input
      
      if float(r) < float (0): #Check to see if the imput is less than 0
         print ("Please try again with a positive number for radius")
                                   
      else:
         area = pow (float (r),2) #Formula
         print ("The area of circle is:" + str(area) + "*(pi)")



def areatrapezoid(a,b,h): #Area of trapezoid input

      if float (a) < float (0): #Check to see if the imput is less than 0
         print ("Please try again with a positive number for the top side")
      elif float (b) < float (0): #Check to see if the imput is less than 0
         print ("Please try again with a positive number for bottom side")
      elif float (h) < float (0): #Check to see if the imput is less than 0
         print ("Please try again with a positive number for h")
           
      else:
         area = (float (a) + float (b)) /2 * float( h) #Formula
         print ("The area of trapezoid is:", str(area)) 



def volsphere(r): #Volume of sphere input

      if float(r) < float (0): #Check to see if the imput is less than 0
         print ("Please try again with a positive number for radius")
         
      else:
            if (pow (r,3) % 3/4 ) == 0: #Fraction
                  volume = pow (r,3) 
                  print ("The volume of sphere is: " +str(volume))
            else:       
                  volume = pow (r,3) #Formula
                  print ("The volume of sephere is:" + str(volume) + "*4/3")



        
def volsquarepyramid(a,h): #Volume of square pyramid input
   
      if float (a) < float (0): #Check to see if the imput is less than 0
         print ("Please try again with a positive number for side")
      elif float (h) < float (0): #Check to see if the imput is less than 0
         print ("Please try again with a positive number for height")
         
      else:
         if (pow(a,2) * (h) % 3) == 0: #Fraction
            volume = pow(a,2) * (h/3)
            print ("The volume of square pyramid is: " +str(volume))
            
         else:
            volume = pow (float(a) ,2) * float(h) #Formula
            print ("The volume of square pyramid is:" + str(volume) +"/3")


                    
def volrectangularprism(w,h,l): #Volume of rectangular prism input
  
      if float (w) < float (0): #Check to see if the imput is less than 0
         print ("Please try again with a positive number for width")
      elif float (h) < float (0): #Check to see if the imput is less than 0
         print ("Please try again with a positive number for height")
      elif float (l) < float (0): #Check to see if the imput is less than 0
         print ("Please try again with a positive number for lengh")
         
      else:
         volume = float(w) * float (h) * float (l) #Formula  
         print ("The volume of rectangular prism is:", str(volume))
        


def volcone(r,h): #Volume of cone input

      if float (r) < float (0): #Check to see if the imput is less than 0
         print ("Please try again with a positive number for radius")
      elif float (h) < float (0): #Check to see if the imput is less than 0
         print ("Please try again with a positive number for height")
         
      else:
         if (pow(r,2) * (h) % 3) == 0: #Fraction
            volume = pow(r,2) * (h/3)
            print ("The volume of cone is: " +str(volume)+ "*(pi)")
            
         else:
            volume = pow (float(r) ,2) * float(h) #Formula 
            print ("The volume of cone is:" + str(volume) + "*(pi)" +"/3")



def volcylinder(r,h): #Volume of cylinder input
   
      if float (r) < float (0): #Check to see if the imput is less than 0
         print ("Please try again with a positive number for radius")
      elif float (h) < float (0): #Check to see if the imput is less than 0
         print ("Please try again with a positive number for height")
         
      else:
         volume = float (r) ** 2 * float (h) #Formula
         print ("The volume of cylinder is:" + str(volume) + "*(pi)")
