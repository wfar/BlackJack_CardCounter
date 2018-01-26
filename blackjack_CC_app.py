
import time
import webbrowser
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.image import Image


class HomePage(FloatLayout):
    '''  Creats the Home page for the app using a FloatLayoot

        main_logo: adds an image to the main page
        start_button: takes you to counting methods page
        instructions_button: takes you to the Hoe To page

        '''
    
    def __init__(self, **kwargs):
        super(HomePage, self).__init__(**kwargs)

        self.main_logo = Image(source='3850.jpg', size_hint=(1, 1) )
        self.add_widget(self.main_logo)

        self.add_widget(Label(text='[color=000000]BlackJack Card Counter[/color]', font_size = 50, size_hint=(.5, .25), pos_hint={'x':.25, 'y':.8}, markup=True))
        self.start_button = Button(text='Start', size_hint=(.5, .05), pos_hint={'x':.25, 'y':.5} )
        self.start_button.bind(on_release = self.go_to_countingmethodpage )
        self.add_widget(self.start_button)
        self.instructions_button = Button(text='Instructions', size_hint=(.5, .05), pos_hint={'x':.25, 'y':.4} )
        self.instructions_button.bind(on_release = self.go_to_howtopage )
        self.add_widget( self.instructions_button  )

    def go_to_countingmethodpage(self, *args):
        ''' binds the start button to the counting method page once button is released'''
        #print('Start button pressed')
        sm.current = 'Counting Methods'

    def go_to_howtopage(self, *args):
        ''' binds instructions button to the how to page once button is released'''
        #print('Instructions button pressed')
        sm.current = 'How To'
        
     
class HowToPage(GridLayout):
    ''' How to page is a class using gridlayout that contains two cols:
        one for Instructions section and the other for resource links'''
    
    def __init__(self, **kwargs):
        super(HowToPage, self).__init__(**kwargs)
        self.cols = 2
      
        self.add_widget( InstructionsSection()) 
        self.add_widget(ResourcesSection())
        
class InstructionsSection(FloatLayout):
    ''' Contains instructions on how to use the applicaition and is added to the HowToPage class

        guide: contains the string of instructions for user to read
        back_button: back widget takes back to the homepage

        '''
    def __init__(self, **kwargs):
        super(InstructionsSection, self).__init__(**kwargs)

        self.guide = '''
                    Using the card couter is simple.
                    First read and understand how
                    counting cards works and take
                    a look at the different methods
                    of counting, then select one. Once
                    selected, enter the amount of decks
                    in the dealers shoe. Then as the
                    game goes on, enter in every card
                    that appears on the table. The app
                    will count the cards up for you,
                    calculaating both the running count
                    and true count. The app will tell
                    you when you have the advantage over
                    the house so you can increase bets.
                    '''

        self.add_widget(Label(text=self.guide, font_size = 20, text_size=(550, None), size_hint=(.1, .05), pos_hint={'x':.5, 'y':.48}))
        self.back_button = Button(text='Back', size_hint=(.15, .119), pos_hint={'x':0, 'y':.88} )
        self.back_button.bind(on_release = self.go_back )
        self.add_widget(self.back_button)

    def go_back(self, *args):
        '''binds the back button to the home page once button is released'''
        print('Back button on the Instructions page pressed')
        sm.current = 'Home'
                              

