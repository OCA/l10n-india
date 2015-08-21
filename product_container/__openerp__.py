# -*- coding: utf-8 -*-
############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011-Today Serpent Consulting Services Pvt. Ltd.
#    (<http://www.serpentcs.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
############################################################################
{
    'name': 'Product Container',
    'version': '1.0',
    'sequence': 110,
    'category': 'Warehouse Management',
    'author': 'Serpent Consulting Services Pvt. Ltd.',
    'website': 'https://www.serpentcs.com',
    'summary': 'Managing the container products',
    'description': """
Efficient management of products and containers
========================================================================
Useful to manage and track containers in which products are delivered to
the customers and to be taken back from customers.

Key Features
+++++++++++++++
A real-time example of use of containers is Oxygen Gas delivered in Cylinder.
With this module you can easily create and manage Cylinder
as container of Oxygen Gas.

* Define product as container (e.g. Cylinder)
* Select container in products (e.g. Oxygen Gas)
* Track containers on hand
* Track containers to be taken back from customers
* Track containers to be taken back from customers

Manage Containers
+++++++++++++++++++++++++
The reusable container products are easily managed by selecting an option
from product form. As we define container as product, its easy to manage
the stock of container. Thus you can track and manage containers efficiently.

Define Products with Containers
++++++++++++++++++++++++++++++++++++++
Create a product and select container for the product, and that's it!

Containers for Multiple Quantities
+++++++++++++++++++++++++++++++++++++++
You can also configure a container to carry more than one quantity of product
by selecting the container product in packaging.

* Define product as container (e.g. Box 30x40x60)
* Select container in packaging
* Select quantity of products and packaging in product sales tab
* Track containers per multiple quantities of product

""",
    'depends': ['l10n_in_base', 'product'],
    'data': [
        'product_container_view.xml',
    ],

    'images': ['images/container1.png',
               'images/container2.png',
               'images/container3.png'],
    'installable': True,
    'application': False,
}

