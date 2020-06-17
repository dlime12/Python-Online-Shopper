# The function for opening a web document given its URL.
from urllib.request import urlopen

# Import the standard Tkinter functions. 
from tkinter import *

# Functions for finding all occurrences of a pattern
# defined via a regular expression.  
from re import findall, finditer

# Import the standard SQLite functions just in case they're

from sqlite3 import *

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#


#########################################Tkinter Window configuration####################################

#Defining TK window
shop_window = Tk()

#Title of the Tkinter interface.
shop_window.title("Go Mart! Best Online Shop in Australia")
#Set the window size
shop_window.geometry("550x600")
#Set the background to white
shop_window.config(background = "White")
#Do not let window size be adjusted
shop_window.resizable(width= False, height = False)


##################################################Contents#############################################


#Welcome label 1, button package, placement 
shop_title_label_one = Label(shop_window, text = 'Welcome to GOnline! Mart',
                         font = ('Arial', 28, 'bold'), fg = 'Dark Green')
shop_title_label_one.pack()
shop_title_label_one.config(background = "White")
shop_title_label_one.place(x = 40, y = 20)

#Welcome label 2, button package, placement 
shop_title_label_two = Label(shop_window, text = 'Shop Anything Anytime!',
                         font = ('Arial', 25, 'bold'), fg = 'Dark Green')
shop_title_label_two.pack()
shop_title_label_two.config(background = "White")
shop_title_label_two.place(x = 75, y = 80)


########################################## Order Processes ##########################################


#Order guideline label, button package, placement
order_procedures = Label(shop_window, text = "Follow these steps to complete your order!",
                        font = ('Arial', 19, 'bold'), fg = 'Black')
order_procedures.pack()
order_procedures.config(background = "White")
order_procedures.place(x = 20, y = 150)

#Quantity guideline label, button package, placement
choose_quantity = Label(shop_window, text = "Step 1. Please choose your quantities.",
                        font = ('Arial', 16, 'bold'), fg = 'Purple')
choose_quantity.pack()
choose_quantity.config(background = "White")
choose_quantity.place(x = 50, y = 210)

#Product 1, anti-theft, label, button package, placement
anti_theft_product_GUI = Label(shop_window, text = "Anti-Theft Products",
                        font = ('Arial', 11, 'bold'), fg = 'Black')
anti_theft_product_GUI.pack()
anti_theft_product_GUI.config(background = "White")
anti_theft_product_GUI.place(x = 100, y = 260)

#Product 2, women's dress, label, button package, placement
womens_dress_GUI = Label(shop_window, text = "Women's Dress",
                        font = ('Arial', 11, 'bold'), fg = 'Black')
womens_dress_GUI.pack()
womens_dress_GUI.config(background = "White")
womens_dress_GUI.place(x = 100, y = 300)


#Product 3, indian handicrafts, label, button package, placement
indian_handicrafts_GUI = Label(shop_window, text = "Indian Handicrafts",
                        font = ('Arial', 11, 'bold'), fg = 'Black')
indian_handicrafts_GUI.pack()
indian_handicrafts_GUI.config(background = "White")
indian_handicrafts_GUI.place(x = 100, y = 340)



############################################## Quantity selection button ############################



#Variables of quantity for product 1
anti_theft_quantity_variable = ['0 Anti-Theft Product', '1 Anti-Theft Product', '2 Anti-Theft Product'
           , '3 Anti-Theft Product', '4 Anti-Theft Product', '5 Anti-Theft Product']
    

#Drop down menu configuration
anti_theft_variable = StringVar(shop_window)
anti_theft_variable.set('0 Anti-Theft Product') # Default value

#Creation of drop down button, package, placement
anti_theft_option = OptionMenu(shop_window, anti_theft_variable, *anti_theft_quantity_variable)
anti_theft_option.pack()
anti_theft_option.place(x = 270, y = 255)





#Variables of quantity for product 2
womens_dress_quantity_variable = ['0 Womens Dress       ', '1 Womens Dress       ', '2 Womens Dress       '
           , '3 Womens Dress       ', '4 Womens Dress       ', '5 Womens Dress       ']

#Drop down menu configuration
womens_dress_variable = StringVar(shop_window)
womens_dress_variable.set('0 Womens Dress       ') # Default value

#Creation of drop down button, package, placement
womens_dress_option = OptionMenu(shop_window, womens_dress_variable, *womens_dress_quantity_variable)
womens_dress_option.pack()
womens_dress_option.place(x = 270, y = 295)



#Variable of quantity for product 3
indian_handicrafts_quantity_variable = ['0 Indian Handicrafts ', '1 Indian Handicrafts ', '2 Indian Handicrafts '
           , '3 Indian Handicrafts ', '4 Indian Handicrafts ', '5 Indian Handicrafts ']

#Drop down menu configuration
indian_handicrafts_variable = StringVar(shop_window)
indian_handicrafts_variable.set('0 Indian Handicrafts ') # Default value

#Creation of drop down button, package, placement
indian_handicrafts_option = OptionMenu(shop_window, indian_handicrafts_variable, *indian_handicrafts_quantity_variable)
indian_handicrafts_option.pack()
indian_handicrafts_option.place(x = 270, y = 335)



################################################### Printing invoice #########################


#Print invoice label guideline, package, placement
print_invoice = Label(shop_window, text = "Step 2. Print your invoice.",
                        font = ('Arial', 16, 'bold'), fg = 'Blue')
print_invoice.pack()
print_invoice.config(background = "White")
print_invoice.place(x = 50, y = 390)







