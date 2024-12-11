import React, { useState } from 'react';
import axios from 'axios';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  const handleLogin = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/login/', {
        username,
        password,
      });
      // ログイン成功時の処理
      localStorage.setItem('token', response.data.token); // トークンを保存
      alert('ログイン成功');
      setErrorMessage('');
    } catch (error) {
      setErrorMessage('ログインに失敗しました。ユーザー名またはパスワードを確認してください。');
    }
  };

  return (
    <div style={styles.container}>
      <h1>ログイン</h1>
      <div style={styles.inputContainer}>
        <input
          type="text"
          placeholder="ユーザー名"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          style={styles.input}
        />
      </div>
      <div style={styles.inputContainer}>
        <input
          type="password"
          placeholder="パスワード"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          style={styles.input}
        />
      </div>
      {errorMessage && <p style={styles.error}>{errorMessage}</p>}
      <button onClick={handleLogin} style={styles.button}>
        ログイン
      </button>
    </div>
  );
};

const styles = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    height: '100vh',
    fontFamily: 'Arial, sans-serif',
  },
  inputContainer: {
    margin: '10px 0',
  },
  input: {
    width: '300px',
    padding: '10px',
    fontSize: '16px',
  },
  button: {
    padding: '10px 20px',
    fontSize: '16px',
    backgroundColor: '#007bff',
    color: '#fff',
    border: 'none',
    borderRadius: '5px',
    cursor: 'pointer',
  },
  error: {
    color: 'red',
    margin: '10px 0',
  },
};

export default Login;
