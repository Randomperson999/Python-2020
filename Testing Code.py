###Caleb Keller
###9/23/2020
##Test1----------------------------------------------------------------------------------------------------------------------------
#value1 = "henlo"
#value2 = "place"
#example = str.format("fOr{1}MaTeD sTr{0}InG",value1,value2)
#print(example)
##---------------------------------------------------------------------------------------------------------------------------------
##Test2
string1 = "Wow "
string2 = "You "
string3 = "E X I S T"
test = str.format("""completely
pointless
text
is a
waste
of your time.
{0:1}{1:2.2}{0:1.1}""", string1,string2,string3)
print(test)
