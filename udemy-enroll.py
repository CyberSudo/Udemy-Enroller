import time
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
################################################################
print('''
  .   . .    .  .    .  :8t..X% .    .  .    .  .    .  .    .  .    .  .       
    .     .    .  .    : XXXXX8S  .    .  .    .  .    .  .    .  .    .  . .  .
  .    .   .       .  ::@XXXXXX:.  .       .       .       .       .            
     .   .   .  .    .;XXXXXXXX8%    .  .    .  .    .  .    .  .    .  .  . .  
  .    .      .   .  8@XXXXXXXX8%. .   .  .   .  ;XS: .   .   .   .   .   .    .
    .     . .   .   @@XXXXXXXXXX;    .      .  S:88@8 %    .    .   .   .    .  
  .   .           .88XXXXXXXXXX:.  .    .     88XXXXXX@% .   .    .        .    
    .   . .  . .  88XXXXXXXXXX88      .   .  t@XXXXXXXX%       .     . .  .   . 
  .         .   .88@XXXXXXXXXX%; .  .   .   :.XXXXXXXXX:. . .    .          .   
     . .  .    t.@XXXXXXXXXXX@8       .   .::XXXXXXXXXXX;     .    . .  .     . 
  .          .SXXXXXXXXXXXXXXX:  . .       t@XXXXXXXXXX@;  .    .      .  .     
    .  . . .:S8XXXXXXXXXXXXXXt .     .  . 88XXXXXXXXXXX@;    .    . .      . .  
  .       tt8XXXXXXXXXXXXXXX@%    .   .  88@XXXXXX@XXX@8;.    .       .  .     .
    . . :X8XXXXXXXXXXXXXXXXX   .    .   S8@XXXXX@      S;; .    . .     .   .   
  .     XXXXXXXXXXXXXXXXXXX88    .     ttXXXXX8@@      . 8   .      . .   .   . 
     .  ;.8XXX@@.@XXXXXXXXX%:  .   .  %%S @XX%@8%    .:;:%.    %%t;             
  .    . .X%:S@.%8XXXXXXXXXt     .   ::   . 88S   .:;;ttt.8tt:t  .8%.  . .  .  .
    .     .     XXXXXXXXXX88 .      :    .:. S   :;%%XS%Stt; S  .:: S:     .    
  .   . .   .  :tXXXXXXXXXX;   .  .%8   :;t;;:::;tS%SXX@St%t;:::;tt.:SX.     .  
    .     .   .%8@XXXXXXXX:. .   .:;  .:;%%S%t%%SXSSS%SXSXSSS%%%St%ttt.  .    . 
  .    .       8@XXXXXXXXX.    . t:@8  :%%X%SS%SXSS%%SS%S%SSS%SS%SS:;:    . .   
     .   .  . .XXXXXXXXXXX   . .88XX@@ :%S%%S%S% %%8@X8X @.t%%SS%%S.@   .      .
  .    .       @XXXXXXXXXX%:  .X@XXX@  ;tSS%%S%S:        .% :%%S%%%tS;     .    
    .     . .  8@XXXXXXXXX@:@8:8S      tSS%XS;.:    .  .   8 :t%S%St:8%::@.  .  
  .   .  .     ;@XXXXXXXXXXXXXXX      :t%%S%%S.  .   .      8.tt%%SXt;:;;X;   . 
    .       .  .;XXXXXXXXXXXXXX@     :t%SS%S%S .   .   . .  t .tSS%t%%%S%S;     
  .    .  .     t%XXXXXXXXXXXXX@   .;t%X%%t%%t   .   .      tX:SSS%SXXS%S%: .  .
     .   .   .  .;:8XXXXXXXXXXX88  :tS%%%SS%t8;.   .    .  .:.t%SSSS%%%St8:  .  
  .    .   .       @%@XXXXXXX8 X.X@.% ;SS%%%S:t.      .    8 :%XS%%S%8.X8t.     
    .        . .    :X@t::tX8t  .    t:tSSSSS%;@8.. .   .S   :%S%S@SX;.    .  . 
  .   .  .       .            .      :X;tSXS%S%t: @;..:SX   .;%XXXS:8   .       
    .   .  .  .   .       .      .   @ ;tSXSSXSt;:::::::;;;;t%X%%SS;8;    . . . 
  .         .   .   . . .   .  .   .t  ;SS%tS%%S%t%%%%%%SSS%XSS%%%S%t8%.        
     . .  .    .              .   ..XX.t%SS%%S%%SSSXS%SSXXS%%SSS%%SS:;%  .  .  .
  .      .   .    . .  .  . .   .    t@tSS%X: .;tXXSSS%%t%S%:X.;%SX 8      .    
    .  .   .    .       .          .  ;t  X.% 8;8;%X%%%%S .8t.8t  t%   . .   .  
  .           .    . .    .  . .  .     .%.     % :t%%S%;:      .;             .
    . . .  .    .      .            .        .   X:%XS%S%X      .  .  .  . .    
  .       .  .    .  .   . .  . .     .  .  .  . X8@88@@8: . .   .     .     .  
--------------------------------------------------------------------------------
                        |Udemy Enrolling Script|
Coded by @CyberSudo.
Don't forget to share it.
Please wait everything will happen in few seconds
Thank you for choosing this tool <3
''')
parser = argparse.ArgumentParser(description='Udemy Enrolling Script')
parser.add_argument('Email', metavar='Email', type=str , help='Enter your email')
parser.add_argument('Password', metavar='Password', type=str , help='Enter your password')
args = parser.parse_args()
Email = args.Email
Password = args.Password
def ask_user():
    check = str(input("Did you delete your credit cards first?! (Y/N): ")).lower().strip()
    try:
        if check[0] == 'y':
            print('Nice')
            time.sleep(1)
            print('Script starting...')
            return True
        elif check[0] == 'n':
            print('Please delete your card first because the script does not differentiate between paid and free')
            time.sleep(5)
            exit()
            return False
        else:
            print('Invalid Input')
            return ask_user()
    except Exception as error:
        print("Please enter valid inputs")
        print(error)
        return ask_user()
ask_user()
web = webdriver.Firefox()
web.get("https://www.udemy.com/")
web.implicitly_wait(5)
login_in = web.find_element_by_link_text("Log in").click()
web.implicitly_wait(5)
email = web.find_element_by_id("email--1").send_keys(Email)
Pass = web.find_element_by_id("id_password").send_keys(Password)
login = web.find_element_by_id("submit-id-submit").click()
web.implicitly_wait(6)
links = open("links.txt","r+")
lst_link = [link.partition('|')[0].strip() for link in links]
for enroll_link in lst_link:
    web.get(enroll_link)
    time.sleep(3)
    try:
        enroll_button = WebDriverWait(web, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".sidebar-container--purchase-section--17KRp > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(5) > div:nth-child(1) > button:nth-child(1)"))
        )
        enroll_button.click()
        time.sleep(6)
        web.find_element_by_css_selector('.styles--checkout-pane-outer--1syWc > div:nth-child(1) > div:nth-child(4) > button:nth-child(2)').click()
        time.sleep(5)
    except:
        continue
print('======= Done :) =======')
#web.close()