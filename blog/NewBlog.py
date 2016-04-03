from blog import Session
from blog.model import Category, PostStatus, Approval, Author, AuthorStatus, CommentStatus, PostType, TrackbackStatus
from Query import Query

from flask import Flask, render_template

app = Flask(__name__)
app.debug = True
#app.propagate_exceptions = True


def load_status_singletons():
    """
    Get the master instances of different statuses.  Attach these to the class as attributes.
    This can be called again when or if the status types change, but is expected only to be called once
    per instance.
    """
    session = Session()
    query = Query(session)
    post_statuses = query.get_post_statuses()
    for post_status in post_statuses:
        setattr(PostStatus, post_status.status, post_status)
    approvals = query.get_approval_statuses()
    for approval in approvals:
        setattr(Approval, approval.status, approval)
    author_statuses = query.get_author_statuses()
    for author_status in author_statuses:
        setattr(AuthorStatus, author_status.status, author_status)
    comment_statuses = query.get_comment_statuses()
    for comment_status in comment_statuses:
        setattr(CommentStatus, comment_status.status, comment_status)
    post_types = query.get_post_types()
    for post_type in post_types:
        setattr(PostType, post_type.type, post_type)
    trackback_statuses = query.get_trackback_statuses()
    for trackback_status in trackback_statuses:
        setattr(TrackbackStatus, trackback_status.status, trackback_status)


def load_categories():
    """
    Get the list of all categories and attach them to the Category class as attributes.
    This should be called whenever a category is added or removed.
    """
    session = Session()
    query = Query(session)
    categories = query.get_categories()
    for category in categories:
        setattr(Category, category.name, category)


@app.route('/')
def index():
    return render_template('main.html', posts=get_posts())


def get_posts():
    session = Session()
    query = Query(session)
    posts = query.load_posts_by_approval_status(PostStatus.publish)
    # TODO consider passing a PostStatus object instead of an id - it seems more natural, right?
    return posts


if __name__ == '__main__':
    load_status_singletons()
    app.run()
