import folium
import requests
import math
import os
from dotenv import load_dotenv

load_dotenv()

# Function to get route from OpenRouteService
def get_route(api_key, start_coords, end_coords):
    url = "https://api.openrouteservice.org/v2/directions/driving-car"
    headers = {"Authorization": api_key}
    params = {
        "start": f"{start_coords[1]},{start_coords[0]}",
        "end": f"{end_coords[1]},{end_coords[0]}"
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

# Function to calculate the bearing between two points
def calculate_bearing(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Calculate the bearing using the formula
    dlon = lon2 - lon1
    x = math.sin(dlon) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dlon)
    initial_bearing = math.atan2(x, y)

    # Convert the bearing from radians to degrees and normalize to 0-360
    initial_bearing = math.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360
    return compass_bearing

# Function to get sharp turns or dangerous points along the route
def find_dangerous_points(route_coords, threshold=45):
    dangerous_points = []
    
    # Loop through the route and calculate the bearing between consecutive points
    for i in range(1, len(route_coords)-1):
        lat1, lon1 = route_coords[i-1]
        lat2, lon2 = route_coords[i]
        lat3, lon3 = route_coords[i+1]
        
        # Calculate bearing between previous and current point, and current and next point
        bearing1 = calculate_bearing(lat1, lon1, lat2, lon2)
        bearing2 = calculate_bearing(lat2, lon2, lat3, lon3)
        
        # Calculate the difference between the bearings
        bearing_diff = abs(bearing2 - bearing1)
        if bearing_diff > threshold:  # If the turn is sharper than the threshold
            dangerous_points.append(route_coords[i])  # Add the dangerous point
    
    return dangerous_points

def GetMap(From, To):
    # Input: Source and destination coordinates
    source_lat = float(From[0])
    source_lon = float(From[1])
    destination_lat = float(To[0])
    destination_lon = float(To[1])

    # OpenRouteService API key
    api_key = os.environ["ORS_API_KEY"]

    # Fetch route data
    route_data = get_route(api_key, (source_lat, source_lon), (destination_lat, destination_lon))

    if route_data:
        # Extract route geometry
        coordinates = route_data['features'][0]['geometry']['coordinates']
        
        # Convert coordinates to (latitude, longitude) format for folium
        route_coords = [(lat, lon) for lon, lat in coordinates]

        # Find dangerous points (sharp turns)
        dangerous_points = find_dangerous_points(route_coords)

        # Create map centered at the source
        m = folium.Map(location=[source_lat, source_lon], zoom_start=12)

        # Add blue route to map (main route)
        folium.PolyLine(route_coords, color="blue", weight=5, opacity=0.8).add_to(m)

        

        # Add markers for source and destination
        folium.Marker(location=[source_lat, source_lon], popup="Source", icon=folium.Icon(color="green")).add_to(m)
        folium.Marker(location=[destination_lat, destination_lon], popup="Destination", icon=folium.Icon(color="red")).add_to(m)

        

        # Save map to an HTML file
        m.save("static/route_map.html")
        print("Map saved as 'static/route_map.html'. Open this file to view the route.")
        return True
    else:
        print("Failed to fetch the route data.")
        return False
