name = "Max"
#variabeln
#Unerlaubt: keywörter, mit:%,/,...

name = " Max"; print(name)
#mit semikolon mehrere aussagen in einer linie

#Kommentararten: mit `#` oder mit """ """ über mehrere Zeilen

#Datentypen: mit == vergleich, mit isisntance kann man Datentyp herrausfinden
#Datentypen, welche gibt es??

number = "20"
age = int(number)
#Casten von Datentypen:


#Opperatoren: =, +, -, *, /, %, ** (Quadrat), // (Flordivision, abrunden auf Int)
#Weitere z.B.: "+=" -> check check
#Vergelch: ==, !=, <, <=, ...

#Boolen opperatoren: not var -> umdrehen, var and var, var or var
# and, or -> Bit

#kann auch in retrun schreiben
#return True if age>18 else False

string_1= "HELLO"
string_2 = "WORLD!"
string_3 = string_1 + " " + string_2
print(string_3)

print(""" 
      
Das ist ein Print über mehrere
Zeilen

      """)

#ansonsten viele String methoden intuitiv, geben zurück
name = "Beau"
print(name.lower())
print("au" in name)

#um " in string schreiben: \" nächster buchstage ist nicht was er normalerweiße bedeutet
#\n zeilensprung oder ander Format sachen
#Strings können mit [] geöffnet werden name[0:4],...

done = True
done = False
#Großschreiben
#1:22:41

print("Is done?",end = " ")
if done:
    print("Yes")
else:
    print("Flase")

print(isinstance(done,bool))


number1 = 2 + 3j
number2 = complex(2,3)

print(number1.real, number2.imag)

#Zahlen in C


print(abs(-5.5))
print(round(5.3))
print(round(5.49,1)) #Runden ab stelle 1 hinter komma/punkt
#Built in funktions

print("")

from enum import Enum

class State(Enum):
      INACTIVE = 0
      ACTIVE = 1

print(State.ACTIVE.value)
#To Create a constant variable
print(State['ACTIVE'].value)
print(State.ACTIVE)