from blog import Base
from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, func, Integer, String

TEXT = 655535
LONGTEXT = 4294967295


class Approval(Base):
    __tablename__ = 'approval'

    id = Column('id', Integer, primary_key=True)
    status = Column('status', String(20))
    description = Column('description', String(255))

    def __repr__(self):
        return "<Approval(id=%d,status=%s,description=%s)>" % (
            self.id, self.status, self.description
        )


class Author(Base):
    __tablename__ = 'author'

    id = Column('id', Integer, primary_key=True)
    login = Column('login', String(128))
    password = Column('password', String(128))
    email = Column('email', String(255))
    url = Column('url', String(1024))
    created = Column('created', DateTime, default=func.now())
    activation_key = Column('activation_key', String(2048))
    status = Column('status_id', Integer, ForeignKey('AuthorStatus.id'))
    display_name = Column('display_name', String(64))

    def __repr__(self):
        return "<Author(id=%s,login=%s,email=%s,url=%s,created=%s,status=%s,display_name=%s)>" % (
            self.id, self.login, self.email, self.url, self.created, self.status, self.display_name
        )


class AuthorStatus(Base):
    __tablename__ = 'author_status'

    id = Column('id', Integer, primary_key=True)
    status = Column('status', String(20))
    description = Column('description', String(255))

    def __repr__(self):
        return "<AuthorStatus(id=%s,status=%s,description=%s)>" % (
            self.id, self.status, self.description
        )


class Category(Base):
    __tablename__ = 'category'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(255))
    description = Column('description', String(255))
    visible = Column('visible', Boolean)

    def __repr__(self):
        return "<Category(id=%s,name=%s,description=%s,visible=%s)>" % (
            self.id, self.name, self.description, self.visible
        )


class Comment(Base):
    __tablename__ = 'comment'

    id = Column('id', Integer, primary_key=True)
    parent = Column('parent_id', Integer, ForeignKey('Comment.id'))
    post = Column('post_id', Integer, ForeignKey('Post.id'))
    author_name = Column('author', String(255))
    author_email = Column('author_email', String(255))
    author_url = Column('author_url', String(255))
    author_IP = Column('author_IP', String(39))
    author = Column('author_id', Integer, ForeignKey('Author.id'))
    date = Column('date', DateTime, default=func.now())
    content = Column('content', String(TEXT))
    approval = Column('approval_id', Integer, ForeignKey('Approval.id'))
    agent = Column('agent', String(255))
    type = Column('type', String(20))

    def __repr__(self):
        return "<Comment(id=%s,parent_id=%s,post_id=%s,author_name=%s,author_email=%s,author_url=%s,author_IP=%s," \
               "author_id=%s,date=%s,len(content)=%s,approval=%s,agent=%s,type=%s" % (
            self.id, self.parent.id, self.post.id, self.author_name, self.author_email, self.author_url, self.author_IP,
            self.author.id, self.date, len(self.content), self.approval, self.agent, self.type
        )


class CommentStatus(Base):
    __tablename__ = 'comment_status'

    id = Column('id', Integer, primary_key=True)
    status = Column('status', String(20))
    description = Column('description', String(255))

    def __repr__(self):
        return "<CommentStatus(id=%s,status=%s,description=%s)>" % (
            self.id, self.status, self.description
        )


class Post(Base):
    __tablename__ = 'post'

    id = Column('id', Integer, primary_key=True)
    parent = Column('parent_id', Integer, ForeignKey("Post.id"))
    author = Column('author_id', Integer, ForeignKey("Author.id"))
    date = Column('date', DateTime, default=func.now())
    modified = Column('modified', DateTime)
    title = Column('title', String(TEXT))
    excerpt = Column('excerpt', String(TEXT))
    trackback_excerpt = Column('trackback_excerpt', String(TEXT))
    content = Column('content', String(LONGTEXT))
    content_filtered = Column('content_filtered', String(LONGTEXT))
    category = Column('category_id', Integer, ForeignKey('Category.id'))
    post_status = Column('post_status_id', Integer, ForeignKey('PostStatus.id'))
    approval = Column('approval_id', Integer, ForeignKey('Approval.id'))
    password = Column('password', String(128))
    post_type = Column('post_type_id', Integer, ForeignKey('PostType.id'))
    mime_type = Column('mime_type', String)
    latitude = Column('latitude', Float)
    longitude = Column('longitude', Float)
    trackback_status = Column('trackback_status_id', Integer, ForeignKey('TrackbackStatus.id'))
    name = Column('name', String)
    comment_status = Column('comment_status_id', Integer, ForeignKey('CommentStatus.id'))
    comment_count = Column('comment_count', Integer)

    def __repr__(self):
        return "<Post(id=%s,parent_id=%s,author_id=%s,date=%s,modified=%s,title=%s,len(content)=%s,category=%s," \
               "approval=%s)>" % (
            self.id, self.parent.id, self.author.id, self.date, self.modified, self.title, len(self.content),
            self.category, self.approval
        )


class PostStatus(Base):
    __tablename__ = 'post_status'

    id = Column('id', Integer, primary_key=True)
    status = Column('status', String(20))
    description = Column('description', String(255))

    def __repr__(self):
        return "<PostStatus(id=%s,status=%s,description=%s)>" % (
            self.id, self.status, self.description
        )

class PostType(Base):
    __tablename__ = 'post_type'

    id = Column('id', Integer, primary_key=True)
    type = Column('type', String(20))
    description = Column('description', String(255))

    def __repr__(self):
        return "<PostType(id=%s,type=%s,description=%s)>" % (
            self.id, self.type, self.description
        )


class TrackbackStatus(Base):
    __tablename__ = 'trackback_status'

    id = Column('id', Integer, primary_key=True)
    status = Column('status', String(20))
    description = Column('description', String(255))

    def __repr_(self):
        return "<TrackbackStatus(id=%s,status=%s,description=%s)>" % (
            self.id, self.status, self.description
        )

