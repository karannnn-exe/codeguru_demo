import sqlite3
import subprocess

def create_database():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)''')
    conn.commit()
    conn.close()

def add_user(username, password):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    # Vulnerable to SQL injection
    c.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")
    conn.commit()
    conn.close()

def run_system_command(command):
    # Vulnerable to command injection
    subprocess.run(command, shell=True)

if __name__ == '__main__':
    create_database()
    add_user('admin', 'admin123')

    # Example usage that can be exploited
    user_input = input("Enter a shell command: ")
    run_system_command(user_input)
