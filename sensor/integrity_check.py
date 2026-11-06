import hashlib
from pathlib import Path


def integrity_check(file_path, hash_file="hash_file.txt"): 

    p = Path(file_path)
    if p.exists(): 
        with p.open("rb") as f: 
            digest = hashlib.file_digest(f, "sha256")
            current_hash = digest.hexdigest()
    else: 
        integrity_report = {
            "error_type": "path file not found", 
            "path": file_path}
        return integrity_report
    

    hash_path = Path(hash_file)
    if hash_path.exists():
        with open(hash_file) as f:
            original_hash = f.readline()
            if current_hash != original_hash:
                integrity_report = {
                    "hash_status": "hash_modified",
                    "original_hash": original_hash,
                    "current_hash": current_hash}
                return integrity_report 
            
            else: 
                integrity_report = {
                    "hash_status": "hash_match", 
                    "original_hash": original_hash, 
                    "current_hash": current_hash}
                return integrity_report 
    
    else: 
        integrity_report = {
            "hash_status": "first_execution", 
            "current_hash": current_hash}
        return integrity_report