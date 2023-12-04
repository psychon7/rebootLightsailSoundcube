import requests
import boto3
import time

def is_website_up(url):
    try:
        response = requests.get(url, timeout=10)
        return response.status_code == 200
    except requests.RequestException:
        return False

def reboot_lightsail_instance(instance_name):
    client = boto3.client('lightsail')
    client.reboot_instance(instanceName=instance_name)

def main():
    website_url = 'https://soundcube.shop'
    lightsail_instance_name = 'SoundCubeNew'

    while True:
        if not is_website_up(website_url):
            reboot_lightsail_instance(lightsail_instance_name)
            print(f"Instance {lightsail_instance_name} rebooted.")
        time.sleep(1800)  # Wait for 30 minutes before next check

if __name__ == "__main__":
    main()
