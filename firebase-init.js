import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
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
