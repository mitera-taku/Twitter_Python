import React, { useEffect, useState } from 'react';
import axios from 'axios';

const MediaList = () => {
  const [mediaPosts, setMediaPosts] = useState([]);

  useEffect(() => {
    const fetchMediaPosts = async () => {
      const response = await axios.get('http://127.0.0.1:8000/api/media-posts/');
      setMediaPosts(response.data);
    };
    fetchMediaPosts();
  }, []);

  return (
    <div>
      <h1>メディア一覧</h1>
      {mediaPosts.map((post) => (
        <div key={post.id}>
          <h2>{post.title}</h2>
          <p>{post.description}</p>
          {post.image && <img src={`http://127.0.0.1:8000${post.image}`} alt={post.title} style={{ width: '300px' }} />}
          {post.video && (
            <video width="300" controls>
              <source src={`http://127.0.0.1:8000${post.video}`} type="video/mp4" />
            </video>
          )}
        </div>
      ))}
    </div>
  );
};

export default MediaList;