#definition for getting quantities for the product and also extracting necessary information into html
def get_quantity_products():

    #Updating label to necessary text
    print_invoice_press_first()


    #3 quantity variables for each product
    Anti_Theft_quantity = ['']

    Womens_Dresses_quantity = ['']

    Indian_Handicrafts_quantity = ['']

    #Get the Value of the Anti-Theft quantity
    print(anti_theft_variable.get())
    Anti_Theft_quantity.insert(0, (anti_theft_variable.get()))
    Anti_Theft_quantity.pop(1)
    #Get the Value of the Women's Dress quantity
    print(womens_dress_variable.get())
    Womens_Dresses_quantity.insert(0, (womens_dress_variable.get()))
    Womens_Dresses_quantity.pop(1)
    #Get the Value of the Indian Handicrafts quantity
    print(indian_handicrafts_variable.get())
    Indian_Handicrafts_quantity.insert(0, (indian_handicrafts_variable.get()))
    Indian_Handicrafts_quantity.pop(1)


    #Replace three variable's string with just number and into a variable not a list
    Anti_Theft_quantity = ([number.replace(' Anti-Theft Product', '') for number in Anti_Theft_quantity])
    Anti_Theft_quantity = int((Anti_Theft_quantity[0]))


    Womens_Dresses_quantity = ([number.replace(' Womens Dress       ', '') for number in Womens_Dresses_quantity])
    Womens_Dresses_quantity = int((Womens_Dresses_quantity[0]))

    Indian_Handicrafts_quantity = ([number.replace(' Indian Handicrafts ', '') for number in Indian_Handicrafts_quantity])
    Indian_Handicrafts_quantity = int((Indian_Handicrafts_quantity[0]))

    


    ################################## Website Extractions #############################################
   


    ############################### First website ##############################################

    #Necessary label text for situation 
    print_invoice_press_one()
    
    #Define the url of the first category, Woman's dresses
    Anti_Theft_url = 'https://www.crimezappers.com/rss/catalog/new/store_id/1/'

    #Get the link to the web page from the server.
    Anti_Theft_page = urlopen(Anti_Theft_url)

    #Extract the web page's content as a string
    Anti_Theft_HTML_code = Anti_Theft_page.read()

    #Close the connection to the web server
    Anti_Theft_page.close()


    ################################ First product Name ################################


    #Regex code for extracing necessary names of Anti Theft Products
    Anti_Theft_Product_Names = findall('m\>\s+<title\>\<\!\[CDATA\[([A-Za-z0-9\,\;\+\&\%\.\﻿\/\'\‘\®\½\-\–\(\) ]+)\]\]\>\<\/title>', Anti_Theft_HTML_code)


    #Determines if the user chose any quantity, if no do nothing, if yes print the name depending on how many quantity
    
    if Anti_Theft_quantity == 0:
        pass
    else:
        print("\n")
        for products in range(Anti_Theft_quantity):
            print(Anti_Theft_Product_Names[products])
            

    ################################ First product price ################################    


    #Regex code for extracting necessary prices of Anti Theft Products
    Anti_Theft_Product_Prices = findall('\$([0-9\.\, ]+)', Anti_Theft_HTML_code)


    #Determines if the user chose any quantity, if no do nothing, if yes print the price depending on how many quantity
    
    if Anti_Theft_quantity == 0:
        pass
    else:
        print("\n")
        for prices in range(Anti_Theft_quantity):
            print("USD$",Anti_Theft_Product_Prices[prices])



    ########################## First product conversion  ######################

    #Definition which Determines if the user chose any quantity, if no do nothing, if yes convert the price to AUD dollars.
    def USD_to_AUD_Anti_Theft():
        if Anti_Theft_quantity == 0:
            pass
        else:
            print("\n")
            #For quantity repeat the code x times.
            for number in range(Anti_Theft_quantity):
                #Converts to number multiplies by currecny and back to string
                Anti_Theft_Product_Prices[number] = str(float(Anti_Theft_Product_Prices[number]) * 1.33)
                #Adding 0.5 rounds up to 2 decimals points and saves as list if needed.
                if len((Anti_Theft_Product_Prices[number]).rsplit('.')[-1]) >= 2:
                    Anti_Theft_Product_Prices[number] = int(((float(Anti_Theft_Product_Prices[number])) * 100) + 0.5) /100.0
                else:
                    pass
                print("AUD $", Anti_Theft_Product_Prices[number])

    #Run the conversion
    USD_to_AUD_Anti_Theft()


    ############################ First Product picture  ########################################


    #Regex code for extracting necessary picutres of Anti Theft Products
    Anti_Theft_Product_Pictures = findall('\<img src\=\"([A-Za-z0-9\:\/\.\-\_]+)\"', Anti_Theft_HTML_code)


    #Determines if the user chose any quantity, if no do nothing, if yes print the picture address depending on how many quantity     
    if Anti_Theft_quantity == 0:
        pass
    else:
        print("\n")
        for picture_link in range(Anti_Theft_quantity):
            print(Anti_Theft_Product_Pictures[picture_link])


    ##########################################################################################

            



      
    ############################### Second website ##############################################


    #Changes to necessary text for the labe 
    print_invoice_press_two()

    #Define the url of the first category, Woman's dresses
    Womens_Dresses_url = 'http://www.joomlajingle.com/rss/catalog/new/store_id/1/'

    #Get the link to the web page from the server.
    Womens_Dresses_page = urlopen(Womens_Dresses_url)

    #Extract the web page's content as a string
    Womens_Dresses_HTML_code = Womens_Dresses_page.read()

    #Close the connection to the web server
    Womens_Dresses_page.close()


    #Uses Regex code to find all necessary names of the Womens' Dress
    Womens_Dresses_Product_Names = findall('m\>\s+<title\>\<\!\[CDATA\[([A-Za-z0-9\,\;\+\&\%\.\﻿\/\'\‘\®\-\–\(\) ]+)\]\]\>\<\/title>', Womens_Dresses_HTML_code)


    #Determines if the user chose any quantity, if no do nothing, if yes print the name depending on how many quantity
    if Womens_Dresses_quantity == 0:
        pass
    else:
        print('\n\n')
        for products in range(Womens_Dresses_quantity):
            print(Womens_Dresses_Product_Names[products])
            


    ################################ Second product price ################################    


    #Regex code to find all necessary prices for Women's dress
    Womens_Dresses_Product_Prices = findall('product\-price\-[0-9]+\"\>\$([0-9\.\, ]+)\<\/span\>', Womens_Dresses_HTML_code)


    #Determines if the user chose any quantity, if no do nothing, if yes print the price depending on how many quantity
    if Womens_Dresses_quantity == 0:
        pass
    else:
        print("\n")
        for prices in range(Womens_Dresses_quantity):
            print("USD $", Womens_Dresses_Product_Prices[prices])



    ########################## Second product conversion  ######################

            
    #Definition which Determines if the user chose any quantity, if no do nothing, if yes convert the price to AUD dollars.    
    def USD_to_AUD_Womens_Dresses():
        if Womens_Dresses_quantity == 0:
            pass
        else:
            print("\n")
            for number in range(Womens_Dresses_quantity):
                #Converts to number multiplies by currecny and back to string
                Womens_Dresses_Product_Prices[number] = str(float(Womens_Dresses_Product_Prices[number]) * 1.33)
                #Adding 0.5 rounds up to 2 decimals points and saves as list if needed.
                if len((Womens_Dresses_Product_Prices[number]).rsplit('.')[-1]) >= 2:
                    Womens_Dresses_Product_Prices[number] = int(((float(Womens_Dresses_Product_Prices[number])) * 100) + 0.5) /100.0
                else:
                    pass
                print("AUD $", Womens_Dresses_Product_Prices[number])

    #Runs the conversion
    USD_to_AUD_Womens_Dresses()




    ############################ Second Product picture  ########################################


    #Regex code to find all necessary pictures for Women's dress
    Womens_Dresses_Product_Pictures = findall('\<img src\=\"([A-Za-z0-9\:\/\.\-\_]+)\"', Womens_Dresses_HTML_code)


    #Determines if the user chose any quantity, if no do nothing, if yes print the picture address depending on how many quantity
    if Womens_Dresses_quantity == 0:
        pass
    else:
        print("\n")
        for pictures in range(Womens_Dresses_quantity):
            print(Womens_Dresses_Product_Pictures[pictures])


        

    #########################################################################################






     
    ############################### Third website ##############################################

    #Necessary text for the label updating its progress    
    print_invoice_press_three()

    #Define the url of the first category, Indian Handicrafts
    Indian_Handicrafts_url = 'http://india-shopping.khazano.com/rss/catalog/category/cid/5/store_id/1/'

    #Get the link to the web page from the server.
    Indian_Handicrafts_page = urlopen(Indian_Handicrafts_url)

    #Extract the web page's content as a string
    Indian_Handicrafts_HTML_code = Indian_Handicrafts_page.read()

    #Close the connection to the web server
    Indian_Handicrafts_page.close()


    #Regex code to find all necessary names for Indian Handicrafts 
    Indian_Handicrafts_Product_Names = findall('m\>\s+<title\>\<\!\[CDATA\[([A-Za-z0-9\,\;\+\&\%\.\﻿\/\'\‘\®\-\–\(\) ]+)\]\]\>\<\/title>', Indian_Handicrafts_HTML_code)

   
    #Determines if the user chose any quantity, if no do nothing, if yes print the name depending on how many quantity
    print("\n")
    if Indian_Handicrafts_quantity == 0:
        pass
    else:
        for products in range(Indian_Handicrafts_quantity):
            print(Indian_Handicrafts_Product_Names[products])
            


    ################################ Third product price ################################    



    #Regex code to find all necessary prices for Indian Handicrafts   
    Indian_Handicrafts_Product_Prices = findall('price\"\>Rs\. ([0-9\.\, ]+)\<\/span\>', Indian_Handicrafts_HTML_code)



    #Determines if the user chose any quantity, if no do nothing, if yes print the name depending on how many quantity
    print #New line
    if Indian_Handicrafts_quantity == 0:
        pass
    else:
        for prices in range(Indian_Handicrafts_quantity):
            print("Rs. ", Indian_Handicrafts_Product_Prices[prices])




    ########################## Third product conversion  ######################


    #Definition which Determines if the user chose any quantity, if no do nothing, if yes convert the price to AUD dollars.  
    def USD_to_AUD_Indian_Handicrafts():
        if Indian_Handicrafts_quantity == 0:
            pass
        else:
            for number in range(Indian_Handicrafts_quantity):
                Indian_Handicrafts_Product_Prices[number] = Indian_Handicrafts_Product_Prices[number].replace(",", "")
                #Converts to number multiplies by currecny and back to string
                Indian_Handicrafts_Product_Prices[number] = str(float(Indian_Handicrafts_Product_Prices[number]) * 0.021)
                #Adding 0.5 rounds up to 2 decimals points and saves as list if needed.
                if len((Indian_Handicrafts_Product_Prices[number]).rsplit('.')[-1]) >= 2:
                    Indian_Handicrafts_Product_Prices[number] = int(((float(Indian_Handicrafts_Product_Prices[number])) * 100) + 0.5) /100.0
                else:
                    pass
                print("AUD $", Indian_Handicrafts_Product_Prices[number])
                
    #Make the conversion if necessary
    USD_to_AUD_Indian_Handicrafts()




    ############################ Third Product picture  ########################################


    #Regex code to find all necessary pictures for Indian Handicrafts  
    Indian_Handicrafts_Product_Pictures = findall('\<img src\=\"([A-Za-z0-9\:\/\.\-\_]+)\"', Indian_Handicrafts_HTML_code)



    #Determines if the user chose any quantity, if no do nothing, if yes print the picture link depending on how many quantity
    print("\n")
    if Indian_Handicrafts_quantity == 0:
        pass
    else:
        for pictures in range(Indian_Handicrafts_quantity):
            print(Indian_Handicrafts_Product_Pictures[pictures])


    ############################################################################################



    #Lines of code which will calculate the total price for the amount of products user orderded
            
    #Empty list for all the prices
    total_price =[]

    #3 lines of code below will gather all the prices into total_price list
    for number in range(Anti_Theft_quantity):
            total_price.append((Anti_Theft_Product_Prices[number]))
            
    for number in range(Womens_Dresses_quantity):
            total_price.append((Womens_Dresses_Product_Prices[number]))
            
    for number in range(Indian_Handicrafts_quantity):
            total_price.append((Indian_Handicrafts_Product_Prices[number]))


    #Adds all the prices
    total_price = sum(total_price)

    #Rounds the price to 2 decimal places
    total_price = round(total_price, 2)

    #Prints the total amount
    print("\n\n The total cost is AUD $",  total_price)

      
    ########################################### HTML Coding ############################################


    #Define the name of the invoice file
    HTML_file_name = 'invoice.html'

    #If the invoice file is already created, it will delete the old and create the new one.
    create_invoice_file = open(HTML_file_name, 'w')


    #HTML code of the invoice file defined as html_structure
    HTML_Structure_Style="""<!DOCTYPE html>
    <html>

    <head>
     <title>GOnline! Mart invoice</title>
     
     <style>

      html {
        min-width: 100%;
        min-height: 100%;
        background-position: top center;
        background-color: #525659;
      }
      
      body {
        background-color: #ffffff;
        width: 80%;
        margin-left: auto;
        margin-right: auto;
        margin-top: 80px; 
        margin-bottom: 80px;
      }

      table, th, td {
        border: 1px solid black;
        table-layout: fixed;
        word-wrap:break-word;
    
      }


      th, td {
        padding: 15px;
      }


      th {
        font-size: 22px;
        width: 300px;

      }


      h1 {
        font-weight: bold;
        font-size: 44px;
        font-family:verdana;
      }
      
      h2 {
        font-weight: bold;
        font-size: 36px;
        font-family:verdana;
      }
      
      h4 {
        font-size: 26px;
        font-family:verdana;
      }

      h5 {
        font-size: 25px;
      }
      ul { 
        display:table; margin:0 auto;
      }

      </style>
    </head>\n\n"""

    shop_title_image ="""    <body>
      <br>
      <h1 align="center"><i>GOnline! Mart</i>.. Shop Anything, Anytime!</h1>

      <p align="center"><img src="http://cdn.phillymag.com/wp-content/uploads/sites/3/2015/01/Shopping-Cart-illo.jpg" alt="Company logo"
         style="width:600px;height:300px; align="auto">"""





    buy_products ="""      </p><h2 align="center">Thank you for Shopping with <i>GOnline! Mart!!</i></h2>

      <h4 align="center">Your invoice with price is displayed below...</h4>"""








    start_table ="""      <table align="center">\n\n"""
    end_table ="""      </table>\n\n"""


    supporters_list ="""      <br>
      <br>

      <p style="font-size: 17px;", align="center"><b><i>GOnline! Mart</i> is proudly supported by...</b></p>
      <ul>
        <li><a href="https://www.crimezappers.com/">Crime Zappers</a></li>
        <li><a href="http://www.joomlajingle.com/">Dress for Sale</a></li>
        <li><a href="http://india-shopping.khazano.com/indian-handicrafts.html">Khazano - Indian Handicrafts</a></li>
      </ul>
      <br>
      <br>
      <br>
    </body>

    </html>"""


    #Add the HTML codes into the invoice file
    create_invoice_file.write(HTML_Structure_Style)
    create_invoice_file.write(shop_title_image)
    if Anti_Theft_quantity == Womens_Dresses_quantity == Indian_Handicrafts_quantity == 0:
        create_invoice_file.write("""<h2 align="center">Thank you for using <i>GOnline! Mart!!</i></h2>
      <h4 style="color:#32CD32;", align="center">No Charge! Please come again...</h4>
      <h5></h5>""")
    else:
        create_invoice_file.write(buy_products)


        
        create_invoice_file.write('      <h4 style="color:#FF5733;" align= "center"><b>Total Price: AUD $'+ str(total_price)  + '</b></h4>') 

        if Anti_Theft_quantity == 0:
            pass
        elif Anti_Theft_quantity != 0:
            for number in range(Anti_Theft_quantity):
                create_invoice_file.write(start_table)
                create_invoice_file.write('        <tr>\n' +'          <th>' + Anti_Theft_Product_Names[number] +' <br><br>'
                                          +' AUD $' + str(Anti_Theft_Product_Prices[number]) + '</th>\n'
                                          "           <td><img src='" + Anti_Theft_Product_Pictures[number] + "'" +
                                          '            width= "300" height= "300" align="center"></td>')
                create_invoice_file.write(end_table)

        if Womens_Dresses_quantity == 0:
            pass
        elif Womens_Dresses_quantity != 0:
            for number in range(Womens_Dresses_quantity):
                create_invoice_file.write(start_table)
                create_invoice_file.write('        <tr>\n' +'          <th>' + Womens_Dresses_Product_Names[number] +' <br><br>'
                                          +' AUD $' + str(Womens_Dresses_Product_Prices[number]) + '</th>\n'
                                          "           <td><img src='" + Womens_Dresses_Product_Pictures[number] + "'" +
                                          '            width= "300" height= "300" align="center"></td>')
                create_invoice_file.write(end_table)
 

        if Indian_Handicrafts_quantity == 0:
            pass
        elif Indian_Handicrafts_quantity != 0:
            for number in range(Indian_Handicrafts_quantity):
                create_invoice_file.write(start_table)
                create_invoice_file.write('        <tr>\n' +'          <th>' + Indian_Handicrafts_Product_Names[number] +' <br><br>'
                                          +' AUD $' + str(Indian_Handicrafts_Product_Prices[number]) + '</th>\n'
                                          "           <td><img src='" + Indian_Handicrafts_Product_Pictures[number] + "'" +
                                          '            width= "300" height= "300" align="center"></td>')
                create_invoice_file.write(end_table)


    create_invoice_file.write(supporters_list)

    #Close and save the HTML file
    create_invoice_file.close()



    print_invoice_finished()

    save_order_ready()





