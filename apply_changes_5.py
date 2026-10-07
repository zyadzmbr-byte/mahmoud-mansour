import os
import glob
import re

directory = r"d:\محمود منصور"

# 1. Update text and images
text_replacements = {
    "فارس الضاد": "محمود منصور",
    "عماد سعدون": "محمود منصور",
    "logo.5.jpg": "logo.jpg",
    "hero.5.jpg": "hero.jpg",
    "fares eddad": "mahmoud mansour"
}

extensions = ["*.html", "*.js", "*.css"]

for ext in extensions:
    for filepath in glob.glob(os.path.join(directory, ext)):
        # Try reading with utf-8 first
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            encoding = 'utf-8'
        except UnicodeDecodeError:
            try:
                with open(filepath, 'r', encoding='utf-16') as f:
                    content = f.read()
                encoding = 'utf-16'
            except UnicodeDecodeError:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                encoding = 'utf-8'
        
        new_content = content
        for old, new in text_replacements.items():
            new_content = new_content.replace(old, new)
            
        if new_content != content:
            with open(filepath, 'w', encoding=encoding) as f:
                f.write(new_content)
            print(f"Updated {os.path.basename(filepath)}")

# 2. Update firebase-init.js
firebase_init_path = os.path.join(directory, "firebase-init.js")
firebase_content = """import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";
import { getStorage } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-storage.js";

const firebaseConfig = {
  apiKey: "AIzaSyBf3A0vLgSu7rzkpRRHTgh_jp6lldOJ3WU",
  authDomain: "mahmoud-mansour-3e486.firebaseapp.com",
  projectId: "mahmoud-mansour-3e486",
  storageBucket: "mahmoud-mansour-3e486.firebasestorage.app",
  messagingSenderId: "75783061395",
  appId: "1:75783061395:web:68e4aa23a739f30d0b7266"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const auth = getAuth(app);
const storage = getStorage(app);

export { db, auth, storage };
"""
with open(firebase_init_path, 'w', encoding='utf-8') as f:
    f.write(firebase_content)
print("Updated firebase-init.js")

