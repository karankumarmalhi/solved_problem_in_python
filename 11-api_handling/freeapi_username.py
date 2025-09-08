import  requests

def fectech_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

    response = requests.get(url)
    # print(response)

    data = response.json()
    # print(data)

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("Failed to fectch!")

def main():
    try:
       username, country = fectech_random_user()
       print("username:", username)
       print("country:", country)
    except Exception as e:
        print(str(e))
    finally:
        pass


if __name__ == "__main__":
    main()