from app import app, db
from server.models import Customer, Item, Review

class TestReview:
    """Test cases for Review model in models.py"""

    def test_can_be_instantiated(self):
        """Test instantiation of Review model."""
        r = Review()
        assert r
        assert isinstance(r, Review)

    def test_has_comment(self):
        """Test Review instantiation with a comment attribute."""
        comment_text = 'great product!'
        r = Review(comment=comment_text)
        assert r.comment == comment_text

    def test_can_be_saved_to_database(self):
        """Test saving Review to database."""
        with app.app_context():
            assert 'comment' in Review.__table__.columns

            r = Review(comment='great!')
            db.session.add(r)
            db.session.commit()

            assert r.id is not None
            assert db.session.query(Review).filter_by(id=r.id).first() is not None

    def test_is_related_to_customer_and_item(self):
        """Test relationships and foreign keys with Customer and Item."""
        with app.app_context():
            assert 'customer_id' in Review.__table__.columns
            assert 'item_id' in Review.__table__.columns

            c = Customer()
            i = Item()
            db.session.add_all([c, i])
            db.session.commit()

            r = Review(comment='great!', customer=c, item=i)
            db.session.add(r)
            db.session.commit()

            # Check foreign keys
            assert r.customer_id == c.id
            assert r.item_id == i.id

            # Check relationships
            assert r.customer == c
            assert r.item == i
            assert r in c.reviews
            assert r in i.reviews
