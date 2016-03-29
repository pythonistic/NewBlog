from blog.Model import Post, PostStatus, PostSynopsis, PostType
from blog.Model import Comment, CommentStatus, Category
from blog.Model import Approval, Author, AuthorStatus
from blog.Model import TrackbackStatus


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

    def get_categories(self):
        """
        Get the list of all categories.

        :return: the list of all categories.
        """
        categories = self.session.query(Category).all()
        return categories

    def get_categories_with_posts(self):
        """
        Get the visible categories with active posts.

        :return: the list of active categories with posts, or an empty list if none.
        """
        categories = self.session.query(Category).join(PostSynopsis).join(Approval) \
            .filter(Category.visible == True) \
            .filter(Approval.status == 'approved') \
            .all()
        return categories

    def load_post_synopsis_for_approval(self):
        """
        Get synopses for the posts in pending status.

        :return: the list of post summaries in pending status.
        """
        synopsis = self.session.query(PostSynopsis).join(Approval) \
            .filter(Approval.status == 'pending') \
            .all()
        return synopsis

    def load_comments_for_approval(self):
        """
        Load comments pending approval.

        :return: the list of comments pending approval.
        """
        comments = self.session.query(Comment).join(Approval) \
            .filter(Approval.status == 'pending') \
            .all()
        return comments

    def load_comment_by_id(self, id):
        """
        Load a comment and its children.

        :param id: the comment ID.
        :return: the comment and its children or None if not found.
        """
        comment = None
        comments = self.session.query(Comment).filter(Comment.id == id).all()
        if len(comments) > 0:
            comment = comments[0]
        return comment

    def get_comment_statuses(self):
        """
        Get the list of all comment statuses.

        :return: the comment statuses.
        """
        comment_statuses = self.session.query(CommentStatus).all()
        return comment_statuses

    def load_authors(self):
        """
        Load all the active authors.

        :return: the list of active authors or [] if none.
        """
        authors = self.session.query(Author).join(AuthorStatus) \
            .filter(Author.status_id == AuthorStatus.id) \
            .filter(AuthorStatus.status == 'active') \
            .all()
        return authors

    def load_pending_authors(self):
        """
        Load the authors pending approval.

        :return: the list of pending authors or [] if none.
        """
        authors = self.session.query(Author).join(AuthorStatus) \
            .filter(Author.status_id == AuthorStatus.id) \
            .filter(AuthorStatus.status == 'pending') \
            .all()
        return authors

    def load_approval_statuses(self):
        """
        Load the list of approval statuses.

        :return: the list of approval statuses.
        """
        approval_statuses = self.session.query(Approval).all()
        return approval_statuses

    def load_author_statuses(self):
        """
        Load the list of author statuses.

        :return: the list of author statuses.
        """
        author_statuses = self.session.query(AuthorStatus).all()
        return author_statuses

    def load_comments_by_approval_status_id(self, id):
        """
        Load the list of comments by status ID, such as to identify comments
        that need to be approved.

        :param id: the approval status ID.
        :return: the list of comments matching that status ID.
        """
        comments = self.session.query(Comment).filter(Comment.approval_id == id).all()
        return comments

    def load_posts_by_approval_status_id(self, id):
        """
        Load the list of posts by approval status ID.

        :param id: the approval status ID.
        :return: the list of poss matching the status ID.
        """
        posts = self.session.query(Post).filter(Post.approval_id == id).all()
        return posts

    def get_post_statuses(self):
        """
        Load the list of post statuses.

        :return: the list of PostStatus.
        """
        statuses = self.session.query(PostStatus).all()
        return statuses

    def get_post_types(self):
        """
        Load the list of post types.

        :return: the list of PostType.
        """
        types = self.session.query(PostType).all()
        return types

    def load_posts_by_type_id(self, id):
        """
        Load the posts by type ID.

        :return: the list of Post by PostType.id.
        """
        posts = self.session.query(Post).filter(Post.post_type_id == id).all()
        return posts

    def get_trackback_statuses(self):
        """
        Load the list of trackback statuses.

        :return the list of TrackBackStatus.
        """
        statuses = self.session.query(TrackbackStatus).all()
        return statuses