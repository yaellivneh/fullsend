import cgi
form = cgi.FieldStorage()
searchterm = form.getvalue('answerone')

While True:
x = input('answerone')
if x != "egg"
    print("That is incorrect")
    continue
else
    break

print("That is correct")
