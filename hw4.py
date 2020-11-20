import numpy as np
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from PIL import Image

image_info = [
    {"id": "34694102243_3370955cf9_z",
     "title": "Eastern",
     "flickr_user": "Sean Davis",
     "tags": ["Los Angeles", "California", "building"]
     },
    {"id": "37198655640_b64940bd52_z",
     "title": "Spreetunnel",
     "flickr_user": "Jens-Olaf Walter",
     "tags": ["Berlin", "Germany", "tunnel", "ceiling"]
     },
    {"id": "36909037971_884bd535b1_z",
     "title": "East Side Gallery",
     "flickr_user": "Pieter van der Velden",
     "tags": ["Berlin", "wall", "mosaic", "sky", "clouds"]
     },
    {"id": "36604481574_c9f5817172_z",
     "title": "Lombardia," " september 2017",
     "flickr_user": "Mónica Pinheiro",
     "tags": ["Italy", "Lombardia", "alley", "building", "wall"]
     },
    {"id": "36885467710_124f3d1e5d_z",
     "title": "Palazzo Madama",
     "flickr_user": "Kevin Kimtis",
     "tags": ["Rome", "Italy", "window", "road", "building"]
     },
    {"id": "37246779151_f26641d17f_z",
     "title": "Rijksmuseum library",
     "flickr_user": "John Keogh",
     "tags": ["Amsterdam", "Netherlands", "book", "library", "museum"]
     },
    {"id": "36523127054_763afc5ed0_z",
     "title": "Canoeing in Amsterdam",
     "flickr_user": "bdodane",
     "tags": ["Amsterdam", "Netherlands", "canal", "boat"]
     },
    {"id": "35889114281_85553fed76_z",
     "title": "Quiet at dawn, Cabo San Lucas",
     "flickr_user": "Erin Johnson",
     "tags": ["Mexico", "Cabo", "beach", "cactus", "sunrise"]
     },
    {"id": "34944112220_de5c2684e7_z",
     "title": "View from our rental",
     "flickr_user": "Doug Finney",
     "tags": ["Mexico", "ocean", "beach", "palm"]
     },
    {"id": "36140096743_df8ef41874_z",
     "title": "Someday",
     "flickr_user": "Thomas Hawk",
     "tags": ["Los Angeles", "Hollywood", "California", "car"]
     }
]
class pic:

    def __init__(self, pos, id, title, flickU, tags):
        self.pos = pos
        self.id = image_info[pos]["id"]
        self.title = image_info[pos]["title"]
        self.flickU = image_info[pos]["flickr_user"]
        self.tags = image_info[pos]["tags"]

    def setAll(self, pos):
        self.pos = pos
        self.id = image_info[pos]["id"]
        self.title = image_info[pos]["title"]
        self.flickU = image_info[pos]["flickr_user"]
        self.tags = image_info[pos]["tags"]
        self.image = Image.open(f"static/images/{self.id}.jpg")
        self.width, self.height = self.image.size

    def getRand(self, pos):
        self.pos = np.random.rand(0,10)
        return self.pos

    def getId(self):
        return self.id

    def getTitle(self):
        return self.title

    def getflickU(self):
        return self.flickU

    def getTags(self):
        return self.tags

    def getImage(self):
        return self.image

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height


app = Flask(__name__)
bootstrap = Bootstrap(app)
img1 = pic(0, 0, 0, 0, 0)
img2 = pic(0, 0, 0, 0, 0)
img3 = pic(0, 0, 0, 0, 0)

@app.route('/')
def home():

    rand1 = np.random.randint(0, 10)
    rand2 = np.random.randint(0, 10)
    rand3 = np.random.randint(0, 10)

    img1.setAll(rand1)
    img2.setAll(rand2)
    img3.setAll(rand3)

    return render_template("home.html", r1=img1.getId(), r2=img2.getId(), r3=img3.getId())

@app.route('/page2')
def page2():
    return render_template('page2.html', title=img1.getTitle(), image=img1.getId(), width=img1.getWidth(), height=img1.getHeight())

@app.route('/page3')
def page3():
    return render_template('page2.html', title=img2.getTitle(), image=img2.getId(), width=img2.getWidth(),
                           height=img2.getHeight())

@app.route('/page4')
def page4():
    return render_template('page2.html', title=img3.getTitle(), image=img3.getId(), width=img3.getWidth(),
                           height=img3.getHeight())

if __name__ == '__main__':
    app.run()
