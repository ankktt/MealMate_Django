# Mealmate - Online Food Ordering System
### **4. Apply Migrations**
```sh
python manage.py migrate
```

### **5. Create a Superuser**
```sh
python manage.py createsuperuser
```

### **6. Run the Development Server**
```sh
python manage.py runserver
```

Now, open your browser and go to `http://127.0.0.1:8000/`

## Directory Structure
```
mealmate/
│── delivery/
│   │── migrations/
│   │── static/
│   │── templates/delivery/
│   │   ├── add_res.html
│   │   ├── base.html
│   │   ├── checkout.html
│   │   ├── cusmenu.html
│   │   ├── customer_home.html
│   │   ├── display_res.html
│   │   ├── failed.html
│   │   ├── index.html
│   │   ├── menu.html
│   │   ├── orders.html
│   │   ├── show_cart.html
│   │   ├── sign_in.html
│   │   ├── sign_up.html
│   │   ├── success.html
│   │   ├── userdata.html
│   │── __init__.py
│   │── admin.py
│   │── apps.py
│   │── forms.py
│   │── models.py
│   │── tests.py
│   │── views.py
│── manage.py
│── requirements.txt
```

## API Endpoints (If Using Django REST Framework)
| Method | Endpoint | Description |
|--------|----------------|--------------------------------|
| GET | `/restaurants/` | List all restaurants |
| POST | `/restaurants/add/` | Add a new restaurant |
| PUT | `/restaurants/update/<id>/` | Update restaurant details |
| DELETE | `/restaurants/delete/<id>/` | Delete a restaurant |
| GET | `/menu/` | Get menu items |
| POST | `/order/` | Place an order |

## Razorpay Payment Integration
1. Sign up at [Razorpay](https://razorpay.com/)
2. Get API keys from Razorpay Dashboard
3. Add API keys to Django settings:
```python
RAZORPAY_KEY_ID = "your_key_id"
RAZORPAY_KEY_SECRET = "your_key_secret"
```

