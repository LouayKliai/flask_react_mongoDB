// // RegisterPage.js
// import React, { useState } from 'react';
// import axios from 'axios';

// function Register() {
//     const [username, setUsername] = useState('');
//     const [password, setPassword] = useState('');

//     const handleSubmit = async (e) => {
//         e.preventDefault();
//         try {
//             const response = await axios.post('/register', { username, password });
//             console.log(response.data.message);
//             // Rediriger l'utilisateur vers une page de connexion ou une page de confirmation
//         } catch (error) {
//             console.error('Erreur lors de l\'inscription :', error.response.data.message);
//         }
//     };

//     return (
//         <div>
//             <h2>Inscription</h2>
//             <form onSubmit={handleSubmit}>
//                 <div>
//                     <label>Nom d'utilisateur:</label>
//                     <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} required />
//                 </div>
//                 <div>
//                     <label>Mot de passe:</label>
//                     <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
//                 </div>
//                 <button type="submit">S'inscrire</button>
//             </form>
//         </div>
//     );
// }

// export default Register;


import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';

function Register() {
  return (
    <Form>
      <Form.Group as={Row} className="mb-3" controlId="formPlaintextEmail">
        <Form.Label column sm="2">
          Email
        </Form.Label>
        <Col sm="10">
          <Form.Control plaintext readOnly defaultValue="email@example.com" />
        </Col>
      </Form.Group>

      <Form.Group as={Row} className="mb-3" controlId="formPlaintextPassword">
        <Form.Label column sm="2">
          Password
        </Form.Label>
        <Col sm="10">
          <Form.Control type="password" placeholder="Password" />
        </Col>
      </Form.Group>
    </Form>
  );
}

export default Register;