#A definition which will insert the selected names and prices into the database
def save_order_into_sqlite():

    save_order_happening()


    ##         #########       #######         This part is not relevent.. skip until you see this same comment again      ##########         ########### ###########   ###
   
    Anti_Theft_quantity = ['']

    Womens_Dresses_quantity = ['']

    Indian_Handicrafts_quantity = ['']

    #Anti-Theft
    print(anti_theft_variable.get())
    Anti_Theft_quantity.insert(0, (anti_theft_variable.get()))
    Anti_Theft_quantity.pop(1)
    #Women's Dress
    print(womens_dress_variable.get())
    Womens_Dresses_quantity.insert(0, (womens_dress_variable.get()))
    Womens_Dresses_quantity.pop(1)
    #Indian Handicrafts
    print(indian_handicrafts_variable.get())
    Indian_Handicrafts_quantity.insert(0, (indian_handicrafts_variable.get()))
    Indian_Handicrafts_quantity.pop(1)
    print(Anti_Theft_quantity)
    print(Womens_Dresses_quantity)
    print(Indian_Handicrafts_quantity)

    Anti_Theft_quantity = ([number.replace(' Anti-Theft Product', '') for number in Anti_Theft_quantity])
    Anti_Theft_quantity = int((Anti_Theft_quantity[0]))
    print(Anti_Theft_quantity)


    Womens_Dresses_quantity = ([number.replace(' Womens Dress       ', '') for number in Womens_Dresses_quantity])
    Womens_Dresses_quantity = int((Womens_Dresses_quantity[0]))
    print(Womens_Dresses_quantity)

    Indian_Handicrafts_quantity = ([number.replace(' Indian Handicrafts ', '') for number in Indian_Handicrafts_quantity])
    Indian_Handicrafts_quantity = int((Indian_Handicrafts_quantity[0]))
    print(Indian_Handicrafts_quantity)
    

    ############################### First website ##############################################
    #Define the url of the first category, Woman's dresses
    Anti_Theft_url = 'https://www.crimezappers.com/rss/catalog/new/store_id/1/'

    #Get the link to the web page from the server.
    Anti_Theft_page = urlopen(Anti_Theft_url)

    #Extract the web page's content as a string
    Anti_Theft_HTML_code = Anti_Theft_page.read()

    #Close the connection to the web server
    Anti_Theft_page.close()


    ################################ First product Name ################################


    #str(Anti_Theft_quantity[0]).strip('[]')
    #print '\n'.join(mylist)

    # just in case <title><!\[CDATA\[([A-Za-z ]+)\
    Anti_Theft_Product_Names = findall('m\>\s+<title\>\<\!\[CDATA\[([A-Za-z0-9\,\;\+\&\%\.\﻿\/\'\‘\®\½\-\–\(\) ]+)\]\]\>\<\/title>', Anti_Theft_HTML_code)


    print("\n\nThere are ", len(Anti_Theft_Product_Names), "available for purchase today.")

    if Anti_Theft_quantity == 0:
        print("And you have ordered... None for today", "\nThank you for visiting!")
    else:
        print("And you orderded", Anti_Theft_quantity, "Anti Theft Products")
        print("The products you have ordered are listed below:\n")
        for products in range(Anti_Theft_quantity):
            print(Anti_Theft_Product_Names[products])
            

    ################################ First product price ################################    

    Anti_Theft_Product_Prices = findall('\$([0-9\.\, ]+)', Anti_Theft_HTML_code)


    print("\n\nThere are ", len(Anti_Theft_Product_Prices), "Anti Theft products available for sale today.")

    if Anti_Theft_quantity == 0:
        print("And your pending balance is... None for today", "\nThank you for visiting!")
    else:
        print("And you orderded", Anti_Theft_quantity, "Anti Theft Products")
        print("The prices for the product you have ordered are listed below:\n")
        for prices in range(Anti_Theft_quantity):
            print("USD$",Anti_Theft_Product_Prices[prices])



    ########################## First product conversion  ######################
    print("\n")

    def USD_to_AUD_Anti_Theft():
        if Anti_Theft_quantity == 0:
            pass
        else:
            for number in range(Anti_Theft_quantity):
                Anti_Theft_Product_Prices[number] = str(float(Anti_Theft_Product_Prices[number]) * 1.33)
                #Adding 0.5 rounds up to 2 decimals points
                if len((Anti_Theft_Product_Prices[number]).rsplit('.')[-1]) >= 2:
                    Anti_Theft_Product_Prices[number] = int(((float(Anti_Theft_Product_Prices[number])) * 100) + 0.5) /100.0
                else:
                    pass
                print("AUD $", Anti_Theft_Product_Prices[number])

    USD_to_AUD_Anti_Theft()


    ############################ First Product picture  ########################################

    Anti_Theft_Product_Pictures = findall('\<img src\=\"([A-Za-z0-9\:\/\.\-\_]+)\"', Anti_Theft_HTML_code)

    if Anti_Theft_quantity == 0:
        pass
    else:
        print("\n\nAnd you orderded", Anti_Theft_quantity, "Anti Theft Products")
        print(len(Anti_Theft_Product_Pictures))
        print("The picture linke for product is listed below:\n")
        for picture_link in range(Anti_Theft_quantity):
            print(Anti_Theft_Product_Pictures[picture_link])


    ##########################################################################################

            

      
    ############################### Second website ##############################################

    #Define the url of the first category, Woman's dresses
    Womens_Dresses_url = 'http://www.joomlajingle.com/rss/catalog/new/store_id/1/'

    #Get the link to the web page from the server.
    Womens_Dresses_page = urlopen(Womens_Dresses_url)

    #Extract the web page's content as a string
    Womens_Dresses_HTML_code = Womens_Dresses_page.read()

    #Close the connection to the web server
    Womens_Dresses_page.close()


    Womens_Dresses_Product_Names = findall('m\>\s+<title\>\<\!\[CDATA\[([A-Za-z0-9\,\;\+\&\%\.\﻿\/\'\‘\®\-\–\(\) ]+)\]\]\>\<\/title>', Womens_Dresses_HTML_code)


    print("\n\n\n\nThere are ", len(Womens_Dresses_Product_Names), "Women's Dresses available for purchase today.")

    if Womens_Dresses_quantity == 0:
        print("And you have ordered... None for today", "\nThank you for visiting!")
    else:
        print("And you orderded", Womens_Dresses_quantity, "dresses")
        print("The products you have ordered are listed below:\n")
        for products in range(Womens_Dresses_quantity):
            print(Womens_Dresses_Product_Names[products])
            

    ################################ Second product price ################################    

    Womens_Dresses_Product_Prices = findall('product\-price\-[0-9]+\"\>\$([0-9\.\, ]+)\<\/span\>', Womens_Dresses_HTML_code)


    print("\n\nThere are ", len(Womens_Dresses_Product_Prices), "Womens Dresses available for sale today.")

    if Womens_Dresses_quantity == 0:
        print("And your pending balance is... None for today", "\nThank you for visiting!")
    else:
        print("And you orderded", Womens_Dresses_quantity, "dresses")
        print("The product prices you have ordered are listed below:\n")
        for prices in range(Womens_Dresses_quantity):
            print("USD $", Womens_Dresses_Product_Prices[prices])




    ########################## Second product conversion  ######################

    print("\n")

    def USD_to_AUD_Womens_Dresses():
        if Womens_Dresses_quantity == 0:
            pass
        else:
            for number in range(Womens_Dresses_quantity):
                Womens_Dresses_Product_Prices[number] = str(float(Womens_Dresses_Product_Prices[number]) * 1.33)
                #Adding 0.5 rounds up to 2 decimals points
                if len((Womens_Dresses_Product_Prices[number]).rsplit('.')[-1]) >= 2:
                    Womens_Dresses_Product_Prices[number] = int(((float(Womens_Dresses_Product_Prices[number])) * 100) + 0.5) /100.0
                else:
                    pass
                print("AUD $", Womens_Dresses_Product_Prices[number])

    USD_to_AUD_Womens_Dresses()




    ############################ Second Product picture  ########################################

    Womens_Dresses_Product_Pictures = findall('\<img src\=\"([A-Za-z0-9\:\/\.\-\_]+)\"', Womens_Dresses_HTML_code)

    if Womens_Dresses_quantity == 0:
        print("\n\nAnd you have ordered... None for today", "\nThank you for visiting!")
    else:
        print("\n\nAnd you orderded", Womens_Dresses_quantity, "Women's dresses")
        print(len(Womens_Dresses_Product_Pictures))
        print("The product's picture link is below:\n")
        for pictures in range(Womens_Dresses_quantity):
            print(Womens_Dresses_Product_Pictures[pictures])


        

    #########################################################################################




     
    ############################### Third website ##############################################

    #Define the url of the first category, Indian Handicrafts
    Indian_Handicrafts_url = 'http://india-shopping.khazano.com/rss/catalog/category/cid/5/store_id/1/'

    #Get the link to the web page from the server.
    Indian_Handicrafts_page = urlopen(Indian_Handicrafts_url)

    #Extract the web page's content as a string
    Indian_Handicrafts_HTML_code = Indian_Handicrafts_page.read()

    #Close the connection to the web server
    Indian_Handicrafts_page.close()



    Indian_Handicrafts_Product_Names = findall('m\>\s+<title\>\<\!\[CDATA\[([A-Za-z0-9\,\;\+\&\%\.\﻿\/\'\‘\®\-\–\(\) ]+)\]\]\>\<\/title>', Indian_Handicrafts_HTML_code)


    print("\n\n\n\nThere are ", len(Indian_Handicrafts_Product_Names), "Indian Handicrafts available for purchase today.")

    if Indian_Handicrafts_quantity == 0:
        print("And you have ordered... None for today", "\nThank you for visiting!")
    else:
        print("And you orderded", Indian_Handicrafts_quantity, "Indian Handicrafts")
        print("The products you have ordered are listed below:\n")
        for products in range(Indian_Handicrafts_quantity):
            print(Indian_Handicrafts_Product_Names[products])
            

    ################################ Third product price ################################    

    Indian_Handicrafts_Product_Prices = findall('price\"\>Rs\. ([0-9\.\, ]+)\<\/span\>', Indian_Handicrafts_HTML_code)


    print("\n\nThere are ", len(Indian_Handicrafts_Product_Prices), "Indian Handicrafts available for sale today.")

    if Indian_Handicrafts_quantity == 0:
        print("And your pending balance is... None for today", "\nThank you for visiting!")
    else:
        print("And you orderded", Indian_Handicrafts_quantity, "Indian Handicrafts")
        print("The product prices you have ordered are listed below:\n")
        for prices in range(Indian_Handicrafts_quantity):
            print("Rs. ", Indian_Handicrafts_Product_Prices[prices])




    ########################## Third product conversion  ######################

    print("\n")

    def USD_to_AUD_Indian_Handicrafts():
        if Indian_Handicrafts_quantity == 0:
            pass
        else:
            for number in range(Indian_Handicrafts_quantity):
                Indian_Handicrafts_Product_Prices[number] = Indian_Handicrafts_Product_Prices[number].replace(",", "")
                Indian_Handicrafts_Product_Prices[number] = str(float(Indian_Handicrafts_Product_Prices[number]) * 0.021)
                 #Adding 0.5 rounds up to 2 decimals points
                if len((Indian_Handicrafts_Product_Prices[number]).rsplit('.')[-1]) >= 2:
                    Indian_Handicrafts_Product_Prices[number] = int(((float(Indian_Handicrafts_Product_Prices[number])) * 100) + 0.5) /100.0
                else:
                    pass
                print("AUD $", Indian_Handicrafts_Product_Prices[number])
                

    USD_to_AUD_Indian_Handicrafts()




    ############################ Third Product picture  ########################################

    Indian_Handicrafts_Product_Pictures = findall('\<img src\=\"([A-Za-z0-9\:\/\.\-\_]+)\"', Indian_Handicrafts_HTML_code)

    if Indian_Handicrafts_quantity == 0:
        print("\n\nAnd you have ordered... None for today", "\nThank you for visiting!")
    else:
        print("\n\nAnd you orderded", Indian_Handicrafts_quantity, "Indian Handicrafts")
        print(len(Indian_Handicrafts_Product_Pictures))
        print("The product's picture link is below:\n")
        for pictures in range(Indian_Handicrafts_quantity):
            print(Indian_Handicrafts_Product_Pictures[pictures])


    ############################################################################################


    total_price =[]

    for number in range(Anti_Theft_quantity):
            total_price.append((Anti_Theft_Product_Prices[number]))
            
    for number in range(Womens_Dresses_quantity):
            total_price.append((Womens_Dresses_Product_Prices[number]))
            
    for number in range(Indian_Handicrafts_quantity):
            total_price.append((Indian_Handicrafts_Product_Prices[number]))

    total_price = sum(total_price)

    total_price = round(total_price, 2)

    print("\n\n AUD $",  total_price)

      
    ############################################################################################



      
    ########################################### HTML Coding ############################################


    #Define the name of the invoice file
    HTML_file_name = 'invoice.html'

    #If the invoice file is already created, it will delete the old and create the new one.
    create_invoice_file = open(HTML_file_name, 'w')


    #HTML code of the invoice file defined as html_structure
    HTML_Structure_Style="""<!DOCTYPE html>
    <html>

    <head>
     <title>GOnline! Mart invoice</title>
     
     <style>

      html {
        min-width: 100%;
        min-height: 100%;
        background-position: top center;
        background-color: #525659;
      }
      
      body {
        background-color: #ffffff;
        width: 80%;
        margin-left: auto;
        margin-right: auto;
        margin-top: 80px; 
        margin-bottom: 80px;
      }

      table, th, td {
        border: 1px solid black;
        table-layout: fixed;
        word-wrap:break-word;
    
      }


      th, td {
        padding: 15px;
      }


      th {
        font-size: 22px;
        width: 300px;

      }


      h1 {
        font-weight: bold;
        font-size: 44px;
        font-family:verdana;
      }
      
      h2 {
        font-weight: bold;
        font-size: 36px;
        font-family:verdana;
      }
      
      h4 {
        font-size: 26px;
        font-family:verdana;
      }

      h5 {
        font-size: 25px;
      }
      ul { 
        display:table; margin:0 auto;
      }

      </style>
    </head>\n\n"""

    shop_title_image ="""    <body>
      <br>
      <h1 align="center"><i>GOnline! Mart</i>.. Shop Anything, Anytime!</h1>

      <p align="center"><img src="http://cdn.phillymag.com/wp-content/uploads/sites/3/2015/01/Shopping-Cart-illo.jpg" alt="Company logo"
         style="width:600px;height:300px; align="auto">"""





    buy_products ="""      </p><h2 align="center">Thank you for Shopping with <i>GOnline! Mart!!</i></h2>

      <h4 align="center">Your invoice with price is displayed below...</h4>"""








    start_table ="""      <table align="center">\n\n"""
    end_table ="""      </table>\n\n"""


    supporters_list ="""      <br>
      <br>

      <p style="font-size: 17px;", align="center"><b><i>GOnline! Mart</i> is proudly supported by...</b></p>
      <ul>
        <li><a href="https://www.crimezappers.com/">Crime Zappers</a></li>
        <li><a href="http://www.joomlajingle.com/">Dress for Sale</a></li>
        <li><a href="http://india-shopping.khazano.com/indian-handicrafts.html">Khazano - Indian Handicrafts</a></li>
      </ul>
      <br>
      <br>
      <br>
    </body>

    </html>"""


    #Add the HTML codes into the invoice file
    create_invoice_file.write(HTML_Structure_Style)
    create_invoice_file.write(shop_title_image)
    if Anti_Theft_quantity == Womens_Dresses_quantity == Indian_Handicrafts_quantity == 0:
        create_invoice_file.write("""<h2 align="center">Thank you for using <i>GOnline! Mart!!</i></h2>
      <h4 style="color:#32CD32;", align="center">No Charge! Please come again...</h4>
      <h5></h5>""")
    else:
        create_invoice_file.write(buy_products)


        
        create_invoice_file.write('      <h4 style="color:#FF5733;" align= "center"><b>Total Price: AUD $'+ str(total_price)  + '</b></h4>') 

        if Anti_Theft_quantity == 0:
            pass
        elif Anti_Theft_quantity != 0:
            for number in range(Anti_Theft_quantity):
                create_invoice_file.write(start_table)
                create_invoice_file.write('        <tr>\n' +'          <th>' + Anti_Theft_Product_Names[number] +' <br><br>'
                                          +' AUD $' + str(Anti_Theft_Product_Prices[number]) + '</th>\n'
                                          "           <td><img src='" + Anti_Theft_Product_Pictures[number] + "'" +
                                          '            width= "300" height= "300" align="center"></td>')
                create_invoice_file.write(end_table)

        if Womens_Dresses_quantity == 0:
            pass
        elif Womens_Dresses_quantity != 0:
            for number in range(Womens_Dresses_quantity):
                create_invoice_file.write(start_table)
                create_invoice_file.write('        <tr>\n' +'          <th>' + Womens_Dresses_Product_Names[number] +' <br><br>'
                                          +' AUD $' + str(Womens_Dresses_Product_Prices[number]) + '</th>\n'
                                          "           <td><img src='" + Womens_Dresses_Product_Pictures[number] + "'" +
                                          '            width= "300" height= "300" align="center"></td>')
                create_invoice_file.write(end_table)
 

        if Indian_Handicrafts_quantity == 0:
            pass
        elif Indian_Handicrafts_quantity != 0:
            for number in range(Indian_Handicrafts_quantity):
                create_invoice_file.write(start_table)
                create_invoice_file.write('        <tr>\n' +'          <th>' + Indian_Handicrafts_Product_Names[number] +' <br><br>'
                                          +' AUD $' + str(Indian_Handicrafts_Product_Prices[number]) + '</th>\n'
                                          "           <td><img src='" + Indian_Handicrafts_Product_Pictures[number] + "'" +
                                          '            width= "300" height= "300" align="center"></td>')
                create_invoice_file.write(end_table)


    create_invoice_file.write(supporters_list)

    #Close and save the HTML file
    create_invoice_file.close()





    ##         #########       #######         This part is not relevent.. skip until you see this same comment again      ##########         ########### ###########   ###

    #Create a connection to Shopping_trolley database
    connection = connect('shopping_trolley.db')


    #Get a Pointer into the database
    shopping_trolley_db = connection.cursor()


    #Delete any existing data in the database
    shopping_trolley_db.execute("DELETE FROM Purchases")


    #For the chosen product by user insert all the product names and prices for the chosen products into the database
    for number in reversed(range(Indian_Handicrafts_quantity)):
        shopping_trolley_db.execute("INSERT INTO Purchases VALUES ('" + Indian_Handicrafts_Product_Names[number] + "', '" +
                        str(Indian_Handicrafts_Product_Prices[number]) + "')")



    for number in reversed(range(Womens_Dresses_quantity)):
        shopping_trolley_db.execute("INSERT INTO Purchases VALUES ('" + Womens_Dresses_Product_Names[number] + "', '" +
                        str(Womens_Dresses_Product_Prices[number]) + "')")
        

    for number in reversed(range(Anti_Theft_quantity)):
        shopping_trolley_db.execute("INSERT INTO Purchases VALUES ('" + Anti_Theft_Product_Names[number] + "', '" +
                        str(Anti_Theft_Product_Prices[number]) + "')")



    #commit the changes
    connection.commit()

    #close the cursor and release the server connection 
    shopping_trolley_db.close()
    connection.close()


    #Make a GUI of order complete label
    save_order_completed()

    



