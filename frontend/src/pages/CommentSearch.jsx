import React, { useState } from "react";
import axios from "axios";

const CommentSearch = () => {
  const [query, setQuery] = useState("");
  const [postId, setPostId] = useState("");
  const [results, setResults] = useState([]);
  const [error, setError] = useState("");

  const handleSearch = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:8000/api/comments/search/", {
        params: {
          q: query,
          post_id: postId,
        },
      });
      setResults(response.data); // 結果をセット
      setError("");
    } catch (err) {
      setError("検索に失敗しました。");
    }
  };

  return (
    <div style={styles.container}>
      <h1>コメント検索</h1>
      <input
        type="text"
        placeholder="検索キーワード"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        style={styles.input}
      />
      <input
        type="text"
        placeholder="投稿ID (任意)"
        value={postId}
        onChange={(e) => setPostId(e.target.value)}
        style={styles.input}
      />
      <button onClick={handleSearch} style={styles.button}>
        検索
      </button>
      {error && <p style={styles.error}>{error}</p>}
      <ul>
        {results.map((comment) => (
          <li key={comment.id}>
            {comment.comment} (投稿ID: {comment.post}, 作成日時: {comment.created_at})
          </li>
        ))}
      </ul>
    </div>
  );
};

const styles = {
  container: {
    padding: "20px",
    fontFamily: "Arial, sans-serif",
  },
  input: {
    margin: "10px 0",
    padding: "10px",
    width: "300px",
    fontSize: "16px",
  },
  button: {
    padding: "10px 20px",
    fontSize: "16px",
    backgroundColor: "#007bff",
    color: "#fff",
    border: "none",
    borderRadius: "5px",
    cursor: "pointer",
  },
  error: {
    color: "red",
  },
};

export default CommentSearch;
