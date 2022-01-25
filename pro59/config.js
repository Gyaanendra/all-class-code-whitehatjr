import firebase from 'firebase'

var firebaseConfig = {
    apiKey: "AIzaSyAL2RQ4weaSdNM8Jw_XF0bgNtUcD3Htv1c",
    authDomain: "rating-8d55e.firebaseapp.com",
    projectId: "rating-8d55e",
    storageBucket: "rating-8d55e.appspot.com",
    messagingSenderId: "553811291456",
    appId: "1:553811291456:web:0f9ced5fce0798e8bd5ea5"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);

  export default firebase.database();