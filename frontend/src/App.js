import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './pages/Login';
import TweetList from './pages/TweetList';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/tweets" element={<TweetList />} />
      </Routes>
    </Router>
  );
};

export default App;
