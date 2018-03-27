import os
import json
import facebook

if __name__ == '__main__':
    token = os.environ.get("FACEBOOK_TEMP_TOKEN")
    graph =facebook.graphAPI(taken)
    profile = graph.get_object('me',fields='name,location{location}')
    posts=graph.get_connection('me','posts')
    print(json.dumps(profile,indent=4))
    
while true :
    try:
        with open ('my_posts.json1','a')as f:
            for post in posts['data']:
                f.write(json.dumps(post)+"\n")
                posts = requests.get(posts['paging']['next'].json()
    except keyerror:
         #if no more pages
          break
