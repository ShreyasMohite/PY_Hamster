from tkinter import *
from PIL import ImageTk
from PIL import *
from tkinter.ttk import Progressbar
import tkinter.messagebox
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests,re,os,time,random     



class xhamster:
     def __init__(self,root):
          self.root=root
          self.root.title("XHAMSTER PIcs ;)")
          self.root.geometry("500x300")
          self.root.resizable(0,0)
          self.root.iconbitmap("ham.ico")


          xurls=StringVar()


#===========================================================================

          def on_enter1(e):
            Down_but['background']="black"
            Down_but['foreground']="cyan"
  
          def on_leave1(e):
            Down_but['background']="SystemButtonFace"
            Down_but['foreground']="SystemButtonText"



          def on_enter2(e):
            Clear_but['background']="black"
            Clear_but['foreground']="cyan"
  
          def on_leave2(e):
            Clear_but['background']="SystemButtonFace"
            Clear_but['foreground']="SystemButtonText"


#=============================================================================

          def clear():
               xurls.set("")

          def download_xhamster():
               site=xurls.get()

               if xurls.get()=="":
                    tkinter.messagebox.askretrycancel("Error","please paste url")

               else:
                    try:
                         
                         prg.start(10)
                         parent="C:\\Users\\SHREYAS\\Desktop\\shreyas python\\HamsterBoy"
                         num=random.randint(1,100)
                         dirs="Xhamster{}".format(num)
                         path=os.path.join(parent,dirs)
                         os.mkdir(path)
                         response=requests.get(site)
                         Soup=BeautifulSoup(response.text,"html.parser")
                         gather=Soup.findAll("div" ,class_="image-thumb")
                         urls=[images["data-lazy"] for images in gather]
                         for url in urls:
                             filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
                             if not filename:
                                  
                                  statusbar.config(text="Regex didn't match with the url: {0}".format(url))
                                  self.root.update()
                                  continue
                             with open(path+"\\"+filename.group(1), 'wb') as f:
                                 if 'http' not in url:
                                     # sometimes an image source can be relative 
                                     # if it is provide the base url which also happens 
                                     # to be the site variable atm.
                                     url = '{}{}'.format(site, url)                                
                                 response = requests.get(url)                                 
                                 f.write(response.content)
                                 prg.stop()
                    except:
                          tkinter.messagebox.askretrycancel("Error","URL is not correct /Network error")
                    
               




#=====================================================================#
          MainFrame=Frame(self.root,width=500,height=300,relief="sunken",bd=3)
          MainFrame.place(x=0,y=0)

          self.original1 = Image.open ("C:\\Users\\SHREYAS\\Desktop\\shreyas python\\HamsterBoy\\xhamster.png")
          resized1 = self.original1.resize((495, 300),Image.ANTIALIAS)
          self.image1 = ImageTk.PhotoImage(resized1)
          bglab1=Label(MainFrame,image=self.image1,bd=1).place(x=0,y=0)

          Lab_Url=Label(MainFrame,text="Paste Xhamsters Url :",font=("times new roman",11,"bold"),bg="black",fg="cyan")
          Lab_Url.place(x=170,y=30)

          Ent_Url=Entry(MainFrame,width=55,font=("times new roman",11,"bold"),bg="#dbfbf8",bd=3,textvariable=xurls)
          Ent_Url.place(x=20,y=60)



          Down_but=Button(MainFrame,text="Download Photos",width=15,font=('times new roman',12,'bold'),relief=RIDGE,bd=3,cursor="hand2",command=download_xhamster)
          Down_but.place(x=30,y=200)
          Down_but.bind("<Enter>",on_enter1)
          Down_but.bind("<Leave>",on_leave1)


          Clear_but=Button(MainFrame,text="Clear",command=clear,width=15,font=('times new roman',12,'bold'),relief=RIDGE,bd=3,cursor="hand2")
          Clear_but.place(x=310,y=200)
          Clear_but.bind("<Enter>",on_enter2)
          Clear_but.bind("<Leave>",on_leave2)


          prg=Progressbar(MainFrame,length=490,orient=HORIZONTAL,mode='indeterminate')
          prg.place(x=4,y=273)




          

          
          

          
          






#=====================================================================#

if __name__ == "__main__":
    root=Tk()
    app=xhamster(root)
    root.mainloop()

