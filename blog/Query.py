from blog.Model import Post, Comment


class Query(object):

    def __init__(self, session):
        self.session = session

    def load_post_with_comments_by_id(self, id):
        """
        Load a single post by ID with all comments.

        :param id: the post ID.
        :return: the post, or None if not found.
        """
        post = None
        posts = self.session.query(Post).filter(Post.id == id).all()
        if len(posts) > 0:
            post = posts[0]
            comments = self.session.query(Comment).filter(Comment.post_id == id).all()
            post.comments = comments
        return post

    def load_post_with_comments_by_permalink(self, permalink):
        """
        Load a single post by permalink with all comments.

        :param permalink: the post permalink.
        :return: the post, or None if not found.
        """
        post = None
        posts = self.session.query(Post).filter(Post.permalink == permalink).all()
        if len(posts) > 0:
            post = posts[0]
            comments = self.session.query(Comment).filter(Comment.post_id == post.id).all()
            post.comments = comments
        return post

