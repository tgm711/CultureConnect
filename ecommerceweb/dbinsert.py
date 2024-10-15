import sqlite3

def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB(id, name, cost, details, category_id, sid, image_file1, image_file2, image_file3, image_file4, stock):
    try:
        # conn = sqlite3.connect('C:/Users/ruchi/Downloads/EcommerceWebsite-master/EcommerceWebsite-master/ecommerceweb/site1.db')
        conn = sqlite3.connect('C:/Users/ruchi/OneDrive/Desktop/EcommerceWebsite-master - Copy/ecommerceweb/site1.db')
        cursor = conn.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO product
                                  (pid, name, cost, details, category_id, sid, image_file1, image_file2, image_file3, image_file4, stock) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        if image_file1:
            img1 = convertToBinaryData(image_file1)
        else:
            img1=None
        if image_file2:
            img2 = convertToBinaryData(image_file2)
        else:
            img2=None
        if image_file3:
            img3 = convertToBinaryData(image_file3)
        else:
            img3=None
        if image_file4:
            img4 = convertToBinaryData(image_file4)
        else:
            img4=None
        # Convert data into tuple format
        data_tuple = (id, name, cost, details, category_id, sid, img1, img2, img3, img4, stock)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        conn.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("the sqlite connection is closed")

