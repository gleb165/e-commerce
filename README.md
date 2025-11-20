# Natash Clothing Store

Natash is a web-based platform for selling clothes online. The project is built using Django and provides features for user authentication, product management, shopping carts, and order processing.

## Features

- **User Accounts**: Registration, login, and profile management using custom user model with phone number support.
- **Product Catalog**: Add, view, and manage clothing products.
- **Shopping Cart**: Users can add products to their cart and manage quantities.
- **Order Management**: Place orders, track order status, and view order history.
- **Flexible Delivery**: Supports home delivery and post office pickup with detailed address management.

## Project Structure

- `accounts/`: User authentication and address management.
- `products/`: Product models, views, and admin configuration.
- `carts/`: Shopping cart logic and models.
- `orders/`: Order models and processing.
- `backend/`: Django project settings, URLs, and configuration.

## Getting Started

1. **Clone the repository**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```
4. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```
5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```
6. **Access the site**: Open [http://localhost:8000](http://localhost:8000) in your browser.

## Models Overview

- **User**: Extends Django's AbstractUser, adds phone number.
- **Address**: Stores user addresses for delivery or post office pickup.
- **Product**: Represents clothing items for sale.
- **Cart**: Manages products added by users.
- **Order**: Handles order details and status.

## Customization

- Add new product categories or attributes in `products/models.py`.
- Extend user profile features in `accounts/models.py`.
- Customize delivery options in `accounts/models.py` (Address).

## License

This project is for educational and demonstration purposes.