#Print invoice label guideline, package, placement
print_invoice = Label(shop_window, text = "Ready to Print!",
                        font = ('Arial', 16, 'bold'), fg = 'Red')
print_invoice.pack()
print_invoice.config(background = "White")
print_invoice.place(x = 100, y = 435)


#Print invoice button, configuration, placement
print_invoice_button = Button(shop_window, text = "Print Invoice!", command = get_quantity_products)
print_invoice_button.config(width = 10, font = 1)
print_invoice_button.place(x = 400, y = 435)



################################################ Saving Order ################################


#Saving order label guideline, package, placement
save_order = Label(shop_window, text = "Step 3. Save your order.",
                        font = ('Arial', 16, 'bold'), fg = 'Dark Magenta')
save_order.pack()
save_order.config(background = "White")
save_order.place(x = 50, y = 490)


#Print invoice label guideline, package, placement
save_invoice = Label(shop_window, text = "Please Print Invoice...",
                        font = ('Arial', 16, 'bold'), fg = 'Red')
save_invoice.pack()
save_invoice.config(background = "White")
save_invoice.place(x = 100, y = 540)


def print_invoice_press_first():
    print_invoice.config(text='Please Wait Patiently...', fg = 'Red')
    print_invoice.place(x = 20, y = 435)
    shop_window.update()

