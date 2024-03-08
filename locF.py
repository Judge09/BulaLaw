import time
import asyncio
import winrt.windows.devices.geolocation as geolocation
from geopy.geocoders import Nominatim

# Gets the location
async def get_location():
    try:
        geolocator = geolocation.Geolocator()
        position = await geolocator.get_geoposition_async()
        latitude = position.coordinate.point.position.latitude
        longitude = position.coordinate.point.position.longitude
        return latitude, longitude
    except Exception as e:
        print(f"Error getting location: {e}")
        return None

def main():

    loop = asyncio.get_event_loop()

    while True:
        location = loop.run_until_complete(get_location())

        if location:
            print(f"Latitude: {location[0]}, Longitude: {location[1]}")

            # Reverse geocoding using geopy
            geolocator = Nominatim(user_agent="User_Locator")
            location_info = geolocator.reverse(location, language='en').raw

            # Extract and print just the city
            city = location_info.get('address', {}).get('city', 'Unknown')
            print(f"City: {city}")
    
            with open('location_geo.txt', 'a') as file:
                # Write the current location and a newline character
                file.write(f'{city}\n')

        else:
            print("Unable to get location.")
        # Wait for a specified time before getting the location again
        time.sleep(5)

if __name__ == "__main__":
    main()
