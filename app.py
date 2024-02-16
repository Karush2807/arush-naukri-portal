from flask import Flask

app=Flask(__name__) #its just app name

@app.route('/') #yhn hm decide krte hai, ki kiss url pr kya hoga
def helloworld():
  return "namste duniya"

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
