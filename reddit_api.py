import praw

reddit = praw.Reddit(
    client_id="9vMN_rGTdCDceB34_pdBWw",
    client_secret="-wLfXTd5EJhC5Fxpa1n5Ay81s_U2Pw",
    password="forteststhanku",
    user_agent="Person",
    username="Mikaaaa_a",
)

for submission in reddit.subreddit("anime").search("Naruto"):
    print(submission.title)

subm = reddit.subreddit("test").submit("Test Submission", url="https://reddit.com")
comment = subm.reply(body="Hello!")

comment.delete()
subm.delete()