class ResourcesSection(GridLayout):
    ''' Contains the resources links and buttons that allow users to learn more about counting.

        rows: creted to add widgts such as the resource label and the links.
        wiki_button: opens browser and leads you to wiki artile on card counting
        bja_button: opens browser and takes you to bja article on counting cards.
        bja_button_2: opens browser and takes you to an article on different counting methods
        bjage_button: opens browser and takes you to an article on card counting systems.

    '''
    def __init__(self, **kwargs):
        super(ResourcesSection, self).__init__(**kwargs)
        self.rows = 5
        self.add_widget(Label(text = '[color=3333ff]Resources[/color]', font_size= 30, halign= 'right', valign = 'middle', markup = True))

        self.wiki_button = Button(text = 'Wikipedia: "Card counting"', font_size= 12, halign= 'left', valign = 'center')
        self.wiki_button.bind(on_release = lambda x: self.open_webpage('https://en.wikipedia.org/wiki/Card_counting'))
        self.add_widget(self.wiki_button)

        self.bja_button = Button(text = 'BlackJack Apprenticeship: "How to count cards"', font_size= 12, halign= 'left', valign = 'center')
        self.bja_button.bind(on_release = lambda x: self.open_webpage('https://www.blackjackapprenticeship.com/resources/how-to-count-cards/'))
        self.add_widget(self.bja_button)

        self.bja_button_2 = Button(text = ' BlackJack Apprenticeship: "Card counting systems"', font_size= 12, halign= 'left', valign = 'center')
        self.bja_button_2.bind(on_release = lambda x: self.open_webpage('https://www.blackjackapprenticeship.com/resources/card-counting-systems/'))
        self.add_widget(self.bja_button_2)

        self.bjage_button = Button(text = 'BlackJack Age: "BlackJack counting systems"', font_size= 12, halign= 'left', valign = 'center')
        self.bjage_button.bind(on_release = lambda x: self.open_webpage('http://www.blackjackage.com/card-counting-systems.php'))
        self.add_widget(self.bjage_button)

    def open_webpage(self, url, *args):
        ''' binds to the resource buttons when buttons released, opens browser and takes you to the article.'''
        webbrowser.open(url)
           

class CountingMethodPage(FloatLayout):
    '''This class contains the CountingmethodPage widgets and functions. User selects the shoe size and counting method
        by entering a number into the input box and pressing method button.

        content_1: contains text telling user to enter shoe size
        shoe_input: textinput widget that allows user input
        back_button: allows user to go back to the previos page, whichis the Home page
        hi_lo_button: Selcts the Hi Lo counting method and goes to All Methods page
        ko_button: Selects KO counting method and goes to ALl methods page
        ho_1_button: slects Hi-Opt I counting method
        ho_2-button: selects Hi-Opt II counting method
        halves_buttion: selects Halves counting method and goes to all methods page
        omege_button: selects Omega II counting method and goes to all methods page
        red_sevens_button: selects Red Sevens counting method and goes to all methods page
        sen_count_button: selects Zen count method and goes to all methods
    '''
    
    def __init__(self, **kwargs):
        super(CountingMethodPage, self).__init__(**kwargs)

        

        self.content_1 = Label(text = 'Enter the number of decks in shoe (usually 6 or 8 decks)', size_hint=(.1, .05), pos_hint={'x':.45, 'y':.80}, font_size= 25 )
        self.shoe_input = TextInput(multiline=False, size_hint=(.08, .08), pos_hint={'x':.45, 'y':.65}, font_size = 25 )
        self.add_widget(self.content_1)
        self.add_widget( self.shoe_input)
        self.add_widget(Label(text = 'Select counting method', size_hint=(.1, .05), pos_hint={'x':.45, 'y':.55}, font_size= 25 ))
        self.back_button = Button(text='Back', size_hint=(.15, .119), pos_hint={'x':0, 'y':.88} )
        self.back_button.bind(on_release = self.go_back )
        self.add_widget( self.back_button)

        self.hi_lo_button = Button(text='Hi-Lo', size_hint=(.12, .08), pos_hint={'x':.35, 'y':.40})
        self.hi_lo_button.bind(on_release = self.go_to_allmethodspage )
        self.add_widget(self.hi_lo_button)

        self.ko_button = Button(text='KO', size_hint=(.12, .08), pos_hint={'x':.55, 'y':.40})
        self.ko_button.bind(on_release = self.go_to_allmethodspage )
        self.add_widget(self.ko_button)

        self.ho_1_button = Button(text='Hi-Opt I', size_hint=(.12, .08), pos_hint={'x':.35, 'y':.30})
        self.ho_1_button.bind(on_release = self.go_to_allmethodspage )
        self.add_widget(self.ho_1_button)

        self.ho_2_button = Button(text='Hi-Opt II', size_hint=(.12, .08), pos_hint={'x':.55, 'y':.30})
        self.ho_2_button.bind(on_release = self.go_to_allmethodspage)
        self.add_widget(self.ho_2_button)

        self.halves_button = Button(text='Halves', size_hint=(.12, .08), pos_hint={'x':.35, 'y':.20})
        self.halves_button.bind(on_release = self.go_to_allmethodspage)
        self.add_widget(self.halves_button)

        self.omega_button = Button(text='Omega II', size_hint=(.12, .08), pos_hint={'x':.55, 'y':.20})
        self.omega_button.bind(on_release = self.go_to_allmethodspage)
        self.add_widget(self.omega_button)

        self.red_seven_button = Button(text='Red 7', size_hint=(.12, .08), pos_hint={'x':.35, 'y':.10})
        self.red_seven_button.bind(on_release = self.go_to_allmethodspage)
        self.add_widget(self.red_seven_button)

        self.zen_count_button = Button(text='Zen Count', size_hint=(.12, .08), pos_hint={'x':.55, 'y':.10})
        self.zen_count_button.bind(on_release = self.go_to_allmethodspage)
        self.add_widget(self.zen_count_button)


        
    def go_to_allmethodspage(self, instance, *args):
        '''Checks to see if a valid number entered into shoe_input, sets the size of shoe,
            sets game to counting method button selected, and goes to the all methods page'''
        
        global shoe     # contains the number of decks in shoe, used in multiple locations
        shoe = self.shoe_input.text
        print(shoe)
        if shoe != '':            
            try:
                if int(shoe) > 0:
                    shoe = int(self.shoe_input.text)
                    print(type(shoe))
                    sm.current = 'Method'
                    global game     # cointains the type of counting method to determine count, used in multiple locations
                    game = instance.text
                    #print(game)
                    #print('a method button was pressed')
                else:
                    print('ENTER A NUMBER')
                    self.error_popup()                    
            except:
                print('ENTER A NUMBER')
                self.error_popup()
        else:
            print('ENTER A NUMBER')
            self.error_popup()

    def go_back(self, *args):
        ''' bound to back button, returns user to home page'''
        
        print('Back button on the methods page pressed')
        sm.current = 'Home'

    def error_popup(self):
        '''creates a popup widget prompting user to enter a valid integer to countine to all methods page'''
        
        content = GridLayout()
        content.rows = 2
        popup_text = Label(text='Please enter a  valid number to continue')
        close_button = Button(text='Close')
        content.add_widget(popup_text)
        content.add_widget(close_button)
        popup = Popup(title='Shoe size', content=content, size_hint=(.4, .4))
        close_button.bind(on_release = popup.dismiss)
        popup.open()
                
    

