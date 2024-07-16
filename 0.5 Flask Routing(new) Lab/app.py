#border 1
from flask import Flask
app = Flask(__name__)


#main entarence
@app.route('/home')
def home():
    return ("<html><h1>THE PHOTO GALLERY<h1><h3>hi!! welcome to THE photo gallery! in here, you can explore 3 types of photos that are: animals, food and outdoor spaces!</h3> <a href=\'food1\'>go to the first food photo </a><a href=\'animal2\'>go to the second animal photo</a><a href =\'outdoorspace1\'>go to the first outdoorspace photo</a></html> ")
#food 1
@app.route('/food1')
def food1():
    #output return, and image+hyperlinks
    return '''
    <html>
    <img src = https://i.pinimg.com/564x/57/b9/4d/57b94d30b9583e7fecccf10d4cae214f.jpg>
    <a href= "home">HOME</a>
    <a href= "/food2">!NEXT PHOTO!</a>
    </html>

    '''
#food2
@app.route('/food2')
def food2():
    return '''
    <html>
    <img src = https://i.pinimg.com/564x/d3/3a/57/d33a57d806b903a98b86bef6e377554e.jpg>
    <a href = "/food3">!LAST PHOTO!</a>
    </html>
    '''
#food3 
@app.route('/food3')
def food3():
    return '''
    <html>
    <img src = https://i.pinimg.com/736x/33/c8/92/33c892619fff761bb7e2fb9513e53765.jpg>
    <a href = "/home">HOME</a>
    '''

#animal2
@app.route('/animal2')
def animal2():
    return '''
    <html>
    <img src = https://i.pinimg.com/564x/b6/2a/6c/b62a6cd76abc74602ef54c1697c740f1.jpg>
    <a href = "/home">HOME</a>
    <a href = "/animal1">FIRST ANIMAL</a>
    <a href = "/animal3">LAST ANIMAL</a>
    </html>
    '''
#animal3 
@app.route('/animal3')
def animal3():
    return '''
    <html>
    <img src = https://i.pinimg.com/736x/33/b5/75/33b575588330127834be8354eb530508.jpg>
    <a href = "/animal2">SECOND ANIMAL</a>
    </html>
    '''

    #animal1
@app.route('/animal1')
def animal1():
    return '''
    <html>
    <img src =https://i.pinimg.com/564x/a8/4d/74/a84d74a1f536936a94792355c64eb2c3.jpg>
    <a href = "/animal2">SECOND ANIMAL</a>
    </html>
    '''

#outdoorspace1
@app.route('/outdoorspace1')
def outdoorspace1():
    return'''
    <html>
    <img src = https://i.pinimg.com/564x/3f/00/49/3f00496448b44d9ffebedec1c8abbc15.jpg>
    <a href = "/home">HOME</a>
    <a href = "/outdoorspace2">NEXT OUTDOOR SPACE</a>
    <a href = "/outdoorspace3">LAST OUTDOOR SPACE</a>
    </html>
    '''

#outdoorspace2 
@app.route('/outdoorspace2')
def outdoorspace2():
    return '''
    <html>
    <img src = https://i.pinimg.com/564x/79/38/a3/7938a393a5c251d96844c0542dacbe5b.jpg>
    <a href = "/outdoorspaces1">FIRST OUTDOOR SPACE</a>
    <a href = "/outdoorspaces3">NEXT OUTDOOR SPACE</a>
    </html>
    '''
#outdoorspace3
@app.route('/outdoorspace3')
def outdoorspace3():
    return '''
    <html>
    <img src = https://i.pinimg.com/564x/bc/1f/a8/bc1fa801b805d37365ad1f36d4338c35.jpg>
    <a href = "/outdoorspace1">FIRST OUTDOOR SPACE</a>
    <a href = "/outdoorspace2">SECOND OUTDOOR SPACE</a>
    <html>
    '''
#border 2
if __name__ == '__main__':
    app.run(debug=True)




