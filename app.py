"""Habib Food Hub - PyQt6 UI prototype.

Run with:  python app.py
The editable Qt Designer source is habib_food_hub.ui.
"""

import sys
from pathlib import Path

from PyQt6 import uic
from PyQt6.QtCore import Qt, QTime
from PyQt6.QtGui import QColor, QFont
from PyQt6.QtWidgets import (
    QApplication, QComboBox, QDialog, QDialogButtonBox, QFormLayout,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListWidgetItem, QMainWindow, QMessageBox, QPushButton, QSpinBox,
    QTableWidget, QTableWidgetItem, QTimeEdit, QVBoxLayout, QWidget
)


ROOT = Path(__file__).resolve().parent

COLORS = {
    "plum": "#4d225b", "plum2": "#6b347a", "saffron": "#efad18",
    "coral": "#dd7355", "ink": "#241f27", "muted": "#756e79",
    "line": "#e8e0e8", "canvas": "#f6f3f5", "surface": "#ffffff",
    "green": "#278257", "red": "#c64f55", "amber": "#bc7b0a",
}


APP_STYLE = """
* { font-family: "Segoe UI", "Arial"; color: #241f27; }
QMainWindow, QWidget#centralwidget, QWidget#loginPage, QWidget#appPage { background: #f6f3f5; }
QFrame#loginCard { background: white; border: 1px solid #e8e0e8; border-radius: 22px; }
QLabel#loginMark { background: #efad18; color: #4d225b; border-radius: 16px; font-size: 25px; font-weight: 900; }
QLabel#loginTitle { font-size: 24px; font-weight: 800; }
QLabel#loginSubtitle { color: #756e79; font-size: 13px; }
QLabel#emailLabel, QLabel#passwordLabel, QLabel#loginRoleLabel { font-size: 11px; font-weight: 700; }
QLineEdit, QComboBox, QSpinBox, QTimeEdit { background: white; border: 1px solid #e3dbe4; border-radius: 10px; padding: 9px 11px; min-height: 20px; }
QLineEdit:focus, QComboBox:focus, QSpinBox:focus, QTimeEdit:focus { border: 1px solid #8c5c99; }
QPushButton { border: 1px solid #e3dbe4; border-radius: 10px; padding: 9px 13px; background: white; font-weight: 700; }
QPushButton:hover { background: #f7f1f8; }
QPushButton#loginButton, QPushButton#quickActionButton, QPushButton[accent="true"] { background: #dd7355; color: #2d1712; border: none; }
QPushButton#vendorRegistrationButton { color: #4d225b; }
QFrame#sidebar { background: #4d225b; border: none; }
QFrame#sidebar QLabel { color: white; }
QLabel#brandLabel { font-size: 18px; font-weight: 850; }
QLabel#brandSubtitle, QLabel#previewLabel, QLabel#workspaceLabel { color: #d6c4da; font-size: 10px; font-weight: 750; letter-spacing: 1px; }
QComboBox#roleCombo { background: #654170; color: white; border: 1px solid #7b5885; }
QListWidget#navigationList { background: transparent; border: none; color: #eee5f0; outline: none; font-weight: 650; }
QListWidget#navigationList::item { padding: 12px 11px; margin: 2px 0; border-radius: 10px; }
QListWidget#navigationList::item:selected { background: white; color: #4d225b; }
QListWidget#navigationList::item:hover:!selected { background: #684374; }
QFrame#profileFrame { border-top: 1px solid #76527f; }
QLabel#profileAvatar { background: #f4d7ca; color: #713722; border-radius: 12px; font-weight: 800; }
QLabel#profileName { font-weight: 750; }
QLabel#profileRole { color: #d1bfd5; font-size: 11px; }
QPushButton#logoutButton { background: transparent; color: #e9deeb; border: 1px solid #76527f; }
QFrame#topbar { background: white; border-bottom: 1px solid #e8e0e8; }
QLabel#breadcrumbLabel { color: #756e79; font-size: 13px; }
QPushButton#notificationButton { background: #faf8fa; }
QStackedWidget#contentStack > QWidget { background: #f6f3f5; }
QFrame[card="true"] { background: white; border: 1px solid #e8e0e8; border-radius: 16px; }
QLabel[eyebrow="true"] { color: #6b347a; font-size: 10px; font-weight: 800; }
QLabel[pageTitle="true"] { font-size: 27px; font-weight: 850; }
QLabel[subtitle="true"] { color: #756e79; font-size: 12px; }
QLabel[statValue="true"] { font-size: 27px; font-weight: 850; }
QLabel[muted="true"] { color: #756e79; font-size: 11px; }
QLabel[sectionTitle="true"] { font-size: 16px; font-weight: 800; }
QLabel[badge="good"] { color: #278257; background: #e8f6ee; border-radius: 9px; padding: 4px 8px; font-size: 10px; font-weight: 750; }
QLabel[badge="warn"] { color: #9b6505; background: #fff4d8; border-radius: 9px; padding: 4px 8px; font-size: 10px; font-weight: 750; }
QLabel[badge="bad"] { color: #c64f55; background: #ffebec; border-radius: 9px; padding: 4px 8px; font-size: 10px; font-weight: 750; }
QLabel[badge="neutral"] { color: #655c68; background: #f0edf1; border-radius: 9px; padding: 4px 8px; font-size: 10px; font-weight: 750; }
QTableWidget { background: white; border: 1px solid #e8e0e8; border-radius: 14px; gridline-color: #eee8ef; selection-background-color: #f1e8f3; alternate-background-color: #fbf9fb; }
QHeaderView::section { background: #f8f5f8; color: #756e79; border: none; border-bottom: 1px solid #e8e0e8; padding: 9px; font-size: 10px; font-weight: 800; }
QTableWidget::item { padding: 8px; }
"""


