# **開発中の画面: 掲示板機能とログイン機能**

---

## **1. 掲示板機能（Post API）**
この画面は**投稿データのAPI取得機能**を示しています。Django REST Framework（DRF）を使用して、投稿データをJSON形式で取得するエンドポイントを提供しています。

### **説明**
- **エンドポイント**: `GET /api/posts/`
- **機能**:
  - 投稿の一覧取得（ページネーション機能付き）
  - 各投稿にコメントを含めることで、関連データも同時に取得可能です。

- **JSONレスポンス例**:
   ```json
   {
       "count": 15,
       "next": "http://127.0.0.1:8000/api/posts/?page=2",
       "previous": null,
       "results": [
           {
               "id": 1,
               "title": "Tech Talk",
               "content": "最新の技術動向やプログラミング言語、フレームワークに関するディスカッションのための掲示板です。",
               "author": 1,
               "created_at": "2024-12-09T06:49:06.473623Z",
               "comments": [
                   {
                       "id": 1,
                       "post": 1,
                       "content": "初めてのWebアプリ開発ですが、DjangoとFlaskのどちらがおすすめですか？",
                       "created_at": "2024-12-09T06:49:06.481124Z"
                   }
               ]
           }
       ]
   }


# 開発中の画面　掲示板機能　改修予定
![image](https://github.com/user-attachments/assets/4b1dbcd2-5341-4a01-a8fc-d52998be1608)

# ログイン機能
![image](https://github.com/user-attachments/assets/5037efe7-b07c-43df-b8cd-b29efda02754)
