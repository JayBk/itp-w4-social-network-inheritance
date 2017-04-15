from datetime import datetime


class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = datetime.now() if timestamp is None else timestamp
        self.user = None
    
    def set_user(self, user):
        self.user = user


class TextPost(Post):
    def __init__(self, text, timestamp=None):
        super(TextPost, self).__init__(text, timestamp)

    def __str__(self):
        return '@{1} {2}: "{3}"\n\t{0:%A}, {0:%b} {0:%d}, {0:%Y}'.format(
            self.timestamp, self.user.first_name, 
            self.user.last_name, self.text)


class PicturePost(Post):
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost, self).__init__(text, timestamp)
        self.image_url = image_url
    
    def __str__(self):
        return '@{1} {2}: "{3}"\n\t{4}\n\t{0:%A}, {0:%b} {0:%d}, {0:%Y}'.format(
            self.timestamp, self.user.first_name, self.user.last_name, 
            self.text, self.image_url)
        

class CheckInPost(Post):
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost, self).__init__(text, timestamp)
        self.latitude, self.longitude = latitude, longitude

    def __str__(self):
        return '@{1} Checked In: "{3}"\n\t{4}, {5}\n\t{0:%A}, {0:%b} {0:%d}, \
{0:%Y}'.format(self.timestamp, self.user.first_name, 
        self.user.last_name, self.text,self.latitude, self.longitude)

"""
__str__ can also be done something like this as done in the projects solution branch:
def __str__(self):
    return '@{first_name} {last_name}: "{text}"\n\t{date}'.format(
        first_name=self.user.first_name,
        last_name=self.user.last_name,
        text=self.text,
        date=self.timestamp.strftime("%A, %b %d, %Y)
"""