def print_invoice_press_one():
    print_invoice.config(text='Downloading Anti-Theft Products..', fg = 'Red')
    print_invoice.place(x = 20, y = 435)
    shop_window.update()

def print_invoice_press_two():
    print_invoice.config(text="Downloading Women's Dresses..", fg = 'Red')
    shop_window.update()

def print_invoice_press_three():
    print_invoice.config(text='Downloading Indian Handicrafts..', fg = 'Red')
    shop_window.update()

def print_invoice_finished():
    print_invoice.config(text='Invoice Printed!', fg = 'Dark Green')
    print_invoice.place(x = 125, y = 435)
    shop_window.update()

def save_order_ready():
    save_invoice.config(text='Ready to Save!', fg = 'Red')
    save_invoice.place(x = 125, y = 540)
    save_order_button.config(state = 'normal')
    shop_window.update()


def save_order_happening():
    save_invoice.config(text='Saving Order...', fg = 'Red')
    shop_window.update()

def save_order_completed():
    save_invoice.config(text='Order Saved!', fg = 'Dark Green')
    shop_window.update()


#Saving order button, configuration, placement
save_order_button = Button(shop_window, text = "Save Order!", state=DISABLED, command = save_order_into_sqlite)
save_order_button.config(width = 10, font = 1)
save_order_button.place(x = 400, y = 540)


#Start the event loop.
shop_window.mainloop()


#################################### End of Tkinter ###########################################################






