import unittest

from blog import Session
from blog.Model import *
from blog.Query import *


class QueryTest(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        self.queries = Query(self.session)

    def tearDown(self):
        self.session.close()

    # TODO refactor this to a common location - duplicate code from ModelTest
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

    def test_load_post_with_comments(self):
        """
        Normal blog display
        :return:
        """


    def test_load_post_synposis(self):
        """
        Load the post for synopsis display (summary, feed, or main page)
        :return:
        """

    def test_load_post_without_comments(self):
        """
        Load the post for editing.
        :return:
        """

    def test_load_comments(self):
        """
        Load the comments for a separate comment feed
        :return:
        """

    def test_get_post_id_for_permalink(self):
        """
        Get the post ID for a given permalink, used for direct linking to the post.
        :return:
        """

    def test_load_categories_with_posts(self):
        """
        Get the registered categories for the blog (only where posts are present in the category).
        :return:
        """

    def test_load_post_summaries_for_approval(self):
        """
        Load the post summaries for approval.
        :return:
        """

    def test_load_comment_summaries_for_approval(self):
        """
        Load the comment summaries for approval.
        :return:
        """

    def test_load_comment(self):
        """
        Load a single comment with children.
        :return:
        """

    def test_load_authors(self):
        """
        Load the list of authors.
        :return:
        """

    def test_load_approval(self):
        """
        Load the list of approval statuses.
        :return:
        """

    def test_load_author_status(self):
        """
        Load the list of author statuses.
        :return:
        """

    def test_load_category(self):
        """
        Load the list of categories.
        :return:
        """

    def test_load_comment_status(self):
        """
        Load the list of comment statuses.
        :return:
        """

    def test_load_comments_by_status(self):
        """
        Load the comments by a status.
        :return:
        """

    def test_load_posts_by_status(self):
        """
        Load the posts by a status.
        :return:
        """

    def test_load_post_status(self):
        """
        Load the list of post statuses.
        :return:
        """

    def test_load_post_type(self):
        """
        Load the list of post types.
        :return:
        """

    def test_load_posts_by_type(self):
        """
        Load the posts by post type.
        :return:
        """

    def test_load_trackback_status(self):
        """
        Load the list of trackback statuses.
        :return:
        """

