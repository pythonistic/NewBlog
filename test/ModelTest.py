import unittest

from blog import Session
from blog.Model import *


class ModelTest(unittest.TestCase):

    ID = -1

    def setUp(self):
        self.session = Session()

    def tearDown(self):
        self.session.close()

    def clean(self, clz, remove_id):
        """
        Remove the test record for the model class.

        :param clz:        The test record class.
        :param remove_id:  The id of the record to remove.
        """
        results = self.session.query(clz).filter(clz.id == remove_id).all()
        for result in results:
            self.session.delete(result)
        self.session.commit()

    def create_approval(self, new_id):
        self.clean(Approval, new_id)

        approval = Approval()
        approval.id = new_id
        approval.status = 'foo'
        approval.description = 'description'

        self.session.add(approval)
        self.session.commit()
        return approval

    def create_author_status(self, new_id):
        self.clean(AuthorStatus, new_id)

        status = AuthorStatus()
        status.id = new_id
        status.status = 'foo'
        status.description = 'description'
        self.session.add(status)
        self.session.commit()
        return status

    def create_author(self, new_id, status):
        self.clean(Author, new_id)

        author = Author()
        author.id = new_id
        author.login = 'foo'
        author.password = 'bar'
        author.email = 'baz'
        author.url = 'frobble'
        author.activation_key = 'activation'
        author.status = status
        author.display_name = 'name'
        self.session.add(author)
        self.session.commit()
        return author

    def create_category(self, new_id):
        self.clean(Category, new_id)

        category = Category()
        category.id = new_id
        category.name = 'foo'
        category.description = 'description'
        category.visible = True
        self.session.add(category)
        self.session.commit()
        return category

    def create_post(self, new_id, author=None, category=None, post_status=None,
                    approval=None, post_type=None, trackback_status=None, comment_status=None):
        self.clean(Post, new_id)

        post = Post()
        post.id = new_id
        post.author = author
        post.title = 'foo'
        post.excerpt = 'foo'
        post.trackback_excerpt = 'foo'
        post.content = 'foo'
        post.content_filtered = 'foo'
        post.category = category
        post.post_status = post_status
        post.approval = approval
        post.post_type = post_type
        post.mime_type = 'text/plain'
        post.trackback_status = trackback_status
        post.name = 'foo'
        post.comment_status = comment_status
        post.comment_count = 2
        self.session.add(post)
        self.session.commit()
        return post

    def create_comment(self, new_id, parent=None, post=None, author=None, approval=None):
        self.clean(Comment, new_id)

        comment = Comment()
        comment.id = new_id
        comment.parent = parent
        comment.post = post
        comment.author_name = 'foo'
        comment.author_email = 'bar@baz'
        comment.author_url = 'https://foo.bar.baz'
        comment.author_IP = '0001:0002:0003:0004'
        comment.author = author
        comment.content = 'foo'
        comment.approval = approval
        comment.agent = 'Mozilla'
        comment.type = 'bar'
        self.session.add(comment)
        self.session.commit()
        return comment

    def create_comment_status(self, new_id):
        self.clean(CommentStatus, new_id)

        comment_status = CommentStatus()
        comment_status.id = new_id
        comment_status.status = 'foo'
        comment_status.description = 'description'
        self.session.add(comment_status)
        self.session.commit()
        return comment_status

    def create_post_status(self, new_id):
        self.clean(PostStatus, new_id)

        post_status = PostStatus()
        post_status.id = new_id
        post_status.status = 'foo'
        post_status.description = 'description'
        self.session.add(post_status)
        self.session.commit()
        return post_status

    def create_post_type(self, new_id):
        self.clean(PostType, new_id)

        post_type = PostType()
        post_type.id = new_id
        post_type.type = 'foo'
        post_type.description = 'description'
        self.session.add(post_type)
        self.session.commit()
        return post_type

    def create_trackback_status(self, new_id):
        self.clean(TrackbackStatus, new_id)

        trackback_status = TrackbackStatus()
        trackback_status.id = new_id
        trackback_status.status = 'foo'
        trackback_status.description = 'description'
        self.session.add(trackback_status)
        self.session.commit()
        return trackback_status

    def test_approval(self):
        approval = self.create_approval(self.ID)
        loaded_approval = self.session.query(Approval).filter(Approval.id == self.ID).first()
        self.assertEqual(approval.id, loaded_approval.id)
        self.assertEqual(approval.status, loaded_approval.status)
        self.assertEqual(approval.description, loaded_approval.description)
        self.assertEqual(str(approval), str(loaded_approval))

        self.session.delete(loaded_approval)
        self.session.commit()

        self.clean(Approval, self.ID)

    def test_author(self):
        status = self.create_author_status(self.ID)
        author = self.create_author(self.ID, status)

        loaded_author = self.session.query(Author).filter(Author.id == self.ID).first()
        self.assertEqual(author.id, loaded_author.id)
        self.assertEqual(author.login, loaded_author.login)
        self.assertEqual(author.password, loaded_author.password)
        self.assertEqual(author.email, loaded_author.email)
        self.assertEqual(author.url, loaded_author.url)
        self.assertEqual(author.activation_key, loaded_author.activation_key)
        self.assertEqual(author.status, loaded_author.status)
        self.assertEqual(status, loaded_author.status)
        self.assertEqual(author.display_name, loaded_author.display_name)
        self.assertEqual(author.created, loaded_author.created)
        self.assertEqual(str(author), str(loaded_author))

        self.clean(Author, self.ID)
        self.clean(AuthorStatus, self.ID)

    def test_author_status(self):
        status = self.create_author_status(self.ID)

        loaded_status = self.session.query(AuthorStatus).filter(AuthorStatus.id == self.ID).first()
        self.assertEqual(status.id, loaded_status.id)
        self.assertEqual(status.status, loaded_status.status)
        self.assertEqual(status.description, loaded_status.description)
        self.assertEqual(str(status), str(loaded_status))

        self.clean(AuthorStatus, self.ID)

    def test_category(self):
        category = self.create_category(self.ID)

        loaded_category = self.session.query(Category).filter(Category.id == self.ID).first()
        self.assertEqual(category.id, loaded_category.id)
        self.assertEqual(category.name, loaded_category.name)
        self.assertEqual(category.description, loaded_category.description)
        self.assertEqual(category.visible, loaded_category.visible)

        self.clean(Category, self.ID)

    def test_comment(self):
        parent_id = self.ID - 1

        author_status = self.create_author_status(self.ID)
        parent_author = self.create_author(self.ID, author_status)
        parent_approval = self.create_approval(self.ID)
        category = self.create_category(self.ID)
        post_status = self.create_post_status(self.ID)
        post_type = self.create_post_type(self.ID)
        trackback_status = self.create_trackback_status(self.ID)
        comment_status = self.create_comment_status(self.ID)
        author = None
        approval = None
        post = self.create_post(self.ID, parent_author, category, post_status, parent_approval,
                                post_type, trackback_status, comment_status)
        parent_comment = self.create_comment(parent_id, post=post, author=parent_author, approval=parent_approval)
        comment = self.create_comment(self.ID, parent=parent_comment, post=post, author=author, approval=approval)
        comment.parent = parent_comment
        self.session.commit()

        approval_2 = self.session.query(Approval).filter(Approval.id == 2).first()

        loaded_comment = self.session.query(Comment).filter(Comment.id == self.ID).first()
        self.assertIsNotNone(loaded_comment)
        self.assertEqual(comment.approval, approval_2)
        self.assertEqual(comment, loaded_comment)
        self.assertEqual(parent_id, comment.parent.id)

        self.clean(Comment, parent_id)
        self.clean(Comment, self.ID)
        self.clean(Post, self.ID)
        self.clean(CommentStatus, self.ID)
        self.clean(TrackbackStatus, self.ID)
        self.clean(PostType, self.ID)
        self.clean(PostStatus, self.ID)
        self.clean(Category, self.ID)
        self.clean(Approval, self.ID)
        self.clean(Author, self.ID)
        self.clean(AuthorStatus, self.ID)

    def test_comment_status(self):
        comment_status = self.create_comment_status(self.ID)

        loaded_comment_status = self.session.query(CommentStatus).filter(CommentStatus.id == self.ID).first()
        self.assertIsNotNone(loaded_comment_status)
        self.assertEqual(str(loaded_comment_status), str(comment_status))
        self.clean(CommentStatus, self.ID)

    def test_post(self):
        author_status = self.create_author_status(self.ID)
        author = self.create_author(self.ID, author_status)
        approval = self.create_approval(self.ID)
        category = self.create_category(self.ID)
        post_status = self.create_post_status(self.ID)
        post_type = self.create_post_type(self.ID)
        trackback_status = self.create_trackback_status(self.ID)
        comment_status = self.create_comment_status(self.ID)
        post = self.create_post(self.ID, author, category, post_status, approval,
                                post_type, trackback_status, comment_status)

        loaded_post = self.session.query(Post).filter(Post.id == self.ID).first()
        self.assertIsNotNone(loaded_post)
        self.assertEqual(str(loaded_post), str(post))

        self.clean(Post, self.ID)
        self.clean(CommentStatus, self.ID)
        self.clean(TrackbackStatus, self.ID)
        self.clean(PostType, self.ID)
        self.clean(PostStatus, self.ID)
        self.clean(Category, self.ID)
        self.clean(Approval, self.ID)
        self.clean(Author, self.ID)
        self.clean(AuthorStatus, self.ID)

    def test_post_status(self):
        post_status = self.create_post_status(self.ID)

        loaded_post_status = self.session.query(PostStatus).filter(PostStatus.id == self.ID).first()
        self.assertIsNotNone(loaded_post_status)
        self.assertEqual(str(loaded_post_status), str(post_status))

        self.clean(PostStatus, self.ID)

    def test_post_type(self):
        post_type = self.create_post_type(self.ID)

        loaded_post_type = self.session.query(PostType).filter(PostType.id == self.ID).first()
        self.assertIsNotNone(loaded_post_type)
        self.assertEqual(str(post_type), str(loaded_post_type))

        self.clean(PostType, self.ID)

    def test_trackback_status(self):
        trackback_status = self.create_trackback_status(self.ID)

        loaded_trackback_status =self.session.query(TrackbackStatus).filter(TrackbackStatus.id == self.ID).first()
        self.assertIsNotNone(loaded_trackback_status)
        self.assertEqual(str(trackback_status), str(loaded_trackback_status))

        self.clean(TrackbackStatus, self.ID)
