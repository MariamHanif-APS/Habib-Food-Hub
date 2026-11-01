# Habib Food Hub
### Habib University Food Vendor and Inventory Management System

Habib Food Hub is a desktop application project that brings Habib University’s food vendors—including Grito, Tapal, Hobnob and Cafe2Go—into one interface.

The system is designed to help students view menus, prices, operating hours and food availability, while allowing vendors to manage inventory and administrators to review vendor applications.

This repository contains an interactive **Python and PyQt6 UI prototype**, with an editable **Qt Designer interface file**.

## Project Overview

The project explores how a database-backed application can connect campus food discovery, vendor management, inventory maintenance and pickup ordering.

The complete system design supports three roles:

| Role | Intended Capabilities |
| --- | --- |
| Student | Browse approved vendors, search menus, manage a cart, place pickup orders and view order history. |
| Food Vendor | Register, maintain menus and operating hours, update inventory, review orders and change order status. |
| Administrator | Review vendor applications, approve or reject vendors and manage vendor records. |

Payment is collected at the vendor counter. Online payments, delivery tracking and integration with external university systems are outside the project scope.

## Designed System Features
<img width="548" height="615" alt="Screenshot 2026-11-01 at 8 57 40 PM" src="https://github.com/user-attachments/assets/5c42f82a-5f85-4b34-8596-7dfcba56ad5c" />
<img width="1470" height="956" alt="Screenshot 2026-11-01 at 8 58 01 PM" src="https://github.com/user-attachments/assets/6e88c47e-7365-48f3-a659-cb59ccf4c0f4" />
<img width="1470" height="956" alt="Screenshot 2026-11-01 at 8 58 07 PM" src="https://github.com/user-attachments/assets/f6eabc09-a0d8-4c2d-bb74-edfdd647004b" />
<img width="1470" height="956" alt="Screenshot 2026-11-01 at 8 58 15 PM" src="https://github.com/user-attachments/assets/75c41d31-767b-4433-81f1-bb75ba6e9801" />

### Authentication and Role-Based Access

- Login for students, approved food vendors and administrators.
- Role-specific dashboards and authorized access.
- Vendor registration with pending approval status.

### Vendor Approval and Profile Management

- Administrator review of vendor applications.
- Approval or rejection of prospective vendors.
- Student visibility restricted to approved vendors.
- Management of vendor contact information, campus location and operating hours.

### Menu and Inventory Management

- Vendor-specific menu categories.
- Menu items with names, descriptions, prices and stock quantities.
- Configurable low-stock thresholds.
- Availability calculated as Available, Low Stock or Out of Stock.
- Deactivation of menu items to preserve historical order records.

### Vendor and Menu Browsing

- Browsing and searching approved vendors.
- Open or Closed status calculated from operating hours.
- Menu browsing with prices and availability.
- Ordering restricted to active, available items.

### Cart and Checkout

- A cart containing items from one vendor.
- Quantity validation against available stock.
- Review of item quantities, subtotals and total cost.
- Checkout designed as one atomic database transaction.

### Order Management and Reporting

- Student order history.
- Vendor views of incoming orders.
- Order states: Pending, Preparing, Ready for Pickup, Completed and Cancelled.
- Inventory reports showing remaining quantities and availability.

## Database Design

The project documentation includes a conceptual ERD, a relational schema and consistency notes connecting the requirements, interfaces and database relations.

| Relation | Purpose |
| --- | --- |
| USER_ACCOUNT | Stores shared login identity and user role. |
| STUDENT | Stores student-specific information. |
| VENDOR | Stores vendor profiles, approval status and operating hours. |
| ADMINISTRATOR | Stores administrator-specific information. |
| CATEGORY | Organizes menu categories belonging to each vendor. |
| MENU_ITEM | Stores item details, prices, stock and low-stock thresholds. |
| CART | Records a student’s cart and selected vendor. |
| CART_ITEM | Stores the items and quantities in a cart. |
| CUSTOMER_ORDER | Stores confirmed order details, totals and status. |
| ORDER_ITEM | Stores ordered quantities and historical selling prices. |

### Key Design Decisions

- Shared account information is separated from role-specific data.
- Menu-item ownership is determined through its category.
- CART_ITEM and ORDER_ITEM resolve many-to-many relationships.
- Composite primary keys prevent duplicate item rows within a cart or order.
- Foreign keys maintain referential integrity.
- Availability is derived from stock quantities rather than stored separately.
- Historical unit prices are preserved even when menu prices change.
- Previously ordered menu items are deactivated rather than deleted.

### Planned Checkout Transaction

1. Verify vendor approval and confirm that all cart items belong to the selected vendor.
2. Validate item eligibility and sufficient stock.
3. Create the order and its line items.
4. Store the selling prices and confirmed total.
5. Reduce stock quantities.
6. Mark the cart as checked out.
7. Commit all changes together, or roll back if any step fails.

### Business Rules

- Account email addresses and student ID numbers must be unique.
- Category names must be unique within each vendor.
- Menu prices must be positive.
- Stock quantities and low-stock thresholds cannot be negative.
- Cart and order quantities must be positive.
- A student may have at most one active cart.
- All items in a cart must belong to the same vendor.
- Cancelled orders require a controlled restocking operation to prevent duplicate stock restoration.

## Current Prototype

The application currently demonstrates:

- Student, Food Vendor and Administrator workspaces.
- Campus vendor cards and sample menus.
- Sample availability and inventory indicators.
- An interactive cart with calculated totals.
- A checkout confirmation interaction.
- Adding menu items to the inventory table during the current session.
- Vendor registration and profile interfaces.
- Administrator application-review screens.
- Sample order-history and incoming-order views.

### Implementation Status

This version uses sample data and does not connect to a database.

Login is simulated. Several controls demonstrate intended interactions without saving changes. Checkout does not yet perform stock validation, inventory deduction or persistent order creation. Search, vendor approval, profile saving and order-status management are illustrative or partially implemented.

Changes are not preserved after the application closes. The database requirements above describe the intended complete system.

## Technologies

- **Python 3:** Application logic.
- **PyQt6:** Desktop interface, widgets, dialogs and navigation.
- **Qt Designer:** Editable interface layout.
- **Qt Style Sheets:** Colours, typography and component styling.
- **Relational Database Modelling:** ERD, schema, integrity constraints and transaction design.

## Files

| File | Description |
| --- | --- |
| app.py | Application logic, styling and prototype interactions. |
| habib_food_hub.ui | Editable Qt Designer interface loaded by the application. |
| README.md | Project overview and setup instructions. |

## How to Run

### 1. Install Python 3

Make sure Python 3 is installed on your computer.

### 2. Install PyQt6

Run the following command in your terminal:

```bash
python3 -m pip install PyQt6
```

### 3. Check the Filenames

Keep these two files in the same folder:

```text
app.py
habib_food_hub.ui
```

If downloaded files include suffixes such as `(1)`, rename them to match the filenames above. The application specifically looks for `habib_food_hub.ui`.

### 4. Launch the Application

Open a terminal in the project folder and run:

```bash
python3 app.py
```

### 5. Explore the Prototype

Select Student, Food Vendor or Administrator on the login screen and click **Log in**.

Real credentials and a database server are not required for this prototype.




