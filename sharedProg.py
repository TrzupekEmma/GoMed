def add_rating(conn, prescription, pharmacy, rating):
    # insert table statement
    sql = " INSERT INTO availabilityReport(prescription,pharmacy,rating) VALUES(?,?,?)"
    
    # Create  a cursor
    cur = conn.cursor()

    # execute the INSERT statement
    inp=(prescription,pharmacy,rating,)
    cur.execute(sql,inp)

    # commit the changes
    conn.commit()

    # get the id of the last inserted row
    return cur.lastrowid

