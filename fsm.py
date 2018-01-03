from transitions.extensions import GraphMachine
from urllib.request import urlopen
from bs4 import BeautifulSoup

        
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs            
        )                
        
    def is_going_to_state16(self, update):
        text = update.message.text        
        if text.lower() == 'about':
            return text.lower() == 'about'
                            
                    
    def on_enter_state16(self, update):
        update.message.reply_text("Info(introduction)：")
        html = urlopen("https://en.wikipedia.org/wiki/Casablanca_(film)") 
        background= BeautifulSoup(html.read(), "lxml")
        #print(background)
        ray=background.find('p')
        update.message.reply_text(ray.text)
       	#update.message.reply_text("KKK")       
       	#update.message.reply_text("NNN")         
        self.go_back(update)

    def on_exit_state16(self, update):
        print('Leaving state16')            
                
    def is_going_to_user(self, update):
        text = update.message.text
        return text.lower() == 'hello'
                
    def on_enter_user(self, update):
         
        update.message.reply_text("Say something and I will reply you with some facts and quotes from the film Casablanca")            
        #self.go_back(update)                    

    def is_going_to_state1(self, update):
        text = update.message.text        
        if text.lower() == 'quotes':
            return text.lower() == 'quotes'           

    def is_going_to_state2(self, update):
        text = update.message.text
        if text.lower() == 'actors':
            return text.lower() == 'actors'
      
    def is_going_to_state3(self, update):
        text = update.message.text
        if text.lower() == 'video':        
            return text.lower() == 'video'        
                                   
    #QUOTES going state4~state6 state7 to back	
    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == 'rick'#Rick's quote
        
    def is_going_to_state5(self, update):
        text = update.message.text
        return text.lower() == 'ilsa'#Ilsa's quotes
         
    def is_going_to_state6(self, update):
        text = update.message.text
        return text.lower() == 'conversation'#Ilsa and Sam's conversation
        
    def is_going_to_state7(self, update):
        text = update.message.text
        if text.lower() == 'see you':        
            return text.lower() == 'see you'        
    
    #ACTORS going state 8-10
    def is_going_to_state8(self, update):
        text = update.message.text
        if text.lower() == 'rick':
            return text.lower() == 'rick'
        elif text.lower() == 'rick blaine':
            return  text.lower() == 'rick blaine'

    def is_going_to_state9(self, update):
        text = update.message.text
        if text.lower() == 'ilsa':
            return text.lower() == 'ilsa'
        elif text.lower() == 'ingrid bergman': 
            return text.lower() == 'ingrid bergman'
            
    def is_going_to_state10(self, update):
        text = update.message.text
        if text.lower() == 'sam':
            return text.lower() == 'sam'
        elif text.lower() == 'pianist':
            return  text.lower() == 'pianist'        

    def is_going_to_state11(self, update):
        text = update.message.text
        if text.lower() == 'see you':        
            return text.lower() == 'see you'        
        #elif text.lower() == 'no':
        #    return text.lower() == 'no' 
    #影音部份 going state12-14 back 15
    def is_going_to_state12(self, update):
        text = update.message.text
        if text.lower() == 'background music':
            return text.lower() == 'background music'
       
    def is_going_to_state13(self, update):
        text = update.message.text
        if text.lower() == 'clip':
            return text.lower() == 'clip'

    def is_going_to_state14(self, update):
        text = update.message.text
        if text.lower() == '配樂':
            return text.lower() == '配樂'
       

    def is_going_to_state15(self, update):
        text = update.message.text
        if text.lower() == 'nothing':        
            return text.lower() == 'nothing'                             
                
    def on_enter_state1(self, update):
      
       	update.message.reply_text("Give me the character's name and I will give you the qoutes.")        
        #self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_text("Wanna see the pictures of the actors?")
        #self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')

    def on_enter_state3(self, update):
        update.message.reply_text("Wanna see something vintage and sublime?")        
        #self.go_back(update)
    
    def on_exit_state3(self, update):
        print('Leaving state3')
    
    #族語部份 on state4-6 back 7            
    def on_enter_state4(self, update):
        update.message.reply_text("Rick: Of all the gin joints in all the towns in all the world, she walks into mine.")
        update.message.reply_text("Want to see some more classic qoutes ?")
        #self.go_back(update)

    def on_exit_state4(self, update):
        print('Leaving state4')   

    def on_enter_state5(self, update):
        update.message.reply_text("Ilsa: Play it once, Sam, for old times' sake. Play  As Time Goes By.")
        update.message.reply_text("Want to take a look at some more classic qoutes ?")
        #self.go_back(update)

    def on_exit_state5(self, update):
        print('Leaving state5')              

    def on_enter_state6(self, update):
        update.message.reply_text("Ilsa: Play it, Sam, Play As Time Goes By. Sam: (lying)Oh, I can't remember it, Miss Ilsa. I'm a little rusty on it")
        update.message.reply_text("That's all my favourite lines from the film Casablanca")        
        self.go_back(update)

    def on_exit_state6(self, update):
        print('Leaving state6')
          
    def on_enter_state7(self, update):
        update.message.reply_text("Hope you enjoy my introduction to this movie")
        self.go_back(update)

    def on_exit_state7(self, update):
        print('Leaving state7')
    #演員部份 on state 8-10
    def on_enter_state8(self, update):
        update.message.reply_text("Rick")               
        photo_file = open('img/casa1.jpg', 'rb')
        update.message.reply_photo(photo_file)
        photo_file.close()
        update.message.reply_text("Wanna see some other characters?")
        #self.go_back(update)

    def on_exit_state8(self, update):
        print('Leaving state8')   

    def on_enter_state9(self, update):
        update.message.reply_text("Ilsa")
        photo_file = open('img/casa2.jpg', 'rb')
        update.message.reply_photo(photo_file)
        photo_file.close()
        update.message.reply_text("Maybe you'd like to see the last one?")
        #self.go_back(update)

    def on_exit_state9(self, update):
        print('Leaving state9')              

    def on_enter_state10(self, update):
        update.message.reply_text("Sam") 
        photo_file = open('img/casa3.jpg', 'rb')
        update.message.reply_photo(photo_file)
        photo_file.close()
        update.message.reply_text("That's all I've got thx")                
        self.go_back(update)
        

    def on_exit_state10(self, update):
        print('Leaving state10') 

    def on_enter_state11(self, update):
        update.message.reply_text("Hope you'd enjoy all the infos above.")
        self.go_back(update)

    def on_exit_state11(self, update):
        print('Leaving state11') 

    #影音部份 going state12-14 back 15 
    def on_enter_state12(self, update):
        update.message.reply_text("music")               
        audio_file = open('music/musicAsTime.mp3', 'rb')
        update.message.reply_audio(audio_file)
        audio_file.close()
        update.message.reply_text("Need some video?")
        #self.go_back(update)

    def on_exit_state12(self, update):
        print('Leaving state12')   

    def on_enter_state13(self, update):
        update.message.reply_text("clip")
        video_file=open('video/CasaClip.mp4', 'rb')
        update.message.reply_video(video_file)
        video_file.close()
        update.message.reply_text("Need more?")
        #self.go_back(update)

    def on_exit_state13(self, update):
        print('Leaving state13')  

    def on_enter_state14(self, update):
        update.message.reply_text("music")               
        audio_file = open('music/CasaSuite.mp3', 'rb')
        update.message.reply_audio(audio_file)
        audio_file.close()
        update.message.reply_text("Thx see u.")                
        self.go_back(update)
        

    def on_exit_state14(self, update):
        print('Leaving state14') 

    def on_enter_state15(self, update):
        update.message.reply_text("Brace yourselves and enjoy this beautiful movie")
        self.go_back(update)

    def on_exit_state15(self, update):
        print('Leaving state15')                                              