class AllMethodsPage(FloatLayout):
    '''
        







    '''
    
    def __init__(self, **kwargs):
        super(AllMethodsPage, self).__init__(**kwargs)

        self.button_log = []
        self.start_trigger = False
        self.red_trigger = False
        self.game_list = {
            'Hi-Lo': {'A': -1, 'K': -1, 'Q': -1, 'J': -1, '10': -1, '9': 0, '8': 0, '7': 0, '6': 1, '5': 1, '4': 1, '3': 1, '2': 1},
            'Hi-Opt I': {'A': 0, 'K': -1, 'Q': -1, 'J': -1, '10': -1, '9': 0, '8': 0, '7': 0, '6': 1, '5': 1, '4': 1, '3': 1, '2': 0},
            'Hi-Opt II': {'A': 0, 'K': -2, 'Q': -2, 'J': -2, '10': -2, '9': 0, '8': 0, '7': 1, '6': 1, '5': 2, '4': 2, '3': 1, '2': 1},
            'KO': {'A': -1, 'K': -1, 'Q': -1, 'J': -1, '10': -1, '9': 0, '8': 0, '7': 1, '6': 1, '5': 1, '4': 1, '3': 1, '2': 1},
            'Omega II': {'A': 0, 'K': -2, 'Q': -2, 'J': -2, '10': -2, '9': -1, '8': 0, '7': 1, '6': 2, '5': 2, '4': 2, '3': 1, '2': 1},
            'Red 7': {'A': -1, 'K': -1, 'Q': -1, 'J': -1, '10': -1, '9': 0, '8': 0, '7': 0, 'R7': 1, '6': 1, '5': 1, '4': 1, '3': 1, '2': 1},
            'Halves': {'A': -1, 'K': -1, 'Q': -1, 'J': -1, '10': -1, '9': -0.5, '8': 0, '7': 0.5, '6': 1, '5': 1.5, '4': 1, '3': 1, '2': 0.5},
            'Zen Count': {'A': -1, 'K': -2, 'Q': -2, 'J': -2, '10': -2, '9': 0, '8': 0, '7': 1, '6': 2, '5': 2, '4': 2, '3': 1, '2': 1}
            }        

        self.back_button = Button(text='Back', size_hint=(.15, .119), pos_hint={'x':0, 'y':.88} )
        self.back_button.bind(on_release = self.go_back )
        self.add_widget( self.back_button)

        self.ace_button = Button(text='A', size_hint=(.09, .09), pos_hint={'x':.1, 'y':.60} )
        self.ace_button.bind(on_release = self.update_count )
        self.add_widget(self.ace_button)
        
        self.king_button = Button(text='K', size_hint=(.09, .09), pos_hint={'x':.2, 'y':.60})
        self.king_button.bind(on_release = self.update_count )
        self.add_widget(self.king_button)
        
        self.queen_button = Button(text='Q', size_hint=(.09, .09), pos_hint={'x':.3, 'y':.60})
        self.queen_button.bind(on_release = self.update_count )
        self.add_widget(self.queen_button)
        
        self.jack_button = Button(text='J', size_hint=(.09, .09), pos_hint={'x':.4, 'y':.60})
        self.jack_button.bind(on_release = self.update_count )
        self.add_widget(self.jack_button)
        
        self.ten_button = Button(text='10', size_hint=(.09, .09), pos_hint={'x':.15, 'y':.50})
        self.ten_button.bind(on_release = self.update_count )
        self.add_widget(self.ten_button)
        
        self.nine_button = Button(text='9', size_hint=(.09, .09), pos_hint={'x':.25, 'y':.50})
        self.nine_button.bind(on_release = self.update_count )
        self.add_widget(self.nine_button)
        
        self.eight_button = Button(text='8', size_hint=(.09, .09), pos_hint={'x':.35, 'y':.50})
        self.eight_button.bind(on_release = self.update_count )
        self.add_widget(self.eight_button)

        self.seven_button = Button(text='7', size_hint=(.09, .09), pos_hint={'x':.15, 'y':.40})
        self.seven_button.bind(on_release = self.update_count )
        self.add_widget(self.seven_button)
        
        self.six_button = Button(text='6', size_hint=(.09, .09), pos_hint={'x':.25, 'y':.40})
        self.six_button.bind(on_release = self.update_count)
        self.add_widget(self.six_button)
        
        self.five_button = Button(text='5', size_hint=(.09, .09), pos_hint={'x':.35, 'y':.40})
        self.five_button.bind(on_release = self.update_count )
        self.add_widget(self.five_button)
        
        self.four_button = Button(text='4', size_hint=(.09, .09), pos_hint={'x':.15, 'y':.30})
        self.four_button.bind(on_release = self.update_count )
        self.add_widget(self.four_button)
        
        self.three_button = Button(text='3', size_hint=(.09, .09), pos_hint={'x':.25, 'y':.30})
        self.three_button.bind(on_release = self.update_count )
        self.add_widget(self.three_button)
        
        self.two_button = Button(text='2', size_hint=(.09, .09), pos_hint={'x':.35, 'y':.30})
        self.two_button.bind(on_release = self.update_count )
        self.add_widget(self.two_button)

        self.undo_button = Button(text='UNDO', size_hint=(.13, .10), pos_hint={'x':.15, 'y':.17})
        self.undo_button.bind(on_release = self.undo )
        self.add_widget(self.undo_button)

        self.restart_button = Button(text='RESTART', size_hint=(.13, .10), pos_hint={'x':.3109, 'y':.17})
        self.restart_button.bind(on_release = self.restart )
        self.add_widget(self.restart_button)        

        self.start_button = Button(text='START', size_hint=(.13, .10), pos_hint={'x':.7, 'y':.7})
        self.start_button.bind(on_release = self.start )
        self.add_widget(self.start_button)

    
    def update_count(self, instance, *args):
        print(instance.text)
        
        if self.start_trigger:
            
            if instance.text == 'A' and self.ace_rem >= 1:
                self.ace_rem -= 1
                print(self.ace_rem)
                self.running_count = self.running_count + self.game_list[game]['A']
                self.true_count = round( self.running_count / self.decks_rem, 2)
                self.remove_widget(self.count_info)
                self.add_count(instance)
                
            elif instance.text == 'K' and self.king_rem >= 1:
                self.king_rem -= 1
                print(self.king_rem)
                self.running_count = self.running_count + self.game_list[game]['K']
                self.true_count = round( self.running_count / self.decks_rem, 2)
                self.remove_widget(self.count_info)
                self.add_count(instance)
                
            elif instance.text == 'Q' and self.queen_rem >= 1:
                self.queen_rem -= 1
                print(self.queen_rem)
                self.running_count = self.running_count + self.game_list[game]['Q']
                self.true_count = round( self.running_count / self.decks_rem, 2)
                self.remove_widget(self.count_info)
                self.add_count(instance)
                
            elif instance.text == 'J' and self.jack_rem >= 1:
                self.jack_rem -= 1
                print(self.jack_rem)
                self.running_count = self.running_count + self.game_list[game]['J']
                self.true_count = round( self.running_count / self.decks_rem, 2)
                self.remove_widget(self.count_info)
                self.add_count(instance)
                
            elif instance.text == '10' and self.ten_rem >= 1:
                self.ten_rem -= 1
                print(self.ten_rem)
                self.running_count = self.running_count + self.game_list[game]['10']
                self.true_count = round( self.running_count / self.decks_rem, 2)
                self.remove_widget(self.count_info)
                self.add_count(instance)
                
            elif instance.text == '9' and self.nine_rem >= 1:
                self.nine_rem -= 1
                print(self.nine_rem)
                self.running_count = self.running_count + self.game_list[game]['9']
                self.true_count = round( self.running_count / self.decks_rem, 2)
                self.remove_widget(self.count_info)
                self.add_count(instance)
        
            elif instance.text == '8' and self.eight_rem >= 1:
                self.eight_rem -= 1
                print(self.eight_rem)
                self.running_count = self.running_count + self.game_list[game]['8']
                self.true_count = round( self.running_count / self.decks_rem, 2)
                self.remove_widget(self.count_info)
                self.add_count(instance)
                
            elif instance.text == '7' and self.seven_rem >= 1:
                self.seven_rem -= 1
                print(self.seven_rem)
                self.running_count = self.running_count + self.game_list[game]['7']
                self.true_count = round( self.running_count / self.decks_rem, 2)
                self.remove_widget(self.count_info)
                self.add_count(instance)

            elif instance.text == 'Red 7' and self.seven_rem >= 1:
                self.seven_rem -= 1
                print(self.seven_rem)
                self.running_count = self.running_count + self.game_list[game]['R7']
                self.true_count = round(self.running_count / self.decks_rem, 2)
                self.remove_widget(self.count_info)
                self.add_count(instance)
                
            elif instance.text == '6' and self.six_rem >= 1:
                self.six_rem -= 1
                print(self.six_rem)
                self.running_count = self.running_count + self.game_list[game]['6']
                self.true_count = round( self.running_count / self.decks_rem, 2)
                self.remove_widget(self.count_info)
                self.add_count(instance)
                
            elif instance.text == '5' and self.five_rem >= 1:
                self.five_rem -= 1
                print(self.five_rem)
                self.running_count = self.running_count + self.game_list[game]['5']
                self.true_count = round( self.running_count / self.decks_rem, 2)
                self.remove_widget(self.count_info)
                self.add_count(instance)
                
            elif instance.text == '4' and self.four_rem >= 1:
                self.four_rem -= 1
                print(self.four_rem)
                self.running_count = self.running_count + self.game_list[game]['4']
                self.true_count = round( self.running_count / self.decks_rem, 2 )
                self.remove_widget(self.count_info)
                self.add_count(instance)
                
            elif instance.text == '3' and self.three_rem >= 1:
                self.three_rem -= 1
                print(self.three_rem)
                self.running_count = self.running_count + self.game_list[game]['3']
                self.true_count = round(self.running_count / self.decks_rem, 2)
                self.remove_widget(self.count_info)
                self.add_count(instance)
                
            elif instance.text == '2' and self.two_rem >= 1:
                self.two_rem -= 1
                print(self.two_rem)
                self.running_count = self.running_count + self.game_list[game]['2']
                self.true_count = round(self.running_count / self.decks_rem, 2)
                self.remove_widget(self.count_info)
                self.add_count(instance)
            
            
        else:
            print('Start button not pressed')
    '''
    def reset_deck(self):
        self.ace_rem = 4 * int(shoe)
        self.king_rem = 4 * int(shoe)
        self.queen_rem = 4 * int(shoe)
        self.jack_rem = 4 * int(shoe)
        self.ten_rem = 4 * int(shoe)
        self.nine_rem = 4 * int(shoe)
        self.eight_rem = 4 * int(shoe)
        self.seven_rem = 4 * int(shoe)
        self.six_rem = 4 * int(shoe)
        self.five_rem = 4 * int(shoe)
        self.four_rem = 4 * int(shoe)
        self.three_rem = 4 * int(shoe)
        self.two_rem = 4 * int(shoe)

        self.button_log.clear()

    '''
    
    def add_count(self, instance):

        if instance.text != 'UNDO' and instance.text != 'START' and instance.text != 'RESTART':
            self.button_log.append(instance.text)
        
        if instance.text != 'START' and instance.text != 'UNDO' and instance.text != 'RESTART':
            self.total_cards -= 1

        if len(self.button_log) > 0 and len(self.button_log) % 52 == 0:
            if self.decks_rem > 1:
                self.decks_rem -= 1
                #self.reset_deck()
            else:
                self.decks_rem -= 1
  
            
        formatted_string = '''


                            True Count: {:5}        Running Count: {:5}
                            
                            Shoe: {:5}                  Total Cards: {:5}

                            

                                        Deck Number: {:5}

                                        CARDS REMAINING
                                        
                                        A's: {:2}                 K's: {:2}
                            
                                        Q's: {:2}                 J's: {:2}
                            
                                        10's: {:2}                9's: {:2}
                            
                                        8's: {:2}                 7's: {:2}
                            
                                        6's: {:2}                 5's: {:2}
                            
                                        4's: {:2}                 3's: {:2}
                            
                                                    2's: {:2}'''.format(self.true_count, self.running_count, shoe, self.total_cards, self.decks_rem, self.ace_rem, self.king_rem, self.queen_rem, self.jack_rem,
                                                        self.ten_rem, self.nine_rem, self.eight_rem, self.seven_rem, self.six_rem, self.five_rem, self.four_rem,
                                                        self.three_rem, self.two_rem )

        self.count_info = Label(text=formatted_string, size_hint=(.09, .09), pos_hint={'x':.67, 'y':.60})
        self.add_widget(self.count_info)
        
    def start(self, instance):
        print(shoe)
        self.start_trigger = True
        self.decks_rem = int(shoe)
        self.running_count = 0 
        self.true_count = 0
        self.total_cards = 52 * int(shoe)
        self.ace_rem = 4 * int(shoe)
        self.king_rem = 4 * int(shoe)
        self.queen_rem = 4 * int(shoe)
        self.jack_rem = 4 * int(shoe)
        self.ten_rem = 4 * int(shoe)
        self.nine_rem = 4 * int(shoe)
        self.eight_rem = 4 * int(shoe)
        self.seven_rem = 4 * int(shoe)
        self.six_rem = 4 * int(shoe)
        self.five_rem = 4 * int(shoe)
        self.four_rem = 4 * int(shoe)
        self.three_rem = 4 * int(shoe)
        self.two_rem = 4 * int(shoe)

        self.decks_rem = int(shoe)

        if game == 'Red 7':
            self.red_trigger = True
            self.red_seven_button = Button(text='Red 7', size_hint=(.13, .10), pos_hint={'x':.3109, 'y':.05}, background_color = (10,0,0,1))
            self.red_seven_button.bind(on_release = self.update_count )
            self.add_widget(self.red_seven_button)

        self.remove_widget(self.start_button)
        self.add_count(instance)
        

    def undo(self, instance, *args):

        if len(self.button_log) > 0 and self.start_trigger and self.decks_rem > 0:
            
            self.remove_widget(self.count_info)
            
            if self.button_log[-1] == 'A':
                if self.ace_rem < 4 * int(shoe):
                    self.ace_rem += 1
                    self.total_cards += 1
                    self.running_count = self.running_count - self.game_list[game]['A']
                    self.true_count = round( self.running_count / self.decks_rem, 2)
                    del self.button_log[-1]
                    self.add_count(instance)
                else:
                    print('Skip undo')
            elif self.button_log[-1] == 'K':
                if self.king_rem < 4 * int(shoe):
                    self.king_rem += 1
                    self.total_cards += 1
                    self.running_count = self.running_count - self.game_list[game]['K']
                    self.true_count = round( self.running_count / self.decks_rem, 2)
                    del self.button_log[-1]
                    self.add_count(instance)
                else:
                    print('Skip undo')                
            elif self.button_log[-1] == 'Q':
                if self.queen_rem < 4 * int(shoe):
                    self.queen_rem += 1
                    self.total_cards += 1
                    self.running_count = self.running_count - self.game_list[game]['Q']
                    self.true_count = round( self.running_count / self.decks_rem, 2)
                    del self.button_log[-1]
                    self.add_count(instance)
                else:
                    print('Skip undo')
            elif self.button_log[-1] == 'J':
                if self.jack_rem < 4 * int(shoe):
                    self.jack_rem += 1
                    self.total_cards += 1
                    self.running_count = self.running_count - self.game_list[game]['J']
                    self.true_count = round( self.running_count / self.decks_rem, 2)
                    del self.button_log[-1]
                    self.add_count(instance)
                else:
                    print('Skip undo')
            elif self.button_log[-1] == '10':
                if self.ten_rem < 4 * int(shoe):
                    self.ten_rem += 1
                    self.total_cards += 1
                    self.running_count = self.running_count - self.game_list[game]['10']
                    self.true_count = round( self.running_count / self.decks_rem, 2)
                    del self.button_log[-1]
                    self.add_count(instance)
                else:
                    print('Skip undo')
            elif self.button_log[-1] == '9':
                if self.nine_rem < 4 * int(shoe):
                    self.nine_rem += 1
                    self.total_cards += 1
                    self.running_count = self.running_count - self.game_list[game]['9']
                    self.true_count = round( self.running_count / self.decks_rem, 2)
                    del self.button_log[-1]
                    self.add_count(instance)
                else:
                    print('Skip undo')
            elif self.button_log[-1] == '8':
                if self.eight_rem < 4 * int(shoe):
                    self.eight_rem += 1
                    self.total_cards += 1
                    self.running_count = self.running_count - self.game_list[game]['8']
                    self.true_count = round( self.running_count / self.decks_rem, 2)
                    del self.button_log[-1]
                    self.add_count(instance)
                else:
                    print('Skip undo')
            elif self.button_log[-1] == '7':
                if self.seven_rem < 4 * int(shoe):
                    self.seven_rem += 1
                    self.total_cards += 1
                    self.running_count = self.running_count - self.game_list[game]['7']
                    self.true_count = round( self.running_count / self.decks_rem, 2)
                    del self.button_log[-1]
                    self.add_count(instance)
                else:
                    print('Skip undo')
            elif self.button_log[-1] == 'Red 7':
                if self.seven_rem < 4 * int(shoe):
                    self.seven_rem += 1
                    self.total_cards += 1
                    self.running_count = self.running_count - self.game_list[game]['R7']
                    self.true_count = round( self.running_count / self.decks_rem, 2)
                    del self.button_log[-1]
                    self.add_count(instance)
                else:
                    print('Skip undo')
            elif self.button_log[-1] == '6':
                if self.six_rem < 4 * int(shoe):
                    self.six_rem += 1
                    self.total_cards += 1
                    self.running_count = self.running_count - self.game_list[game]['6']
                    self.true_count = round( self.running_count / self.decks_rem, 2)
                    del self.button_log[-1]
                    self.add_count(instance)
                else:
                    print('Skip undo')
            elif self.button_log[-1] == '5':
                if self.five_rem < 4 * int(shoe):
                    self.five_rem += 1
                    self.total_cards += 1
                    self.running_count = self.running_count - self.game_list[game]['5']
                    self.true_count = round( self.running_count / self.decks_rem, 2)
                    del self.button_log[-1]
                    self.add_count(instance)
                else:
                    print('Skip undo')
            elif self.button_log[-1] == '4':
                if self.four_rem < 4 * int(shoe):
                    self.four_rem += 1
                    self.total_cards += 1
                    self.running_count = self.running_count - self.game_list[game]['4']
                    self.true_count = round( self.running_count / self.decks_rem, 2)
                    del self.button_log[-1]
                    self.add_count(instance)
                else:
                    print('Skip undo')
            elif self.button_log[-1] == '3':
                if self.three_rem < 4 * int(shoe):
                    self.three_rem += 1
                    self.total_cards += 1
                    self.running_count = self.running_count - self.game_list[game]['3']
                    self.true_count = round( self.running_count / self.decks_rem, 2)
                    del self.button_log[-1]
                    self.add_count(instance)
                else:
                    print('Skip undo')
            elif self.button_log[-1] == '2':
                if self.two_rem < 4 * int(shoe):
                    self.two_rem += 1
                    self.total_cards += 1
                    self.running_count = self.running_count - self.game_list[game]['2']
                    self.true_count = round( self.running_count / self.decks_rem, 2)
                    del self.button_log[-1]
                    self.add_count(instance)
                else:
                    print('Skip undo')
        else:
            print('Button log empty. Do nothing')


    def restart(self, instance, *args):
        if self.start_trigger:
            self.running_count = 0 
            self.true_count = 0
            self.total_cards = 52 * int(shoe)
            self.ace_rem = 4 * int(shoe)
            self.king_rem = 4 * int(shoe)
            self.queen_rem = 4 * int(shoe)
            self.jack_rem = 4 * int(shoe)
            self.ten_rem = 4 * int(shoe)
            self.nine_rem = 4 * int(shoe)
            self.eight_rem = 4 * int(shoe)
            self.seven_rem = 4 * int(shoe)
            self.six_rem = 4 * int(shoe)
            self.five_rem = 4 * int(shoe)
            self.four_rem = 4 * int(shoe)
            self.three_rem = 4 * int(shoe)
            self.two_rem = 4 * int(shoe)
            self.decks_rem = int(shoe)

            self.button_log.clear()
            self.remove_widget(self.count_info)
            self.add_count(instance)
        else:
            print('Can not restart if start has not been pressed')
        
        

    def go_back(self, *args):
        print('Back button on the all methods page pressed')
        self.button_log.clear()
        if self.start_trigger:
            self.remove_widget(self.count_info)
            self.add_widget(self.start_button)
            self.start_trigger = False
        if self.red_trigger:
            self.remove_widget(self.red_seven_button)
            red = False
        sm.current = 'Counting Methods'


