# cs421-deliverable3

# Installation

You need `python 3` to run this. If you just installed python, make sure you're using 3 with `python --version`. Your pip should also map to python 3 (`pip --version` should point to python 3)


If you're running pyhont 2 but you have 3 installed, you can just use `python3` or `pip3` instead of the `python` or `pip` commands.

First, run this to get setup:
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
This will create a self-contained environment where you have all the dependencies of this project. Once that's done, create the `cs421` database in postgres. Log in using your postgres account to this DB and execute the following commands (just copy paste):
```
CREATE TABLE Account (
username varchar(255) UNIQUE NOT NULL PRIMARY KEY,
password varchar(255) NOT NULL,
email varchar(255) UNIQUE NOT NULL,
creation_date date
);

CREATE TABLE DeveloperAccount (
    studio_name varchar(255)
) inherits (Account);

CREATE TABLE UserAccount (
    name varchar(255) NOT NULL
) inherits (Account);

CREATE TABLE PaymentMethods (
    date_added date NOT NULL,
    is_primary boolean NOT NULL,
    username varchar(255) NOT NULL,
    PRIMARY KEY (username, date_added)
);

CREATE RULE payment_username_ref
AS ON INSERT TO PaymentMethods
WHERE new.username NOT IN (SELECT username FROM Account)
DO INSTEAD NOTHING;

CREATE TABLE RiseupWallet (
    public_key varchar(255) NOT NULL
) inherits (PaymentMethods);

CREATE RULE riseup_wallet_username_ref
AS ON INSERT TO RiseupWallet
WHERE new.username NOT IN (SELECT username FROM Account)
DO INSTEAD NOTHING;

CREATE TABLE CreditCard (
    card_number varchar(255) NOT NULL,
    cvc varchar(255) NOT NULL,
    exp_date date NOT NULL
) inherits (PaymentMethods);

CREATE RULE cc_wallet_username_ref
AS ON INSERT TO CreditCard
WHERE new.username NOT IN (SELECT username FROM Account)
DO INSTEAD NOTHING;

CREATE TABLE Paypal (
    pp_email varchar (255) NOT NULL,
pp_password varchar (255) NOT NULL
) inherits (PaymentMethods);

CREATE RULE paypal_wallet_username_ref
AS ON INSERT TO Paypal
WHERE new.username NOT IN (SELECT username FROM Account)
DO INSTEAD NOTHING;

CREATE TABLE GameListing (
    listing_id serial PRIMARY KEY,
    title varchar (255) NOT NULL UNIQUE,
    description text,
    is_on_sale boolean,
    price float8 NOT NULL,
    category varchar (255),
    sale_price float8,
    developer_username varchar(255) NOT NULL
);

CREATE RULE gamelisting_username_ref
AS ON INSERT TO GameListing
WHERE new.developer_username NOT IN (SELECT username FROM DeveloperAccount)
DO INSTEAD NOTHING;


CREATE TABLE GameKey (
    key varchar (255) PRIMARY KEY,
    redeemed boolean,
    listing_id serial references GameListing(listing_id)
);

CREATE TABLE ShoppingCart (
    username varchar(255) NOT NULL, 
    listing_id serial references GameListing(listing_id),
quantity integer,
    PRIMARY KEY (username, listing_id)
);

CREATE RULE shoppingcart_username_ref
AS ON INSERT TO ShoppingCart
WHERE new.username NOT IN (SELECT username FROM UserAccount)
DO INSTEAD NOTHING;

CREATE TABLE Orders (
    order_id serial PRIMARY KEY,
    username varchar(255) NOT NULL,
    total float8
);

CREATE RULE orders_username_ref
AS ON INSERT TO Orders
WHERE new.username NOT IN (SELECT username FROM UserAccount)
DO INSTEAD NOTHING;


CREATE TABLE OrderListing (
    order_id serial references Orders(order_id),
    listing_id serial references GameListing(listing_id),
    PRIMARY KEY (order_id, listing_id)
);


CREATE TABLE DeveloperOrders(
    username varchar(255) NOT NULL,
    order_id serial references GameListing(listing_id),
    PRIMARY KEY (username, order_id)
);

CREATE RULE devorders_username_ref
AS ON INSERT TO DeveloperOrders
WHERE new.username NOT IN (SELECT username FROM DeveloperAccount)
DO INSTEAD NOTHING;

CREATE TABLE Reviews (
    username varchar(255) NOT NULL,
    listing_id serial references GameListing(listing_id),  
    rating integer NOT NULL,
    content text NOT NULL,
    date timestamp,
    PRIMARY KEY (username, listing_id)
);

CREATE RULE reviews_username_ref
AS ON INSERT TO Reviews
WHERE new.username NOT IN (SELECT username FROM UserAccount)
DO INSTEAD NOTHING;
```

From here, all you need to do is run:
```
python app.py
```

And open `index.html` to run the app.
