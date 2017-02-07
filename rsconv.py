from numpy import *


class Rs:
   def __init__(self, str):                       
     self.str=str

   def concentration(self, str):
   	 a1=(float)(self.str)*0.52918*power(10.0,-8)
   	 result=3.0/(4.0*pi*power(a1,3.0))
   	 return float32(result) 
     
   def bandwidth(self, str):
     k=power(9.0*pi/4.0,1.0/3.0)/float(self.str) 
     result=k*k/2*27.211
     return float32(result)



if __name__ == '__main__':                             
   s2=""
   s3=""
   e = Rs(2.07)                                       
   s2=e.concentration(2.07)
   s3=e.bandwidth(2.07)
   print(s2,s3)
   

                                                                                          
                
