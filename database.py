import mysql.connector

# Database configuration
db = mysql.connector.connect(
    host="localhost", user="root", password="Test1234", database="restaurateur"
)
cursor = db.cursor()
