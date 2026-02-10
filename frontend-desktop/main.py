import sys
import os
import requests
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QFileDialog, QMessageBox,
    QTableWidget, QTableWidgetItem, QTabWidget, QScrollArea,
    QGroupBox, QFormLayout, QListWidget, QListWidgetItem, QTextEdit,
    QDialog, QDialogButtonBox
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QFont, QIcon
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
import json

# API Configuration
API_BASE_URL = "http://localhost:8000/api"


class APIClient:
    """API client for backend communication"""
    
    def __init__(self):
        self.session = requests.Session()
        self.base_url = API_BASE_URL
    
    def login(self, username, password):
        """Login user"""
        try:
            response = self.session.post(f"{self.base_url}/auth/login/", json={
                'username': username,
                'password': password
            })
            if response.status_code == 200:
                return True, response.json()
            else:
                return False, response.json().get('error', 'Login failed')
        except requests.exceptions.RequestException as e:
            print(f"Login error: {e}")
            return False, str(e)
    
    def get_datasets(self):
        """Get all datasets"""
        try:
            response = self.session.get(f"{self.base_url}/datasets/")
            response.raise_for_status()
            data = response.json()
            return data.get('results', data) if isinstance(data, dict) else data
        except requests.exceptions.RequestException as e:
            print(f"Error fetching datasets: {e}")
            return []
    
    def get_dataset(self, dataset_id):
        """Get specific dataset"""
        try:
            response = self.session.get(f"{self.base_url}/datasets/{dataset_id}/")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching dataset: {e}")
            return None
    
    def get_summary(self, dataset_id):
        """Get dataset summary"""
        try:
            response = self.session.get(f"{self.base_url}/datasets/{dataset_id}/summary/")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching summary: {e}")
            return None
    
    def upload_dataset(self, file_path, name):
        """Upload CSV dataset"""
        try:
            with open(file_path, 'rb') as f:
                files = {'file': f}
                data = {'name': name}
                response = self.session.post(
                    f"{self.base_url}/datasets/upload/",
                    files=files,
                    data=data
                )
                response.raise_for_status()
                return True, response.json()
        except requests.exceptions.RequestException as e:
            return False, str(e)
    
    def download_report(self, dataset_id, save_path):
        """Download PDF report"""
        try:
            response = self.session.get(
                f"{self.base_url}/datasets/{dataset_id}/report/",
                stream=True
            )
            response.raise_for_status()
            
            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            return True, "Report downloaded successfully"
        except requests.exceptions.RequestException as e:
            return False, str(e)