class HomePageScreen(Screen):
    
    def __init__(self, **kwargs):
        super(HomePageScreen, self).__init__(**kwargs)
        self.homepage_objects = HomePage()
        self.add_widget(self.homepage_objects)

class HowToPageScreen(Screen):
    
    def __init__(self, **kwargs):
        super(HowToPageScreen, self).__init__(**kwargs)
        self.howtopage_objects = HowToPage()
        self.add_widget(self.howtopage_objects)

class CountingMethodScreen(Screen):

    def __init__(self, **kwargs):
        super(CountingMethodScreen, self).__init__(**kwargs)
        self.countingmethodpage_objects = CountingMethodPage()
        self.add_widget(self.countingmethodpage_objects)

class AllMethodsScreen(Screen):

    def __init__(self, **kwargs):
        super(AllMethodsScreen, self).__init__(**kwargs)
        self.allmethodspage_objects = AllMethodsPage()
        self.add_widget(self.allmethodspage_objects)
        

class CardCounterApp(App):

    def build(self):
        
        global sm
        sm = ScreenManager()      
        sm.add_widget(HomePageScreen(name='Home'))
        sm.add_widget(HowToPageScreen(name='How To'))
        sm.add_widget(CountingMethodScreen(name='Counting Methods'))
        sm.add_widget(AllMethodsScreen(name='Method'))
        return sm
            

if __name__ == '__main__':    
    CardCounterApp().run()   
    
