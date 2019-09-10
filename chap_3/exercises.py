import datetime
# Exercises

# book, magazine

# computer, phone, keyboard, calculator

class Post:
    likes = 0 
    def __init__(self, user_id, text):
        self.user_id = user_id
        self.text = text

    def edit(self, text):
        self.text = text

    def like(self):
        self.likes += 1

    def comment(self, commentor_id, comment_text):
        self.commentor_id = commentor_id
        self.comment_text = comment_text

class Comment(Post):
    def __init__(self, user_id, text):
        super().__init__(user_id, text)


p = Post(3, 'hello there')
c = Comment(4, 'hello back')
