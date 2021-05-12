import cgi
form = cgi.FieldStorage()
answerone = form.getvalue('answerone')

if answerone not in ("egg", "Egg", "EGG"):
        print("Content-type: text/html\n")
        print("<html>")
        print("<body>")
        print("<h1>HelloWorld")
        print("</body>")
        print("</html>")
else:
        print("Correct")
break


#while True:
   # data = input("Please enter your answer for Etgar 1")
   # if data not in ("egg", "Egg", "EGG"):
      #  print("Incorrect")
  #  else:
      #  print("Correct")
  #  break
