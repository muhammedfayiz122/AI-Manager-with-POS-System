import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, 
                             QTableWidget, QTableWidgetItem, QGridLayout, QHeaderView, QLineEdit)
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
        
        # Top - Product Area
        self.product_table = QTableWidget(0, 4)
        self.product_table.setHorizontalHeaderLabels(["Product Name", "Quantity", "Price", "Amount"])
        self.product_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        main_layout.addWidget(self.product_table)
        
        # Bottom - Actions and Payments
        bottom_layout = QGridLayout()
        
        # Payment buttons
        self.create_payment_buttons(bottom_layout)
        
        # Add discount, refund, comment, and customer
        self.create_action_buttons(bottom_layout)
        
        # Bottom right - Subtotal, Tax, Total
        self.create_total_display(bottom_layout)
        
        main_layout.addLayout(bottom_layout)
        
        # Bottom lock, transfer, void order buttons
        self.create_bottom_buttons(main_layout)

    def create_payment_buttons(self, layout):
        # Payment Methods
        payment_methods = ["Cash", "Credit Card", "Debit Card", "Check", "Voucher", "Gift Card"]
        for i, method in enumerate(payment_methods):
            button = QPushButton(method)
            layout.addWidget(button, i // 3, i % 3)
            button.clicked.connect(lambda _, m=method: self.handle_payment(m))
    
    def create_action_buttons(self, layout):
        actions = [("Discount", "F2"), ("Comment", ""), ("Customer", ""), ("Refund", "F9")]
        for i, (action, key) in enumerate(actions):
            button = QPushButton(f"{action} {key}")
            layout.addWidget(button, 2 + (i // 2), i % 2)
            button.clicked.connect(lambda _, a=action: self.handle_action(a))

    def create_total_display(self, layout):
        self.subtotal_label = QLabel("Subtotal: 0.00")
        self.tax_label = QLabel("Tax: 0.00")
        self.total_label = QLabel("<h3>Total: 0.00</h3>")
        
        layout.addWidget(self.subtotal_label, 4, 0)
        layout.addWidget(self.tax_label, 4, 1)
        layout.addWidget(self.total_label, 4, 2)
    
    def create_bottom_buttons(self, layout):
        button_layout = QGridLayout()
        lock_button = QPushButton("Lock")
        transfer_button = QPushButton("Transfer")
        void_order_button = QPushButton("Void Order")
        
        button_layout.addWidget(lock_button, 0, 0)
        button_layout.addWidget(transfer_button, 0, 1)
        button_layout.addWidget(void_order_button, 0, 2)
        
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
