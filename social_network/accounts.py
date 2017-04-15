
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.following = []
        self.posts = []
    
    def add_post(self, post):
        post.set_user(self)
        self.posts.append(post)
    
    def get_timeline(self):
        timeline = [post for user in self.following for post in user.posts]
        return sorted(timeline, key=lambda post: post.timestam)
        
# {THINK OF AN EASIER WAY TO RECOMEND FOR ITP STUDENTS
# {THINK OF AN EASIER WAY TO RECOMEND FOR ITP STUDENTS
    """
    def get_timeline(self):
        timeline = []
        for user in self.following:
            timeline += user.posts
        return timeline
or
    def get_timeline(self):
        timeline = []
        for user in self.following:
            for post in user.posts:
                timeline.append(post)  # This one is pretty much the same thing but a nested loop since were appending and we don't want to append the list of each users post, just the individual posts themselves.
        return timeline                 # When you use += we're basically just combining the two lists, so in the first example you'd have a list of posts, and you += it to timeline and they merge together. Newer at the end.
    """
    def follow(self, other):
        self.following.append(other)
