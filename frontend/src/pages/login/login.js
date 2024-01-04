import React, { useState } from "react";
import '../registration/registration.css'

export const Login = (props) => {
    const [email, setEmail] = useState('');
    const [pass, setPass] = useState('');
    
    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(email);
    }

    return (
        <div className="auth-form-container">
            <h2>Вход</h2>
            <form className="login-form" onSubmit={handleSubmit}>
                <input className="input-registr" value={email} onChange={(e) => setEmail(e.target.value)} type="email" placeholder="email" id="email" name="email" />
                <input className="input-registr" value={pass} onChange={(e) => setPass(e.target.value)} type="password" placeholder="password" id="password" name="password" />
                <button type="submit">войти</button>
            </form>
            <button className="link-btn" onClick={() => props.onFormSwitch('registration')}>зарегистрироваться</button>
        </div>
    )
}