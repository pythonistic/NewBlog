from blog.Model import Post, PostSynopsis, Comment, Category, Approval


class Query(object):

    def __init__(self, session):
        self.session = session

    def load_post_by_id(self, id):
        """
        Load a single post by ID without comments.

        :param id:
        :return: the post, or None if not found.
        """
        post = None
        posts = self.session.query(Post).filter(Post.id == id).all()
        if len(posts) > 0:
            post = posts[0]
        return post

    def load_post_by_permalink(self, permalink):
        """
        Load a single post by permalink without comments.

        :param permalink:
        :return: the post, or None if not found.
        """
        post = None
        posts = self.session.query(Post).filter(Post.permalink == permalink).all()
        if len(posts) > 0:
            post = posts[0]
        return post

    def load_comments_by_post_id(self, id):
        """
        Load all the comments for a post by post ID.

        :param id: the post ID.
        :return: the comments or an empty list of no comments.
        """
        comments = self.session.query(Comment).filter(Comment.post_id == id).all()
        return comments

    def load_post_with_comments_by_id(self, id):
        """
        Load a single post by ID with all comments.

        :param id: the post ID.
        :return: the post, or None if not found.
        """
        post = self.load_post_by_id(id)
        if post:
            post.comments = self.load_comments_by_post_id(id)
        return post

    def load_post_with_comments_by_permalink(self, permalink):
        """
        Load a single post by permalink with all comments.

        :param permalink: the post permalink.
        :return: the post, or None if not found.
        """
        post = self.load_post_by_permalink(permalink)
        if post:
            comments = self.load_comments_by_post_id(post.id)
            post.comments = comments
        return post

    def load_post_synopsis_by_id(self, id):
        """
        Load a single post synopsis by ID.

        :param id: the post ID.
        :return: the PostSynopsis, or None if not found.
        """
        post_synopsis = None
        posts = self.session.query(PostSynopsis).filter(PostSynopsis.id == id).all()
        if len(posts) > 0:
            post_synopsis = posts[0]
        return post_synopsis

    def get_post_id_for_permalink(self, permalink):
        """
        Get the post ID for the given permalink.

        :param permalink:
        :return: the post ID or None if not found.
        """
        post_id = None
        post_synopses = self.session.query(PostSynopsis).filter(PostSynopsis.permalink == permalink).all()
        if len(post_synopses) > 0:
            post_id = post_synopses[0].id
        return post_id

    def get_categories_with_posts(self):
        """
        Get the visible categories with active posts.

        :return: the list of active categories with posts, or an empty list if none.
        """
        categories = self.session.query(Category).join(PostSynopsis).join(Approval)\
            .filter(Category.visible == True)\
            .filter(Approval.status == 'approved')\
            .all()
        return categories

    def load_post_synopsis_for_approval(self):
        """
        Get synopses for the posts in pending status.

        :return: the list of post summaries in pending status.
        """
        synopsis = self.session.query(PostSynopsis).join(Approval)\
            .filter(Approval.status == 'pending')\
            .all()
        return synopsis