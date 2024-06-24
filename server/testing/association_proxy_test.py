from app import app, db
from server.models import Customer, Item, Review

class TestAssociationProxy:
    '''Tests for the association proxy between Customer and Item through Review'''

    def test_has_association_proxy(self):
        '''Customer should have an association proxy to items'''
        with app.app_context():
            # Clear the database before running the test
            db.session.query(Review).delete()
            db.session.query(Customer).delete()
            db.session.query(Item).delete()
            db.session.commit()

            # Create a Customer and an Item
            c = Customer(name='John Doe')
            i = Item(name='Sample Item')
            db.session.add_all([c, i])
            db.session.commit()

            # Create a Review to establish the association
            r = Review(comment='Great!', customer_id=c.id, item_id=i.id)
            db.session.add(r)
            db.session.commit()

            # Check if the association proxy 'items' exists in the Customer
            assert hasattr(c, 'items'), "Customer does not have an 'items' association proxy"
            assert i in c.items, "Item not found in customer's items through association proxy"

            # Clean up after test
            db.session.delete(r)
            db.session.delete(c)
            db.session.delete(i)
            db.session.commit()

