## TikTok API Functionality

Underlying API: [David Teather's TikTokApi](https://github.com/davidteather/TikTok-Api)
> Note: what legal requirements pertain to this library?

### Provided Functions

- [x] General Trending
  * region
  * language

- [x] Hashtag search
  * full info (TBD)
  * associated videos
  
- [x] Users search

- [x] Specific video infomration
  * diggCount - number of likes
  * author
  * sound
  * hashtags
  * stats
  * create_time

- [x] Specific user information
    > Need to include both secUid & userId/id [reference](https://dteather.com/TikTok-Api/docs/TikTokApi/api.html)
  * screenname / username
  * videos posted by the user
    * can filter by "since DATETIME"
  * videos liked by the user (*if* they are public)
    * can filter by "since DATETIME"
  * full information (TBD)

- [ ] No Comments

#### Bonus/Specific
- [x] Sounds search