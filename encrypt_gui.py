from tkinter import *  
from rsconv import Rs                                                     
import os  
from PIL import ImageTk, Image                                                                      


class EncryptGUI(Frame):
    
  def __init__(self, master=None):                                                         
      Frame.__init__(self, master, bd=25)                                                    
      self.grid()                                                                     
      self.createWidgets()                                                          
      self.e = None                                                                   
      self.userinput = ""                                                             
      self.result = ""                                                                
  def createWidgets(self):     
      path = 'test.jpeg'
      img = ImageTk.PhotoImage(Image.open(path))
      self.panel= Label(self, image = img)
      self.panel.image = img
      self.panel.grid(row=0, column=0, columnspan=4)
      
      self.it = Label(self)                                                           
      self.it["text"] = "Input the Rs Value"
      self.it["font"] = ('Helvetica', '18')                                                      
      self.it.grid(row=1, column=0, sticky=W)                                                   
      self.ifd = Entry(self)                                                           
      self.ifd.grid(row=1, column=1,                                                  
                    columnspan=2) 
      self.it2 = Label(self)                                                           
      self.it2["text"] = "(a.u.)"
      self.it2.grid(row=1, column=3, sticky=W)  

      self.ot = Label(self)                                                  
      self.ot["text"] = "Carrier Concentration"    
      self.ot["font"] = ('Helvetica', '18')                                              
      self.ot.grid(row=2, column=0, sticky=W)                                                   
      self.ofd = Entry(self)                                                                                                               
      self.ofd.grid(row=2, column=1,                                                  
                    columnspan=2)      
      self.ot2 = Label(self)                                                  
      self.ot2["text"] = "(cm^(-3)"                 
      self.ot2.grid(row=2, column=3, sticky=W) 

      self.ct = Label(self)                                                           
      self.ct["text"] = "Bandwidth"
      self.ct["font"] = ('Helvetica', '18')                                                      
      self.ct.grid(row=3, column=0, sticky=W) 
      self.ct2 = Label(self)                                                  
      self.ct2["text"] = "(eV)"                 
      self.ct2.grid(row=3, column=3, sticky=W)

      self.cfd = Entry(self)                                                           
      self.cfd.grid(row=3, column=1,                                                  
                    columnspan=2)  

      self.dt = Label(self)                                                           
      self.dt["text"] = ""
      self.dt.grid(row=4,column=1,columnspan=2)

                                                                                      
      self.eb = Button(self)                                                          
      self.eb["text"] = "Convert"  
      self.eb["font"] = ('Helvetica', '18')                                                     
      self.eb.grid(row=6, column=1)                                                   
      self.eb["command"] = self.em                                                    
      self.cb = Button(self)                                                          
      self.cb["text"] = "Clear"  
      self.cb["font"] = ('Helvetica', '18')                                                        
      self.cb.grid(row=6, column=2)                                                   
      self.cb["command"] = self.cm                                                    
                                                                                      
                                                 
                                                                                      
  def em(self):       
    

      self.userinput = self.ifd.get()                                                 
                                                                                
      # if self.userinput == "":                                                        
      #    m = "No input string!!"                                                      
      #    self.dt["text"] = m                                                          
      # else:                                                                           
      #     if self.e == None:                                                           
      #        m = "Nothing to do"                                                 
      #        self.dt["text"] = m                                                       
      #     else:                                                                        
      s = self.userinput                                                        
      r = Rs(s).concentration(s) 
      r1= Rs(s).bandwidth(s)                                              
      self.result = r                                                                 
      self.ofd.delete(0, 200)                                                   
      self.ofd.insert(0, r) 
      self.result = r1
      self.cfd.delete(0,200)
      self.cfd.insert(0,r1)

      m = "Successful Conversion"                                                  
      self.dt["text"] = m                                                       
                                                                                      
                                                     
                                                                                      
  def cm(self):                                                                      
      self.e = None                                                                   
      self.userinput = ""                                                             
      self.result = ""                                                                
      self.ifd.delete(0, 200)                                                         
      self.ofd.delete(0, 200)  
      self.cfd.delete(0, 200)                                                       
                                                                                      
      self.dt["text"] = "Cleared"                                                 
                                                                                      
                                                          
                                                                                      
if __name__ == '__main__':                                                            
   root = Tk()                                                                        
   root.title('Material Calculation')

   app = EncryptGUI(master=root)                                                      
   app.mainloop()                                                                     
                                                                                      