def label(text, **props):
    w = QLabel(text)
    w.setWordWrap(True)
    for key, value in props.items():
        w.setProperty(key, value)
    return w


def card(layout=None):
    frame = QFrame()
    frame.setProperty("card", True)
    if layout is None:
        layout = QVBoxLayout()
    layout.setContentsMargins(18, 18, 18, 18)
    layout.setSpacing(10)
    frame.setLayout(layout)
    return frame


def page_header(eyebrow, title, subtitle, action_text=None, action=None):
    row = QHBoxLayout()
    copy = QVBoxLayout()
    copy.setSpacing(4)
    copy.addWidget(label(eyebrow.upper(), eyebrow=True))
    copy.addWidget(label(title, pageTitle=True))
    copy.addWidget(label(subtitle, subtitle=True))
    row.addLayout(copy, 1)
    if action_text:
        button = QPushButton(action_text)
        button.setProperty("accent", True)
        if action:
            button.clicked.connect(action)
        row.addWidget(button, 0, Qt.AlignmentFlag.AlignTop)
    return row


def stat_card(title, value, detail):
    box = card()
    box.layout().addWidget(label(title, muted=True))
    box.layout().addWidget(label(value, statValue=True))
    detail_label = label(detail, muted=True)
    detail_label.setStyleSheet("color:#278257")
    box.layout().addWidget(detail_label)
    return box


def badge(text, kind="neutral"):
    w = label(text, badge=kind)
    w.setAlignment(Qt.AlignmentFlag.AlignCenter)
    return w


def make_table(headers, rows, stretch_column=0):
    table = QTableWidget(len(rows), len(headers))
    table.setHorizontalHeaderLabels(headers)
    table.setAlternatingRowColors(True)
    table.setShowGrid(False)
    table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
    table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
    table.verticalHeader().setVisible(False)
    table.horizontalHeader().setStretchLastSection(False)
    for col in range(len(headers)):
        mode = QHeaderView.ResizeMode.Stretch if col == stretch_column else QHeaderView.ResizeMode.ResizeToContents
        table.horizontalHeader().setSectionResizeMode(col, mode)
    for r, row in enumerate(rows):
        for c, value in enumerate(row):
            if isinstance(value, QWidget):
                table.setCellWidget(r, c, value)
            else:
                table.setItem(r, c, QTableWidgetItem(str(value)))
        table.setRowHeight(r, 44)
    table.setMinimumHeight(min(420, 62 + len(rows) * 44))
    return table


class VendorRegistrationDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("New Food Vendor Registration")
        self.setMinimumWidth(500)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(28, 26, 28, 26)
        layout.addWidget(label("NEW VENDOR APPLICATION", eyebrow=True))
        layout.addWidget(label("Register a food vendor", pageTitle=True))
        layout.addWidget(label("The account will remain pending until an administrator approves it.", subtitle=True))
        form = QFormLayout()
        form.setSpacing(12)
        for caption, placeholder in [
            ("Vendor name", "e.g. Cafe2Go"), ("Contact number", "0300-0000000"),
            ("Campus location", "e.g. Basement, Student Center"),
            ("Email", "vendor@habib.edu.pk"), ("Password", "Create a password")
        ]:
            edit = QLineEdit()
            edit.setPlaceholderText(placeholder)
            if caption == "Password":
                edit.setEchoMode(QLineEdit.EchoMode.Password)
            form.addRow(caption, edit)
        open_time, close_time = QTimeEdit(QTime(8, 30)), QTimeEdit(QTime(19, 0))
        form.addRow("Opening time", open_time)
        form.addRow("Closing time", close_time)
        layout.addLayout(form)
        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Save)
        buttons.button(QDialogButtonBox.StandardButton.Save).setText("Submit application")
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)


class AddItemDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Menu Item")
        self.setMinimumWidth(470)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(26, 24, 26, 24)
        layout.addWidget(label("MENU AND INVENTORY", eyebrow=True))
        layout.addWidget(label("Add a menu item", pageTitle=True))
        form = QFormLayout()
        self.name = QLineEdit("Chicken Wrap")
        self.category = QComboBox(); self.category.addItems(["Snacks", "Main Course", "Drinks", "Desserts"])
        self.price = QSpinBox(); self.price.setRange(1, 10000); self.price.setValue(320)
        self.stock = QSpinBox(); self.stock.setRange(0, 10000); self.stock.setValue(15)
        self.threshold = QSpinBox(); self.threshold.setRange(0, 1000); self.threshold.setValue(5)
        for caption, widget in [("Item name", self.name), ("Category", self.category), ("Price (PKR)", self.price), ("Starting stock", self.stock), ("Low-stock threshold", self.threshold)]:
            form.addRow(caption, widget)
        layout.addLayout(form)
        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Save)
        buttons.button(QDialogButtonBox.StandardButton.Save).setText("Add item")
        buttons.accepted.connect(self.accept); buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)


