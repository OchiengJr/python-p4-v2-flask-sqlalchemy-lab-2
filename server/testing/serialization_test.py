from app import app, db
from server.models import Customer, Item, Review


class TestSerialization:
    """Test cases for serialization of models in models.py"""

    def test_customer_is_serializable(self):
        """Test serialization of Customer."""
        with app.app_context():
            c = Customer(name='Phil')
            db.session.add(c)
            db.session.commit()

            r = Review(comment='great!', customer=c)
            db.session.add(r)
            db.session.commit()

            customer_dict = c.to_dict()

            assert 'id' in customer_dict, "Customer dictionary should have 'id'"
            assert customer_dict['name'] == 'Phil', "Customer name should match"
            assert 'reviews' in customer_dict, "Customer dictionary should have 'reviews'"
            assert 'customer' not in customer_dict['reviews'], "Customer reviews should not contain 'customer' key"

    def test_item_is_serializable(self):
        """Test serialization of Item."""
        with app.app_context():
            i = Item(name='Insulated Mug', price=9.99)
            db.session.add(i)
            db.session.commit()

            r = Review(comment='great!', item=i)
            db.session.add(r)
            db.session.commit()

            item_dict = i.to_dict()

            assert 'id' in item_dict, "Item dictionary should have 'id'"
            assert item_dict['name'] == 'Insulated Mug', "Item name should match"
            assert item_dict['price'] == 9.99, "Item price should match"
            assert 'reviews' in item_dict, "Item dictionary should have 'reviews'"
            assert 'item' not in item_dict['reviews'], "Item reviews should not contain 'item' key"

    def test_review_is_serializable(self):
        """Test serialization of Review."""
        with app.app_context():
            c = Customer()
            i = Item()
            db.session.add_all([c, i])
            db.session.commit()

            r = Review(comment='great!', customer=c, item=i)
            db.session.add(r)
            db.session.commit()

            review_dict = r.to_dict()

            assert 'id' in review_dict, "Review dictionary should have 'id'"
            assert 'customer' in review_dict, "Review dictionary should have 'customer'"
            assert 'item' in review_dict, "Review dictionary should have 'item'"
            assert review_dict['comment'] == 'great!', "Review comment should match"
            assert 'reviews' not in review_dict['customer'], "Customer reviews should not contain 'reviews' key"
            assert 'reviews' not in review_dict['item'], "Item reviews should not contain 'reviews' key"
