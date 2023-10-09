import tkinter as tk
from tkinter import ttk
import os

SELECTED_OPP = None
PAST_SELECTED_OPP = None
QUERY = None

def make_connection():
    os.system("mysql -u newone -p < \"/home/kali/Desktop/projects/mysql.sql\"")

def select(what, table, *args):
    if args:
        os.system(f"mysql -u newone my_little_database -e \"select {what} from {table}\"") 
        #os.system(f"echo -ne '\n'") 
    else:
        os.system(f"mysql -u newone my_little_database -e \"select {what} from {table} {args[0]}\"")

def update(table, what):
    os.system(f"mysql -u newone my_little_database -e \"update {table} set {what}\"") 

def delete(table, *args):
    if args:
        os.system(f"mysql -u newone my_little_database -e \"delete from {table} {args[0]}\"") 
    else:
        os.system(f"mysql -u newone my_little_database -e \"delete from {table}") 

def drop(subject,target):
    os.system(f"mysql -u newone my_little_database -e \"drop {subject} if exists {target}") 

def alter_table(table, modch, what):
    os.system(f"mysql -u newone my_little_database -e \"alter table {table} {modch} {what}") 

def insert(table, *targers ,**values):
    v = str(targers)[2:-3].replace("'","")
    #print(v)
    #print(f"mysql -u newone my_little_database -e \"insert into {table}({v}) values({str(values.values())[13:-2]});\"")
    os.system(f"mysql -u newone my_little_database -e \"insert into {table}({v}) values({str(values.values())[13:-2]});\"") 
    
def show_tables():
    os.system(f"mysql -u newone my_little_database -e \"show tables from my_little_database;\"") 
      
def show_columns(table):
    os.system(f"mysql -u newone my_little_database -e \"show columns from {table};\"") 

