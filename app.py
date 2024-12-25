from flask import Flask, render_template 

app=Flask(__name__)

#creating a url and a function to bound to it 
@app.route("/home")
def home():
      return render_template("home.html")

@app.route("/About")
def about_us():
    return "welcome to the About us page"


#clients details 
@app.route("/form/<name>")
def form_details(name):
    return "The name of the client is: %s" % name

    


#we are running the file directly so, the below condition is valid
if __name__=="__main__":
    app.run(debug=True)

