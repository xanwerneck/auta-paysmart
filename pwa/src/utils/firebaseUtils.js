import firebase from 'firebase/app'
import 'firebase/firestore';
import 'firebase/auth';

const firebaseConfig = {
    apiKey: "AIzaSyDG1r-98WFuLkvnVSKgS4gZYO6IM4BktpM",
    authDomain: "auta-paysmart.firebaseapp.com",
    projectId: "auta-paysmart",
    storageBucket: "auta-paysmart.appspot.com",
    messagingSenderId: "1038057013732",
    appId: "1:1038057013732:web:9c304930da3e64f75647f1"
};

export const firebaseImpl = firebase.initializeApp(firebaseConfig);
export const firebaseDatabase  = firebase.firestore();
export const firebaseAuth = firebase.auth()