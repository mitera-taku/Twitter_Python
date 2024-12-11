import React, { useEffect, useState } from 'react';
import axios from 'axios';

const TweetList = () => {
  const [tweets, setTweets] = useState([]);

  useEffect(() => {
    const fetchTweets = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/posts/');
        setTweets(response.data);
      } catch (error) {
        console.error('エラーが発生しました', error);
      }
    };
    fetchTweets();
  }, []);

  return (
    <div>
      <h1>ツイート一覧</h1>
      <ul>
        {tweets.map((tweet) => (
          <li key={tweet.id}>{tweet.title}</li>
        ))}
      </ul>
    </div>
  );
};

export default TweetList;
