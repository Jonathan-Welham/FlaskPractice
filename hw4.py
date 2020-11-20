import numpy as np
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)

image_info = [
    { "id" : "34694102243_3370955cf9_z",
      "title" : "Eastern",
      "flickr_user" : "Sean Davis",
      "tags" : ["Los Angeles", "California", "building"]
    },
    { "id" : "37198655640_b64940bd52_z",
      "title" : "Spreetunnel",
      "flickr_user" : "Jens-Olaf Walter",
      "tags" : ["Berlin", "Germany", "tunnel", "ceiling"]
    },
    { "id" : "36909037971_884bd535b1_z",
      "title" : "East Side Gallery",
      "flickr_user" : "Pieter van der Velden",
      "tags" : ["Berlin", "wall", "mosaic", "sky", "clouds"]
    },
    { "id" : "36604481574_c9f5817172_z",
      "title" : "Lombardia," " september 2017",
      "flickr_user" : "Mónica Pinheiro",
      "tags" : ["Italy", "Lombardia", "alley", "building", "wall"]
    },
    { "id" : "36885467710_124f3d1e5d_z",
      "title" : "Palazzo Madama",
      "flickr_user" : "Kevin Kimtis",
      "tags" : [ "Rome", "Italy", "window", "road", "building"]
    },
    { "id" : "37246779151_f26641d17f_z",
      "title" : "Rijksmuseum library",
      "flickr_user" : "John Keogh",
      "tags" : ["Amsterdam", "Netherlands", "book", "library", "museum"]
    },
    { "id" : "36523127054_763afc5ed0_z",
      "title" : "Canoeing in Amsterdam",
      "flickr_user" : "bdodane",
      "tags" : ["Amsterdam", "Netherlands", "canal", "boat"]
    },
    { "id" : "35889114281_85553fed76_z",
      "title" : "Quiet at dawn, Cabo San Lucas",
      "flickr_user" : "Erin Johnson",
      "tags" : ["Mexico", "Cabo", "beach", "cactus", "sunrise"]
    },
    { "id" : "34944112220_de5c2684e7_z",
      "title" : "View from our rental",
      "flickr_user" : "Doug Finney",
      "tags" : ["Mexico", "ocean", "beach", "palm"]
    },
    { "id" : "36140096743_df8ef41874_z",
      "title" : "Someday",
      "flickr_user" : "Thomas Hawk",
      "tags" : ["Los Angeles", "Hollywood", "California", "car"]
    }
]

@app.route('/')
def hello_world():
    r1 = image_info[np.random.randint(0,10)]["id"]
    r2 = image_info[np.random.randint(0,10)]["id"]
    r3 = image_info[np.random.randint(0,10)]["id"]
    return render_template("home.html", r1=r1, r2=r2, r3=r3)

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/page3')
def page3():
    return render_template('page3.html')

@app.route('/page4')
def page4():
    return render_template('page4.html')

if __name__ == '__main__':
    app.run()