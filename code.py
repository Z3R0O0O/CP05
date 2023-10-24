 # Validar item_name para evitar injeção de SQL
            if not re.match(r'^[a-zA-Z0-9\s]+$', item_name):
                return redirect(url_for('index', error=4))  # Valor inválido
            try:
                db_cur.execute("SELECT * FROM Movies WHERE name COLLATE NOCASE=?", (item_name,))
                query_result = db_cur.fetchall()
