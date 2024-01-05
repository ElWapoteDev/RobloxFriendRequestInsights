import requests
import json
import time
import sys

def get_page(roblox_securty_cookie: str, cursor_: str = ""):
    url_peticiones_amistad = f'https://friends.roblox.com/v1/my/friends/requests?limit=18&cursor={cursor_}'

    try:
        requests_headers = {
            'Cookie': roblox_securty_cookie,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
        }

        peticion_solicitudes_amistad = requests.get(url=url_peticiones_amistad, headers=requests_headers).text
        decoded_utf_text = peticion_solicitudes_amistad.encode('utf-8')
        json_data = json.loads(decoded_utf_text)

        with open('output.json', 'w', encoding='utf-8') as file:
            json.dump(json_data, file, ensure_ascii=False, indent=4)

        return True, json_data
    except Exception as err:
        return False, err

def get_player_follower_count(player_id: str):
    url_follower_endpoint = f"https://friends.roblox.com/v1/users/{player_id}/followers/count"

    try:
        request_ = requests.get(url=url_follower_endpoint).json()
        return True, request_['count']
    except Exception as err:
        return False, err


def iterate_roblox_friend_pages(roblox_securty_cookie: str):
    next_page_cursor = ''
    follower_list = []
    verified_list = []
    plr_count = 0

    while next_page_cursor is not None:
        succ, this_friend_page = get_page(roblox_securty_cookie=roblox_securty_cookie, cursor_=next_page_cursor)
        if not succ:
            print(this_friend_page)
            break

        next_page_cursor = this_friend_page['nextPageCursor']

        for index, player_ in enumerate(this_friend_page['data']):
            
            player_name = player_['name']
            player_id = player_['id']
            player_is_verified = player_['hasVerifiedBadge']

            print(f'{plr_count} | Obteniendo a `{player_name}`')

            data = {
                'Name': player_name,
                'UserId': player_id,
            }

            plr_count += 1

            if player_is_verified:
                verified_list.append(data)
                continue

            follower_success, followers = get_player_follower_count(player_id=str(player_id))
            if not follower_success:
                print(followers)
                continue

            print(f'    followers: {followers}')

            data['Followers'] = followers

            follower_list.append(data)

            time.sleep(0.1)
        
        follower_list_sorted = sorted(follower_list, key=lambda x: x.get('Followers', 0), reverse=True)
        with open('follower_list.json', 'w') as json_file:
            json.dump(follower_list_sorted, json_file, indent=4)
        with open('verified_list.json', 'w') as json_file:
            json.dump(verified_list, json_file, indent=4)

def main():
    if len(sys.argv) != 3 or sys.argv[1].lower() != 'start':
        print("Uso: python script.py start <cookie>")
        return

    cookie = sys.argv[2]
    iterate_roblox_friend_pages(cookie)

if __name__ == "__main__":
    main()