class LoginWindow(QWidget):
    """Login Window"""
    
    def __init__(self, api_client, on_login_success):
        super().__init__()
        self.api_client = api_client
        self.on_login_success = on_login_success
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle('Login - Chemical Equipment Visualizer')
        self.setFixedWidth(400)
        self.setFixedHeight(300)
        
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(40, 40, 40, 40)
        
        # Title
        title = QLabel('Welcome Back')
        title.setFont(QFont('Arial', 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Subtitle
        subtitle = QLabel('Please sign in to continue')
        subtitle.setStyleSheet("color: #666;")
        subtitle.setAlignment(Qt.AlignCenter)
        layout.addWidget(subtitle)
        
        layout.addStretch()
        
        # Form
        form_layout = QFormLayout()
        form_layout.setSpacing(10)
        
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText('Username')
        self.username_input.setMinimumHeight(35)
        
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText('Password')
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setMinimumHeight(35)
        self.password_input.returnPressed.connect(self.handle_login)
        
        form_layout.addRow(self.username_input)
        form_layout.addRow(self.password_input)
        
        layout.addLayout(form_layout)
        
        layout.addStretch()
        
        # Login Button
        login_btn = QPushButton('Sign In')
        login_btn.setMinimumHeight(40)
        login_btn.setStyleSheet("""
            QPushButton {
                background-color: #3f51b5;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #303f9f;
            }
        """)
        login_btn.clicked.connect(self.handle_login)
        layout.addWidget(login_btn)
        
        self.setLayout(layout)
        
        # Center on screen
        frame_gm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        center_point = QApplication.desktop().screenGeometry(screen).center()
        frame_gm.moveCenter(center_point)
        self.move(frame_gm.topLeft())

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        
        if not username or not password:
            QMessageBox.warning(self, 'Error', 'Please enter username and password')
            return
            
        success, result = self.api_client.login(username, password)
        
        if success:
            self.close()
            self.on_login_success()
        else:
            QMessageBox.critical(self, 'Login Failed', str(result))


class ChartWidget(QWidget):
    """Widget for displaying matplotlib charts"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.figure = Figure(figsize=(8, 6))
        self.canvas = FigureCanvas(self.figure)
        
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)
    
    def plot_bar_chart(self, data, title, xlabel, ylabel):
        """Plot bar chart"""
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        
        labels = list(data.keys())
        values = list(data.values())
        
        bars = ax.bar(labels, values, color='#3f51b5', alpha=0.8)
        ax.set_title(title, fontsize=14, fontweight='bold')
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.grid(axis='y', alpha=0.3)
        
        # Rotate labels if too many
        if len(labels) > 5:
            plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
        
        self.figure.tight_layout()
        self.canvas.draw()
    
    def plot_pie_chart(self, data, title):
        """Plot pie chart"""
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        
        labels = list(data.keys())
        values = list(data.values())
        
        colors = ['#3f51b5', '#667eea', '#ff4081', '#4caf50', '#ff9800', '#9c27b0', '#00bcd4', '#ffeb3b']
        
        ax.pie(values, labels=labels, autopct='%1.1f%%', colors=colors[:len(labels)], startangle=90)
        ax.set_title(title, fontsize=14, fontweight='bold')
        
        self.figure.tight_layout()
        self.canvas.draw()
    
    def plot_multi_bar(self, equipment_data, title):
        """Plot multiple parameters for equipment"""
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        
        # Limit to first 10 equipment
        equipment_data = equipment_data[:10]
        
        names = [eq['equipment_name'][:15] for eq in equipment_data]
        flowrates = [eq['flowrate'] for eq in equipment_data]
        pressures = [eq['pressure'] for eq in equipment_data]
        temperatures = [eq['temperature'] for eq in equipment_data]
        
        x = range(len(names))
        width = 0.25
        
        ax.bar([i - width for i in x], flowrates, width, label='Flowrate', color='#3f51b5', alpha=0.8)
        ax.bar(x, pressures, width, label='Pressure', color='#ff4081', alpha=0.8)
        ax.bar([i + width for i in x], temperatures, width, label='Temperature', color='#4caf50', alpha=0.8)
        
        ax.set_title(title, fontsize=14, fontweight='bold')
        ax.set_xlabel('Equipment')
        ax.set_ylabel('Value')
        ax.set_xticks(x)
        ax.set_xticklabels(names, rotation=45, ha='right')
        ax.legend()
        ax.grid(axis='y', alpha=0.3)
        
        self.figure.tight_layout()
        self.canvas.draw()


class MainWindow(QMainWindow):
    """Main application window"""
    
    def __init__(self, api_client):
        super().__init__()
        self.api_client = api_client
        self.current_dataset = None
        self.init_ui()
        self.load_datasets()
    
    def init_ui(self):
        self.setWindowTitle('Chemical Equipment Visualizer')
        self.setGeometry(100, 100, 1200, 800)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QVBoxLayout()
        
        # Header
        header = QHBoxLayout()
        title = QLabel('🧪 Chemical Equipment Visualizer')
        title.setFont(QFont('Arial', 18, QFont.Bold))
        header.addWidget(title)
        header.addStretch()
        
        main_layout.addLayout(header)
        
        # Tab widget
        self.tabs = QTabWidget()
        
        # Dashboard tab
        self.dashboard_tab = self.create_dashboard_tab()
        self.tabs.addTab(self.dashboard_tab, 'Dashboard')
        
        # Upload tab
        self.upload_tab = self.create_upload_tab()
        self.tabs.addTab(self.upload_tab, 'Upload Dataset')
        
        # Visualization tab
        self.viz_tab = self.create_visualization_tab()
        self.tabs.addTab(self.viz_tab, 'Visualization')
        
        main_layout.addWidget(self.tabs)
        
        central_widget.setLayout(main_layout)
    
    def create_dashboard_tab(self):
        """Create dashboard tab"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Refresh button
        refresh_btn = QPushButton('🔄 Refresh Datasets')
        refresh_btn.clicked.connect(self.load_datasets)
        refresh_btn.setMaximumWidth(200)
        layout.addWidget(refresh_btn)
        
        # Dataset list
        self.dataset_list = QListWidget()
        self.dataset_list.itemClicked.connect(self.on_dataset_selected)
        layout.addWidget(QLabel('All Datasets:'))
        layout.addWidget(self.dataset_list)
        
        widget.setLayout(layout)
        return widget
    
    def create_upload_tab(self):
        """Create upload tab"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Instructions
        instructions = QLabel('Upload a CSV file with columns: Equipment Name, Type, Flowrate, Pressure, Temperature')
        instructions.setWordWrap(True)
        layout.addWidget(instructions)
        
        # File selection
        file_layout = QHBoxLayout()
        self.file_path_label = QLabel('No file selected')
        file_layout.addWidget(self.file_path_label)
        
        browse_btn = QPushButton('Browse...')
        browse_btn.clicked.connect(self.browse_file)
        file_layout.addWidget(browse_btn)
        
        layout.addLayout(file_layout)
        
        # Dataset name
        layout.addWidget(QLabel('Dataset Name:'))
        self.dataset_name_input = QLineEdit()
        self.dataset_name_input.setPlaceholderText('Enter dataset name')
        layout.addWidget(self.dataset_name_input)
        
        # Upload button
        upload_btn = QPushButton('Upload Dataset')
        upload_btn.setMinimumHeight(40)
        upload_btn.setStyleSheet("""
            QPushButton {
                background-color: #4caf50;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        upload_btn.clicked.connect(self.handle_upload)
        layout.addWidget(upload_btn)
        
        layout.addStretch()
        
        widget.setLayout(layout)
        return widget
    
    def create_visualization_tab(self):
        """Create visualization tab"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Dataset info
        self.viz_info_label = QLabel('Select a dataset from the Dashboard to view visualizations')
        self.viz_info_label.setFont(QFont('Arial', 12))
        layout.addWidget(self.viz_info_label)
        
        # Download report button
        self.download_report_btn = QPushButton('📄 Download PDF Report')
        self.download_report_btn.clicked.connect(self.download_report)
        self.download_report_btn.setEnabled(False)
        self.download_report_btn.setMaximumWidth(200)
        layout.addWidget(self.download_report_btn)
        
        # Charts container
        charts_widget = QWidget()
        charts_layout = QVBoxLayout()
        
        # Type distribution chart
        self.type_chart = ChartWidget()
        charts_layout.addWidget(QLabel('Equipment Type Distribution:'))
        charts_layout.addWidget(self.type_chart)
        
        # Parameter comparison chart
        self.param_chart = ChartWidget()
        charts_layout.addWidget(QLabel('Parameter Comparison:'))
        charts_layout.addWidget(self.param_chart)
        
        charts_widget.setLayout(charts_layout)
        
        # Scroll area for charts
        scroll = QScrollArea()
        scroll.setWidget(charts_widget)
        scroll.setWidgetResizable(True)
        layout.addWidget(scroll)
        
        widget.setLayout(layout)
        return widget
    
    def load_datasets(self):
        """Load datasets from API"""
        datasets = self.api_client.get_datasets()
        self.dataset_list.clear()
        
        for dataset in datasets:
            item_text = f"{dataset['name']} - {dataset['total_count']} equipment"
            item = QListWidgetItem(item_text)
            item.setData(Qt.UserRole, dataset)
            self.dataset_list.addItem(item)
    
    def on_dataset_selected(self, item):
        """Handle dataset selection"""
        dataset = item.data(Qt.UserRole)
        dataset_id = dataset['id']
        
        # Fetch full dataset details
        full_dataset = self.api_client.get_dataset(dataset_id)
        
        if full_dataset:
            self.current_dataset = full_dataset
            self.update_visualizations()
            self.tabs.setCurrentIndex(2)  # Switch to visualization tab
    
    def update_visualizations(self):
        """Update visualization charts"""
        if not self.current_dataset:
            return
        
        dataset = self.current_dataset
        
        # Update info label
        self.viz_info_label.setText(
            f"Dataset: {dataset['name']} | "
            f"Equipment: {dataset['total_count']} | "
            f"Avg Flowrate: {dataset['avg_flowrate']:.2f} | "
            f"Avg Pressure: {dataset['avg_pressure']:.2f} | "
            f"Avg Temperature: {dataset['avg_temperature']:.2f}°C"
        )
        
        # Enable download button
        self.download_report_btn.setEnabled(True)
        
        # Plot type distribution
        self.type_chart.plot_pie_chart(
            dataset['equipment_types'],
            'Equipment Type Distribution'
        )
        
        # Plot parameter comparison
        if dataset.get('equipment'):
            self.param_chart.plot_multi_bar(
                dataset['equipment'],
                'Parameter Comparison (First 10 Equipment)'
            )
    
    def browse_file(self):
        """Browse for CSV file"""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            'Select CSV File',
            '',
            'CSV Files (*.csv)'
        )
        
        if file_path:
            self.file_path_label.setText(file_path)
            
            # Auto-fill dataset name
            if not self.dataset_name_input.text():
                file_name = os.path.basename(file_path).replace('.csv', '')
                self.dataset_name_input.setText(file_name)
    
    def handle_upload(self):
        """Handle dataset upload"""
        file_path = self.file_path_label.text()
        dataset_name = self.dataset_name_input.text()
        
        if file_path == 'No file selected':
            QMessageBox.warning(self, 'Error', 'Please select a file')
            return
        
        if not dataset_name:
            QMessageBox.warning(self, 'Error', 'Please enter a dataset name')
            return
        
        success, result = self.api_client.upload_dataset(file_path, dataset_name)
        
        if success:
            QMessageBox.information(self, 'Success', 'Dataset uploaded successfully!')
            self.file_path_label.setText('No file selected')
            self.dataset_name_input.clear()
            self.load_datasets()
            self.tabs.setCurrentIndex(0)  # Switch to dashboard
        else:
            QMessageBox.critical(self, 'Upload Failed', f'Upload failed: {result}')
    
    def download_report(self):
        """Download PDF report"""
        if not self.current_dataset:
            return
        
        save_path, _ = QFileDialog.getSaveFileName(
            self,
            'Save PDF Report',
            f"equipment_report_{self.current_dataset['id']}.pdf",
            'PDF Files (*.pdf)'
        )
        
        if save_path:
            success, message = self.api_client.download_report(
                self.current_dataset['id'],
                save_path
            )
            
            if success:
                QMessageBox.information(self, 'Success', f'Report saved to {save_path}')
            else:
                QMessageBox.critical(self, 'Error', f'Failed to download report: {message}')


def main():
    """Main application entry point"""
    app = QApplication(sys.argv)
    
    # Set application style
    app.setStyle('Fusion')
    
    # Create API client
    api_client = APIClient()
    
    # Define success callback
    def on_login_success():
        global main_window
        main_window = MainWindow(api_client)
        main_window.show()
    
    # Show login window first
    login_window = LoginWindow(api_client, on_login_success)
    login_window.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
