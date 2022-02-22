def get_header(machine_db_path):
    with open(machine_db_path, "rb") as f:
        return f.read(30)
    
def get_machine_i(machine_db_path, i, db_has_header=True):
    with open(machine_db_path, "rb") as f:
        c = 1 if db_has_header else 0
        f.seek(30*(i+c))
        return f.read(30)