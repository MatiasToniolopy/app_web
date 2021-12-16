import sqlite3 as sqlite3



def createdata():
    
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    
    cursor.execute("""CREATE TABLE paciente (
        [id] INTEGER PRIMARY KEY,
        [nombre] VARCHAR(255),
        [edad] INTEGER,
        [dni] INTEGER,
        [habitacion] INTEGER,
        [diagnostico] VARCHAR(200)
    );
    """)
    conn.commit()
    conn.close()

def insert():
    
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    data = [
        ('matias toniolo', 35, 31910606, 2, 'neumonia')
    ]
    
    cursor.executemany("INSERT INTO paciente VALUES (NULL,?,?,?,?,?)", data)
    conn.commit()
    conn.close()
    
    
    
    
    
    
    
if __name__ == '__main__':
    createdata()
    insert()