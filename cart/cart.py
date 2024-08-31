from store.models import Product

class Cart:
    """
    A class to manage the shopping cart.
    """

    def __init__(self, request):
        """
        Initialize the cart.

        Args:
            request (HttpRequest): The current request object.
        """
        self.session = request.session
        # Get the cart from the session, or create an empty one if it doesn't exist
        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            # Initialize the cart if it doesn't exist
            cart = self.session['session_key'] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """
        Add a product to the cart or update its quantity.

        Args:
            product (Product): The product to add to the cart.
            quantity (int, optional): The quantity of the product to add. Defaults to 1.
            update_quantity (bool, optional): Whether to update the quantity of the product
                in the cart. Defaults to False.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            # Add product to cart if it doesn't already exist
            self.cart[product_id] = {'price': str(product.price), 'quantity': quantity}
        else:
            if update_quantity:
                # Update the quantity if it's already in the cart and update_quantity is True
                self.cart[product_id]['quantity'] = quantity
            else:
                # Increment the quantity
                self.cart[product_id]['quantity'] += quantity
        
        self.save()

    def save(self):
        # Update the session cart
        self.session['session_key'] = self.cart
        self.session.modified = True
        
    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_prods(self):
        """
        Get all products in the cart.

        Returns:
            QuerySet: A QuerySet of all products in the cart.
        """
        # Get all product IDs in the cart
        product_ids = self.cart.keys()
        # Get all products in the DB that have an ID in the cart
        products = Product.objects.filter(id__in=product_ids)
        # Return the QuerySet of products
        return products
