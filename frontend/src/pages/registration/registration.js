import React, { useState } from "react";
import './registration.css';

export const Registration = (props) => {
    const [email, setEmail] = useState('');
    const [pass, setPass] = useState('');
    const [name, setName] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(email);
    }

    return (
        <div className="auth-form-container">
            <h2>Регистрация</h2>
            <form className="registration-form" onSubmit={handleSubmit}>
                <input className="input-registr" value={email} onChange={(e) => setEmail(e.target.value)} type="email" placeholder="email" id="email" name="email" />
                <input className="input-registr" value={name} onChange={(e) => setName(e.target.value)} id="name" placeholder="имя"  name="name" />
                <input className="input-registr" value={pass} onChange={(e) => setPass(e.target.value)} type="password" placeholder="password" id="password" name="password" />
                <button type="submit">создать</button>
            </form>
            <button className="link-btn" onClick={() => props.onFormSwitch('login')}>войти</button>
        </div>
    )
}