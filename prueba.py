from facebook_scraper import get_posts

# Define la URL de la publicación
post_url = "https://www.facebook.com/<UPTCOficial>/posts/<5698394720258939>"

# Obtén la publicación utilizando su URL
posts = get_posts(post_urls=[post_url])

# Itera sobre los resultados y obtén la URL de cada publicación
for post in posts:
    print(post['post_url'])