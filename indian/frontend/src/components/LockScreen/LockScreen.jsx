import React, { useState } from 'react';
import { Lock, Eye, EyeOff } from 'lucide-react';
import './LockScreen.css';

const VALID_PASSWORDS = ['0210', 'NAVY2026', 'NAVY', '1234', 'ADMIN'];

function LockScreen({ onUnlock }) {
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!password) {
      setError('Please enter password');
      return;
    }

    if (VALID_PASSWORDS.includes(password.trim().toUpperCase())) {
      sessionStorage.setItem('mda_authenticated', 'true');
      onUnlock();
    } else {
      setError('Incorrect password');
      setPassword('');
    }
  };

  return (
    <div className="simple-lock-container">
      <div className="simple-lock-card">
        <div className="lock-icon-circle">
          <Lock size={22} color="#38bdf8" />
        </div>

        <h2>Indian Navy - NMDA</h2>
        <p className="lock-sub">Enter password to access dashboard</p>

        <form onSubmit={handleSubmit} className="simple-lock-form">
          <div className="password-input-group">
            <input
              type={showPassword ? 'text' : 'password'}
              placeholder="Enter Password"
              value={password}
              onChange={(e) => {
                setPassword(e.target.value);
                if (error) setError('');
              }}
              autoFocus
            />
            <button
              type="button"
              className="toggle-eye"
              onClick={() => setShowPassword(!showPassword)}
            >
              {showPassword ? <EyeOff size={16} /> : <Eye size={16} />}
            </button>
          </div>

          {error && <div className="simple-error">{error}</div>}

          <button type="submit" className="login-btn">
            Login
          </button>
        </form>
      </div>
    </div>
  );
}

export default LockScreen;
