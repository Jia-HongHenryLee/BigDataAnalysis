# BigDataAnalysis
## DataAnalysisHW1-the twitter's data Crawler
*   **Environment** <br/>
(1) ubuntu 14.04 <br/>
(2) Anaconda Installer for Linux 64-bit Python 2.7<br/>
(3) Java8<br/>
(4) Spark release 1.5.2
*   **Python API**<br/>
(1) Python Twitter library ($pip install twitter)
*   **Keyword-A Movie**<br/>
(1) twitterdata16412001.json - #movie <br/>
(2) twitterdata16413001.json - a 
*   **JSON format** <br/>
```json
{
   "contributors": "使用者物件的集合",
   "truncated": "內文是否有裁減",
   "text": "文字內容",
   "is_quote_status": "是否被引用",
   "in_reply_to_status_id": "是否顯示被回覆的Tweet的ID",
   "id": "這篇Tweet的ID",
   "favorite_count": "like 數",
   "entities":
   {
      "symbols": ["hashtag的功能，$表示"],
      "user_mentions": ["有否tag到其他Twitter user"],
      "hashtags": ["被解析出來的hashtag"],
      "urls": ["包含Tweet的網址"],
   },
   "retweeted": "是否有被其他Twitter使用者分享",
   "coordinates": "發文位置",
   "source": "提到的網址",
   "in_reply_to_screen_name": "如果這篇Tweet為回覆別人的Tweet，會顯示原Tweet名稱",
   "in_reply_to_user_id": "如果這篇Tweet為回覆別人的Tweet，會顯示原Tweet的使用者ID",
   "retweet_count": "被分享的次數",
   "id_str": "Tweet ID",
   "favorited": "是否有被其他已驗證的使用者按like",
   "user":
   {
       "follow_request_sent": "是否有已驗證的使用者要求追蹤這位使用者",
       "has_extended_profile": "是否有額外的profile",
       "profile_use_background_image": "是否同意可以使用背景圖片",
       "default_profile_image": "是否有上傳照片",
       "id": "user id",
       "profile_background_image_url_https": "背景圖片的連結",
       "verified": "是否有通過Email驗證",
       "profile_text_color": "使用的的字體顏色",
       "profile_image_url_https": "大頭貼的連結",
       "profile_sidebar_fill_color": "側邊欄位的背景顏色",
       "entities": "Entity會提供metadata以及有關於這篇Tweet的其他資訊",
       "followers_count": "追蹤post文者的人數",
       "profile_sidebar_border_color": "側邊Bar的背景顏色",
       "id_str": "user id",
       "profile_background_color": "側邊欄位的邊框顏色",
       "listed_count": "post文者所擁有的list數量",
       "is_translation_enabled": "是否允許翻譯",
       "utc_offset": "與GMT標準時間的時差",
       "statuses_count": "發出的Tweet數量",
       "description": "post文者簡介",
       "friends_count": "追蹤其他使用者的數量",
       "location": "座標位置",
       "profile_link_color": "連結顏色",
       "profile_image_url": "照片的網址",
       "following": "是否有被其他已驗證的使用者追蹤",
       "geo_enabled": "是否同意將座標位置顯示於照片上",
       "profile_banner_url": "banner的連結",
       "profile_background_image_url": "背景圖片的連結",
       "screen_name": "視窗名稱",
       "lang": "顯示介面的語言",
       "profile_background_tile": "是否顯示背景圖片的連結",
       "favourites_count": "喜歡的Tweet數量",
       "name": "顯示的名稱",
       "notifications": "是否同意收到SMS的更新通知",
       "url": "post文者所提供的連結",
       "created_at": "post文者註冊帳號的時間",
       "contributors_enabled": "是否有連結contributor mode",
       "time_zone": "時區",
       "protected": "是否有選擇保護他們的Tweet",
       "default_profile": "是否使用預設的圖片",
       "is_translator": "是否有參與幫助翻譯Twitter的文",
   },
   "geo": "座標位置",
   "in_reply_to_user_id_str": "如果這篇Tweet為回覆別人的Tweet，會顯示被回覆的Tweet的作者ID",
   "possibly_sensitive": "是否可能為不好的文",
   "lang": "Tweet文章的語系",
   "created_at": "發出Tweet的時間",
   "in_reply_to_status_id_str": "如果這篇Tweet為回覆別人的Tweet，會顯示被回覆的Tweet的標題",
   "place": "是否有與某個地方連結",
   "metadata": 
   {
        "iso_language_code": "網站使用的語系",
        "result_type": "Tweet的型態",
   }
}
```
