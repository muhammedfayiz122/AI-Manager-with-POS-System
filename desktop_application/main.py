import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, 
                             QTableWidget, QTableWidgetItem, QGridLayout, QHBoxLayout, QLineEdit, QSpacerItem, QSizePolicy)
from PyQt6.QtCore import Qt

class POS(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("POS System")
        self.setGeometry(100, 100, 900, 600)
        
        # Main layout container
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        
        # Search bar
        search_bar = QLineEdit()
        search_bar.setPlaceholderText("Search products by name")
        main_layout.addWidget(search_bar)
        
        # Main content layout (Products on left, Buttons on right)
        content_layout = QHBoxLayout()
        main_layout.addLayout(content_layout)
        
        # Left side: Product Area + Total display
        product_layout = QVBoxLayout()
        
        self.product_table = QTableWidget(0, 4)
        self.product_table.setHorizontalHeaderLabels(["Product Name", "Quantity", "Price", "Amount"])
        product_layout.addWidget(self.product_table)
        
        # Total display section under the product table
        self.create_total_display(product_layout)
        
        content_layout.addLayout(product_layout, stretch=3)
        
        # Right side: Buttons
        button_layout = QVBoxLayout()
        self.create_payment_buttons(button_layout)
        self.create_action_buttons(button_layout)
        content_layout.addLayout(button_layout, stretch=1)
        
        # Bottom: Lock, Transfer, Void Order buttons
        self.create_bottom_buttons(main_layout)

    def create_payment_buttons(self, layout):
        # Payment Methods
        payment_methods = ["Cash", "Credit Card", "Debit Card", "Check", "Voucher", "Gift Card"]
        for method in payment_methods:
            button = QPushButton(method)
            button.setFixedHeight(40)  # Set consistent button height
            layout.addWidget(button)
            button.clicked.connect(lambda _, m=method: self.handle_payment(m))
    
    def create_action_buttons(self, layout):
        actions = [("Discount", "F2"), ("Comment", ""), ("Customer", ""), ("Refund", "F9")]
        for action, key in actions:
            button = QPushButton(f"{action} {key}")
            button.setFixedHeight(40)  # Set consistent button height
            layout.addWidget(button)
            button.clicked.connect(lambda _, a=action: self.handle_action(a))

    def create_total_display(self, layout):
        # Total display section aligned below the product table
        self.subtotal_label = QLabel("Subtotal: 0.00")
        self.tax_label = QLabel("Tax: 0.00")
        self.total_label = QLabel("<h3>Total: 0.00</h3>")
        
        layout.addWidget(self.subtotal_label)
        layout.addWidget(self.tax_label)
        layout.addWidget(self.total_label)
    
    def create_bottom_buttons(self, layout):
        # Bottom buttons (Lock, Transfer, Void Order)
        button_layout = QHBoxLayout()
        lock_button = QPushButton("Lock")
        transfer_button = QPushButton("Transfer")
        void_order_button = QPushButton("Void Order")
        
        lock_button.setFixedHeight(40)
        transfer_button.setFixedHeight(40)
        void_order_button.setFixedHeight(40)
        
        button_layout.addWidget(lock_button)
        button_layout.addWidget(transfer_button)
        button_layout.addWidget(void_order_button)
        
        layout.addLayout(button_layout)
    
    def handle_payment(self, method):
        print(f"Processing payment with {method}")
    
    def handle_action(self, action):
        print(f"Action: {action}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pos_system = POS()
    pos_system.show()
    sys.exit(app.exec())
