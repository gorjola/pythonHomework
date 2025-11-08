class User:
    def __init__(self, name):
        self.name = name
        self.friends_set = set()
        self.post_list = []

    def create_post(self, content):
        post = Post(content, self)
        self.post_list.append(post)
        return post

    def add_friend(self, user):
        self.friends_set.add(user)

    def post_comment(self, post, content):
        comment = Comment(content, self)
        post.add_comment(comment)
        return comment

    def like_post(self, item):
        if isinstance(item, (Post, Comment)):
            item.add_like(self)
            return item
        else:
            raise TypeError("Can like only Post or Comment")

    def __str__(self):
        friends_names = ", ".join(friend.name for friend in self.friends_set) or "no friends"
        return f"User('{self.name}', friends=[{friends_names}])"

    def __repr__(self):
        return f"User('{self.name}')"


class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.comment_list = []
        self.like_list = []

    def add_comment(self, comment):
        self.comment_list.append(comment)

    def add_like(self, user):
        if user not in self.like_list:
            self.like_list.append(user)

    def __str__(self):
        return f"Post('{self.content}', by {self.author.name}, {len(self.like_list)} likes, and {len(self.comment_list)} comments )"


class Comment:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.likes = []

    def add_like(self, user):
        if user not in self.likes:
            self.likes.append(user)

    def __str__(self):
        return f"Comment(by {self.author.name}: '{self.content}', {len(self.likes)} likes)"



user1 = User("ultramarine")
user2 = User("blood angel")

user1.add_friend(user2)

post1 = user1.create_post("what is your duty?")
comment1 = user2.post_comment(post1, "die for emperor")

user1.like_post(comment1)
user2.like_post(post1)

post2 = user1.create_post("for the emperor")
user2.like_post(post2)

print(user1.friends_set)
print(post1)
print(post2)
print(comment1)