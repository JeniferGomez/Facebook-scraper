from facebook_scraper import get_posts

post_url = "https://www.facebook.com/zuck/posts/10112681480907401"
post = get_posts(post_urls=[post_url], pages=1).__next__()

print(post)
