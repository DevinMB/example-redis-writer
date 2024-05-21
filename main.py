from vault_service import authenticate_vault, get_redis_credentials
from redis_service import write_to_redis_hashset


def main():
    try:
        vault_client = authenticate_vault()
        role = "write"
        redis_username, redis_password = get_redis_credentials(vault_client, role)
        
        mapping = {
            "thing1" : "is a thing",
            "thing2" : "is another thing"
        }

        write_to_redis_hashset(redis_username, redis_password, 'test:category4', mapping)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
