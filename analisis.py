from facebook_scraper import get_profile

profile_id = '100003853222559' #id de mi perfil personal


profile = get_profile(profile_id, cookies="facebook.com_cookies.txt",   friends=True) 


for key, value in profile.items():
    print(key, ": ", value) #veremos que informacion nos devuelve la consulta