def on_button_click(dropdown_og,root,canvas,prin):
    global PAST_SELECTED_OPP, QUERY 
    
    SELECTED_OPP = dropdown_og.get()
    if len(SELECTED_OPP) <= 0:
        SELECTED_OPP = PAST_SELECTED_OPP
    else:
        PAST_SELECTED_OPP = SELECTED_OPP 

    print(SELECTED_OPP)

    c = tk.Canvas(dropdown_og,width=350,height=250,background="white")
         
    if SELECTED_OPP == "delete from":
        c.pack()
        
        one_label = tk.Label(root, text = "table name                                                                  ",background="white")
        one_label.place(x = 70, y = 185)
        one_entry = tk.Entry(root,text = "select",background="white") 
        one_entry.place(x = 70, y = 160) 

        two_label = tk.Label(root, text = "where condition                                                                    ",background="white")
        two_label.place(x = 70, y = 225)
        two_entry = tk.Entry(root,text = "select1") 
        two_entry.place(x = 70, y = 205) 

        QUERY = SELECTED_OPP + " " + one_entry.get() + " where " + two_entry.get() + ";"
        
        
    if SELECTED_OPP == "select":
        
        one_label = tk.Label(root, text = "item name (for eg: * meaning all)                                                            ",background="white")
        one_label.place(x = 70, y = 185)
        one_entry = tk.Entry(root,text = "select2") 
        one_entry.place(x = 70, y = 160) 

        two_label = tk.Label(root, text = "table name                                                                    ",background="white")
        two_label.place(x = 70, y = 225)
        two_entry = tk.Entry(root,text = "select3") 
        two_entry.place(x = 70, y = 205) 

        three_label = tk.Label(root, text = "conditions (for eg: where id = 5 limit 10)",background="white")
        three_label.place(x = 70, y = 265)
        three_entry = tk.Entry(root,text = "select4") 
        three_entry.place(x = 70, y = 245) 

        QUERY = SELECTED_OPP + " " + one_entry.get() + " from " + two_entry.get() + " " + three_entry.get() + ";"

    if SELECTED_OPP == "insert into":

        one_label = tk.Label(root, text = "table name                                           ",background="white")
        one_label.place(x = 70, y = 185)
        one_entry = tk.Entry(root,text = "select5") 
        one_entry.place(x = 70, y = 160) 

        two_label = tk.Label(root, text =  "column names                                          ",background="white")
        two_label.place(x = 70, y = 225)
        two_entry = tk.Entry(root,text = "select6") 
        two_entry.place(x = 70, y = 205) 

        three_label = tk.Label(root, text = "values                                                           ",background="white")
        three_label.place(x = 70, y = 265)
        three_entry = tk.Entry(root,text = "select7") 
        three_entry.place(x = 70, y = 245) 

        QUERY = SELECTED_OPP + " " + one_entry.get() + "(" + two_entry.get() + ") values(" + three_entry.get() + ");"


    if SELECTED_OPP == "drop":

        c.pack()

        one_label = tk.Label(root, text = "table, view or user                                           ",background="white")
        one_label.place(x = 70, y = 185)
        one_entry = tk.Entry(root,text = "select8") 
        one_entry.place(x = 70, y = 160) 

        two_label = tk.Label(root, text =  "item, users' names                                          ",background="white")
        two_label.place(x = 70, y = 225)
        two_entry = tk.Entry(root,text = "select9") 
        two_entry.place(x = 70, y = 205) 

        QUERY = SELECTED_OPP + " " + one_entry.get() + " " + two_entry.get() + ";"



    if SELECTED_OPP == "alter":   

        c.pack()
        
        one_label = tk.Label(root, text = "table, view or user                                           ",background="white")
        one_label.place(x = 70, y = 185)
        one_entry = tk.Entry(root,text = "select10") 
        one_entry.place(x = 70, y = 160) 

        two_label = tk.Label(root, text =  "modify or change ...                                         ",background="white")
        two_label.place(x = 70, y = 225)
        two_entry = tk.Entry(root,text = "select11") 
        two_entry.place(x = 70, y = 205) 

        QUERY = SELECTED_OPP + one_entry.get() + " " + two_entry.get() + ";"



    if SELECTED_OPP == "show columns": 
 
        c.pack()
        one_label = tk.Label(root, text = "table name                                                   ",background="white")
        one_label.place(x = 70, y = 185)
        one_entry = tk.Entry(root,text = "select12") 
        one_entry.place(x = 70, y = 160) 
        QUERY = SELECTED_OPP + " from " + one_entry.get()
        

    if SELECTED_OPP == "show tables": 
        
        c.pack() 
        QUERY = "show tables;"
           
    

    button1 = tk.Button(root, text="send query",command=sql_handle)
    button1.place(x=270, y=330)

    button2 = tk.Button(root, text="check query", command = lambda: on_button_click(dropdown,root,canvas,1))
    button2.place(x=110, y=330)

    options = ["select", "insert into","delete from","drop", "alter","show columns", "show tables"]
    choice = tk.StringVar()
     
    dropdown = ttk.Combobox(root, textvariable=choice, values=options)
    dropdown.place(x = 70, y = 110)
    dropdown.set(f"{PAST_SELECTED_OPP}")

    qbutton = tk.Button(root,text="confirm statement", command = lambda: on_button_click(dropdown,root,canvas,0))
    qbutton.place(x = 270, y = 105)

    
    
    if prin == 1:

        print(QUERY)
        length_check = len(QUERY)/40
        why = 370
        queries = []

        tk.Label(root,text=f"                                                                                                                  ",background="white").place(x=50,y=why)            
        tk.Label(root,text=f"                                                                                                                  ",background="white").place(x=50,y=why+20)            
        tk.Label(root,text=f"                                                                                                                  ",background="white").place(x=50,y=why+40)    
        tk.Label(root,text=f"                                                                                                                  ",background="white").place(x=50,y=why+60)    
        tk.Label(root,text=f"                                                                                                                  ",background="white").place(x=50,y=why+80)    
        tk.Label(root,text=f"                                                                                                                  ",background="white").place(x=50,y=why+100)    


        if length_check > 1:
            catch = ""
            test_query = QUERY

            for i,char in enumerate(test_query):
                catch += char
                if len(catch) >= 50 or i == len(test_query)-1:
                    queries.append(catch) 
                    catch = ""
                    
            print(queries)
            
            
            for ind,i in enumerate(queries):
                why += 20
                if ind == 0:
                    tk.Label(root,text=f"Query is: {i}",background="white").place(x=50,y=why)
                else:
                    tk.Label(root,text=f"{i}",background="white").place(x=50,y=why)

        else:
            tk.Label(root,text=f"Query is: {QUERY}",background="white").place(x=50,y=370)


def sql_handle():
    print("handled", "query is: ", QUERY)
    os.system(f"mysql -u newone my_little_database -e \"{QUERY}\"")        
   
   
    
def application():  
    root = tk.Tk()
    root.geometry("500x500")

    canvas = tk.Canvas(root,width=500,height=500,background="white")
    canvas.pack()
    
    button = tk.Button(root, text="send query",command=sql_handle)
    button.place(x=270, y=330)

    button = tk.Button(root, text="check query",command= lambda: on_button_click(dropdown,root,canvas,1))
    button.place(x=110, y=330)

    options = ["select", "insert into","delete from","drop", "alter","show columns", "show tables"]
    choice = tk.StringVar()
     
    dropdown = ttk.Combobox(root, textvariable=choice, values=options)
    dropdown.place(x = 70, y = 110)
    dropdown.set("select statement")

    qbutton = tk.Button(root,text="confirm statement", command = lambda: on_button_click(dropdown,root,canvas,0))
    qbutton.place(x = 270, y = 105)
    root.mainloop()  


application()