class HabibFoodHub(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ROOT / "habib_food_hub.ui", self)
        self.setStyleSheet(APP_STYLE)
        self.mainStack.setCurrentWidget(self.loginPage)
        self.cart = {"Zinger Roll": [2, 250], "Cold Coffee": [1, 200]}
        self.foods = [
            ["Zinger Roll", "Snacks", 250, 12], ["Beef Burger", "Main Course", 380, 6],
            ["Chicken Karahi", "Main Course", 650, 0], ["Cold Coffee", "Drinks", 200, 20],
            ["Brownie", "Desserts", 220, 8], ["Club Sandwich", "Snacks", 420, 9],
        ]
        self.role_pages = {
            "Student": [("Dashboard", self.studentDashboardPage), ("Food vendors", self.foodVendorsPage), ("Menu and cart", self.menuCartPage), ("My orders", self.studentOrdersPage)],
            "Food Vendor": [("Dashboard", self.vendorDashboardPage), ("Menu and inventory", self.inventoryPage), ("Incoming orders", self.incomingOrdersPage), ("Profile and hours", self.vendorProfilePage)],
            "Administrator": [("Dashboard", self.adminDashboardPage), ("Vendor applications", self.vendorApplicationsPage), ("All vendors", self.allVendorsPage)],
        }
        self.profiles = {
            "Student": ("MH", "Mariam Hanif", "Student account"),
            "Food Vendor": ("GR", "Grito", "Food vendor"),
            "Administrator": ("AD", "Food Hub Admin", "Administrator"),
        }
        self._build_pages()
        self._connect_signals()

    def _connect_signals(self):
        self.loginButton.clicked.connect(self.login)
        self.vendorRegistrationButton.clicked.connect(self.register_vendor)
        self.logoutButton.clicked.connect(lambda: self.mainStack.setCurrentWidget(self.loginPage))
        self.roleCombo.currentTextChanged.connect(self.set_role)
        self.navigationList.currentRowChanged.connect(self.navigate)
        self.quickActionButton.clicked.connect(self.quick_action)

    def login(self):
        role = self.loginRoleCombo.currentText()
        self.roleCombo.setCurrentText(role)
        self.mainStack.setCurrentWidget(self.appPage)
        self.set_role(role)

    def register_vendor(self):
        dialog = VendorRegistrationDialog(self)
        if dialog.exec():
            QMessageBox.information(self, "Application submitted", "The vendor application has been created with Pending status.")

    def set_role(self, role):
        self.navigationList.clear()
        for title, _page in self.role_pages[role]:
            self.navigationList.addItem(QListWidgetItem(title))
        avatar, name, account = self.profiles[role]
        self.profileAvatar.setText(avatar); self.profileName.setText(name); self.profileRole.setText(account)
        self.quickActionButton.setText({"Student": "Find food", "Food Vendor": "Add menu item", "Administrator": "Review queue"}[role])
        self.navigationList.setCurrentRow(0)

    def navigate(self, row):
        role = self.roleCombo.currentText()
        if row < 0 or row >= len(self.role_pages[role]):
            return
        title, page = self.role_pages[role][row]
        self.contentStack.setCurrentWidget(page)
        self.breadcrumbLabel.setText(f"Food Hub  /  {title}")

    def quick_action(self):
        role = self.roleCombo.currentText()
        if role == "Student": self.navigationList.setCurrentRow(1)
        elif role == "Food Vendor": self.add_item()
        else: self.navigationList.setCurrentRow(1)

    def _build_pages(self):
        self.build_student_dashboard(); self.build_vendors(); self.build_menu_cart(); self.build_student_orders()
        self.build_vendor_dashboard(); self.build_inventory(); self.build_incoming_orders(); self.build_vendor_profile()
        self.build_admin_dashboard(); self.build_applications(); self.build_all_vendors()

    def build_student_dashboard(self):
        L = self.studentDashboardLayout
        L.addLayout(page_header("Good afternoon, Mariam", "What would you like to eat?", "Check what is open, see live availability and order ahead for pickup.", "Browse vendors", lambda: self.goto("Food vendors")))
        stats = QGridLayout()
        for i, data in enumerate([("Open now", "3", "of 4 campus vendors"), ("Ready for pickup", "1", "Order #1042"), ("Menu items", "47", "39 currently available"), ("This month", "8", "orders placed")]):
            stats.addWidget(stat_card(*data), 0, i)
        L.addLayout(stats)
        rows = [["Zinger Roll", "Grito", "Rs. 250", badge("12 available", "good")], ["Cold Coffee", "Grito", "Rs. 200", badge("20 available", "good")], ["Beef Burger", "Grito", "Rs. 380", badge("6 left", "warn")], ["Club Sandwich", "Cafe2Go", "Rs. 420", badge("9 available", "good")]]
        box = card(); box.layout().addWidget(label("Popular right now", sectionTitle=True)); box.layout().addWidget(make_table(["Item", "Vendor", "Price", "Availability"], rows, 0)); L.addWidget(box); L.addStretch()

    def build_vendors(self):
        L = self.foodVendorsLayout
        L.addLayout(page_header("Campus dining", "Food vendors", "Only approved vendors appear here. Open or closed is calculated from operating hours."))
        search = QLineEdit(); search.setPlaceholderText("Search vendors by name or location"); L.addWidget(search)
        grid = QGridLayout(); grid.setSpacing(14)
        vendors = [("Grito", "Ground Floor, Student Center", "8:30 AM - 7:00 PM", True), ("Tapal", "Courtyard, Student Center", "9:00 AM - 9:00 PM", True), ("Hobnob", "1st Floor, ADFC", "9:00 AM - 8:00 PM", False), ("Cafe2Go", "Basement, Student Center", "7:00 AM - 6:00 PM", True)]
        for i, (name, location, hours, opened) in enumerate(vendors):
            box = card(); box.setMinimumHeight(180)
            top = QHBoxLayout(); top.addWidget(label(name, sectionTitle=True)); top.addStretch(); top.addWidget(badge("Open now" if opened else "Closed", "good" if opened else "bad")); box.layout().addLayout(top)
            box.layout().addWidget(label(location, muted=True)); box.layout().addWidget(label(hours, muted=True))
            btn = QPushButton("View menu"); btn.setProperty("accent", True); btn.clicked.connect(lambda _=False: self.goto("Menu and cart")); box.layout().addWidget(btn)
            grid.addWidget(box, i // 2, i % 2)
        L.addLayout(grid); L.addStretch()

    def build_menu_cart(self):
        L = self.menuCartLayout
        L.addLayout(page_header("Grito - Open until 7:00 PM", "Menu and cart", "Add available items from one vendor and collect the order at the counter.", "Change vendor", lambda: self.goto("Food vendors")))
        body = QHBoxLayout(); products = QGridLayout(); products.setSpacing(12)
        for i, food in enumerate(self.foods):
            name, category, price, stock = food
            box = card(); box.setMinimumWidth(200)
            box.layout().addWidget(label(name, sectionTitle=True)); box.layout().addWidget(label(category, muted=True))
            status = badge("Out of stock" if stock == 0 else f"{stock} left", "bad" if stock == 0 else "warn" if stock <= 6 else "good")
            box.layout().addWidget(status, 0, Qt.AlignmentFlag.AlignLeft); box.layout().addWidget(label(f"Rs. {price}", sectionTitle=True))
            btn = QPushButton("Add to cart"); btn.setProperty("accent", True); btn.setEnabled(stock > 0); btn.clicked.connect(lambda _=False, f=food: self.add_to_cart(f)); box.layout().addWidget(btn)
            products.addWidget(box, i // 3, i % 3)
        products_widget = QWidget(); products_widget.setLayout(products); body.addWidget(products_widget, 1)
        self.cartBox = card(); self.cartBox.setMinimumWidth(300); self.cartBox.setMaximumWidth(350); body.addWidget(self.cartBox)
        L.addLayout(body); self.refresh_cart(); L.addStretch()

    def refresh_cart(self):
        while self.cartBox.layout().count():
            item = self.cartBox.layout().takeAt(0)
            if item.widget(): item.widget().deleteLater()
        self.cartBox.layout().addWidget(label("Your cart", sectionTitle=True)); self.cartBox.layout().addWidget(label("Grito - Pickup order", muted=True))
        total = 0
        for name, (qty, price) in self.cart.items():
            total += qty * price
            row = QHBoxLayout(); row.addWidget(label(f"{name}\n{qty} x Rs. {price}"), 1); row.addWidget(label(f"Rs. {qty*price}", sectionTitle=True)); self.cartBox.layout().addLayout(row)
        self.cartBox.layout().addWidget(label(f"Total: Rs. {total}", sectionTitle=True))
        btn = QPushButton("Review checkout"); btn.setProperty("accent", True); btn.setEnabled(bool(self.cart)); btn.clicked.connect(self.checkout); self.cartBox.layout().addWidget(btn)

    def add_to_cart(self, food):
        name, _cat, price, _stock = food
        if name in self.cart: self.cart[name][0] += 1
        else: self.cart[name] = [1, price]
        self.refresh_cart()

    def checkout(self):
        total = sum(qty * price for qty, price in self.cart.values())
        lines = "\n".join(f"{name} x{qty}: Rs. {qty*price}" for name, (qty, price) in self.cart.items())
        answer = QMessageBox.question(self, "Confirm pickup order", f"{lines}\n\nTotal: Rs. {total}\n\nStock will be verified before the transaction is committed. Confirm order?")
        if answer == QMessageBox.StandardButton.Yes:
            self.cart.clear(); self.refresh_cart(); QMessageBox.information(self, "Order confirmed", "Order #1043 was created and inventory was updated."); self.goto("My orders")

    def build_student_orders(self):
        L = self.studentOrdersLayout; L.addLayout(page_header("Student account", "My orders", "Track active pickup orders and review previous order history."))
        rows = [["#1042", "Grito", "Zinger Roll x2, Cold Coffee x1", "Oct 12", "Rs. 700", badge("Preparing", "warn")], ["#1039", "Tapal", "Chai x2, Samosa x4", "Oct 9", "Rs. 360", badge("Completed", "good")], ["#1031", "Cafe2Go", "Club Sandwich x1", "Oct 4", "Rs. 420", badge("Completed", "good")], ["#1020", "Hobnob", "Pasta x1, Iced Tea x1", "Sep 28", "Rs. 550", badge("Cancelled", "bad")]]
        L.addWidget(make_table(["Order", "Vendor", "Items", "Date", "Total", "Status"], rows, 2)); L.addStretch()

    def build_vendor_dashboard(self):
        L = self.vendorDashboardLayout; L.addLayout(page_header("Grito workspace", "Vendor dashboard", "Manage your menu, monitor stock and keep pickup orders moving.", "+ Add menu item", self.add_item))
        stats = QGridLayout()
        for i, data in enumerate([("Today's orders", "18", "5 currently active"), ("Available items", "12", "of 15 menu items"), ("Low stock", "2", "Action recommended"), ("Completed today", "13", "72% of today's orders")]): stats.addWidget(stat_card(*data), 0, i)
        L.addLayout(stats)
        rows = [["#1042", "Mariam Hanif", "Rs. 700", badge("Preparing", "warn")], ["#1041", "Abdullah Hasan", "Rs. 380", badge("Pending", "neutral")], ["#1038", "Ayesha Noor", "Rs. 250", badge("Ready", "good")]]
        box = card(); box.layout().addWidget(label("Incoming orders", sectionTitle=True)); box.layout().addWidget(make_table(["Order", "Student", "Total", "Status"], rows, 1)); L.addWidget(box); L.addStretch()

    def build_inventory(self):
        L = self.inventoryLayout; L.addLayout(page_header("Grito operations", "Menu and inventory", "Maintain menu items, prices, quantities and low-stock thresholds.", "+ Add item", self.add_item))
        self.inventoryTable = QTableWidget(); L.addWidget(self.inventoryTable); self.refresh_inventory(); L.addStretch()

    def refresh_inventory(self):
        rows = []
        for name, category, price, stock in self.foods:
            kind = "bad" if stock == 0 else "warn" if stock <= 6 else "good"
            state = "Out of stock" if stock == 0 else "Low stock" if stock <= 6 else "Available"
            btn = QPushButton("Edit"); rows.append([name, category, f"Rs. {price}", stock, badge(state, kind), btn])
        replacement = make_table(["Menu item", "Category", "Price", "Stock", "Status", "Actions"], rows, 0)
        layout = self.inventoryLayout; old = self.inventoryTable; index = layout.indexOf(old); layout.replaceWidget(old, replacement); old.deleteLater(); self.inventoryTable = replacement

    def add_item(self):
        dialog = AddItemDialog(self)
        if dialog.exec():
            self.foods.append([dialog.name.text(), dialog.category.currentText(), dialog.price.value(), dialog.stock.value()])
            self.refresh_inventory(); QMessageBox.information(self, "Item added", f"{dialog.name.text()} was added to Grito's menu.")

    def build_incoming_orders(self):
        L = self.incomingOrdersLayout; L.addLayout(page_header("Order operations", "Incoming orders", "Review pickup orders and move each order through preparation."))
        rows = []
        for values in [["#1042", "Mariam Hanif", "Zinger Roll x2, Cold Coffee x1", "Rs. 700", "12:43 PM", "Preparing"], ["#1041", "Abdullah Hasan", "Beef Burger x1", "Rs. 380", "12:39 PM", "Pending"], ["#1038", "Ayesha Noor", "Zinger Roll x1", "Rs. 250", "12:25 PM", "Ready"]]:
            btn = QPushButton("Update status"); btn.clicked.connect(lambda _=False, b=btn: (b.setText("Updated"), b.setEnabled(False)))
            kind = {"Preparing":"warn", "Pending":"neutral", "Ready":"good"}[values[-1]]; rows.append(values[:-1] + [badge(values[-1], kind), btn])
        L.addWidget(make_table(["Order", "Student", "Items", "Total", "Placed", "Status", "Action"], rows, 2)); L.addStretch()

    def build_vendor_profile(self):
        L = self.vendorProfileLayout; L.addLayout(page_header("Vendor settings", "Grito profile and hours", "Keep location, contact information and operating hours accurate."))
        box = card(); form = QFormLayout(); form.setSpacing(12)
        for caption, value in [("Vendor name", "Grito"), ("Contact number", "0300-1234567"), ("Campus location", "Ground Floor, Student Center"), ("Account email", "grito@vendors.habib.edu.pk")]: form.addRow(caption, QLineEdit(value))
        form.addRow("Opening time", QTimeEdit(QTime(8,30))); form.addRow("Closing time", QTimeEdit(QTime(19,0))); box.layout().addLayout(form)
        save = QPushButton("Save profile"); save.setProperty("accent", True); save.clicked.connect(lambda: QMessageBox.information(self, "Saved", "Vendor profile and operating hours were updated.")); box.layout().addWidget(save, 0, Qt.AlignmentFlag.AlignRight)
        L.addWidget(box); L.addStretch()

    def build_admin_dashboard(self):
        L = self.adminDashboardLayout; L.addLayout(page_header("Administrator workspace", "Food Hub overview", "Review vendor onboarding and monitor the campus food-vendor directory.", "Review applications", lambda: self.goto("Vendor applications")))
        stats = QGridLayout()
        for i, data in enumerate([("Approved vendors", "4", "Currently active"), ("Pending review", "2", "Needs attention"), ("Menu items", "47", "Across all vendors"), ("Orders today", "51", "Campus total")]): stats.addWidget(stat_card(*data), 0, i)
        L.addLayout(stats)
        rows = [["Cafe2Go", "Basement, Student Center", "7:00 AM - 6:00 PM", "Oct 11", badge("Pending", "warn")], ["Hobnob", "1st Floor, ADFC", "9:00 AM - 8:00 PM", "Oct 10", badge("Pending", "warn")]]
        L.addWidget(make_table(["Vendor", "Proposed location", "Hours", "Submitted", "Status"], rows, 1)); L.addStretch()

    def build_applications(self):
        L = self.vendorApplicationsLayout; L.addLayout(page_header("Vendor onboarding", "Vendor applications", "Verify account, campus location and operating hours before approval."))
        body = QHBoxLayout(); list_box = card(); list_box.layout().addWidget(label("Applications", sectionTitle=True))
        for name, meta, state in [("Cafe2Go", "Basement, Student Center", "Pending"), ("Hobnob", "1st Floor, ADFC", "Pending"), ("Grito", "Ground Floor, Student Center", "Approved"), ("Tapal", "Courtyard, Student Center", "Approved")]:
            row = QHBoxLayout(); row.addWidget(label(f"{name}\n{meta}"), 1); row.addWidget(badge(state, "warn" if state=="Pending" else "good")); list_box.layout().addLayout(row)
        body.addWidget(list_box, 1)
        detail = card(); detail.layout().addWidget(label("Cafe2Go", pageTitle=True)); detail.layout().addWidget(badge("Pending review", "warn"), 0, Qt.AlignmentFlag.AlignLeft)
        detail.layout().addWidget(label("Contact: 0301-5550198\nEmail: cafe2go@vendors.hu\nLocation: Basement, Student Center\nHours: 7:00 AM - 6:00 PM", subtitle=True))
        actions = QHBoxLayout(); reject = QPushButton("Reject"); approve = QPushButton("Approve vendor"); approve.setProperty("accent", True)
        reject.clicked.connect(lambda: QMessageBox.information(self, "Reason required", "Enter a rejection reason before changing the application status.")); approve.clicked.connect(lambda: QMessageBox.information(self, "Vendor approved", "Cafe2Go is now visible to students."))
        actions.addWidget(reject); actions.addWidget(approve); detail.layout().addLayout(actions); body.addWidget(detail, 1); L.addLayout(body); L.addStretch()

    def build_all_vendors(self):
        L = self.allVendorsLayout; L.addLayout(page_header("Vendor directory", "All food vendors", "Review active, pending and inactive vendor accounts."))
        rows = [["Grito", "Ground Floor, SSC", "8:30 AM - 7:00 PM", "grito@vendors.hu", badge("Approved", "good")], ["Tapal", "Courtyard, SSC", "9:00 AM - 9:00 PM", "tapal@vendors.hu", badge("Approved", "good")], ["Cafe2Go", "Basement, SSC", "7:00 AM - 6:00 PM", "cafe2go@vendors.hu", badge("Pending", "warn")]]
        L.addWidget(make_table(["Vendor", "Location", "Operating hours", "Account email", "Status"], rows, 1)); L.addStretch()

    def goto(self, title):
        for index in range(self.navigationList.count()):
            if self.navigationList.item(index).text() == title:
                self.navigationList.setCurrentRow(index); return


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Habib Food Hub")
    window = HabibFoodHub()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
