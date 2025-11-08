---
source_url: "https://tds.s-anand.net/#/nominatim-api-with-python"
---

## Nominatim API with Python

[**[Image Description]**: Here's a detailed description of the image:

1.  **Image Content:** The image is a static slide or presentation page, likely from an educational video or online course. It contains text elements and branding associated with IIT Madras.

2.  **Key Elements & Text:**
    *   **Title:** "Get the data: Nominatim - Open Street Maps" is the main title, indicating the topic is retrieving data using Nominatim, which is associated with Open Street Maps.
    *   **Course Information:** "Course: TOOLS IN DATA SCIENCE" indicates the course context.
    *   **Instructor Information:** "INSTRUCTOR - ANAND S" and "Tutorial Instructor - MAHESH BALAN U" credits the instructors.
    *   **IIT Madras Branding:** The logo of IIT Madras along with "IIT Madras" and "ONLINE DEGREE" indicates the source of the presentation.

3.  **Purpose & Educational Value:**
    *   The slide introduces the topic of data acquisition, specifically using Nominatim, a tool related to Open Street Maps. This suggests the presentation will cover how to obtain geospatial data for analysis or applications.
    *   The context of "Tools in Data Science" implies the tutorial is aimed at teaching data science techniques and tools.

4.  **Technical Details:**
    *   The combination of Nominatim and Open Street Maps suggests the tutorial will likely focus on retrieving location-based data (e.g., addresses, coordinates, place names) from the Open Street Maps database using the Nominatim service.
    *   Depending on the intended learning objectives, it may explore methods of extracting street maps information or coordinates.

*Original image: ![Nominatim Open Street Map with Python](https://i.ytimg.com/vi_webp/f0PZ-pphAXE/sddefault.webp)*](https://youtu.be/f0PZ-pphAXE)

You'll learn how to get the latitude and longitude of any city from the Nominatim API.

- **Introduction to Nominatim**: Understand how Nominatim, from OpenStreetMap, works similarly to Google Maps for geocoding.
- **Installation and Import**: Learn to install and import [geopy](https://geopy.readthedocs.io/) and [nominatim](https://nominatim.org/).
- **Using the Locator**: Create a locator object using Nominatim and set up a user agent.
- **Geocoding an Address**: Use `locator.geocode` to input an address (e.g., Eiffel Tower) and fetch geocoded data.
- **Extracting Data**: Access detailed information like latitude, longitude, bounding box, and accurate address from the JSON response.
- **Classifying Locations**: Identify the type of place (e.g., tourism, university) using the response data.
- **Practical Example**: Geocode "IIT Madras" and retrieve its full address, type (university), and other relevant information.

Here are links and references:

- [Geocoding using Nominatim - Notebook](https://colab.research.google.com/drive/1-vvP-UyMjHgBqc-hdsUhm3Bsbgi7oO6g)
- Learn about the [`geocoders` module in the `geopy` package](https://geopy.readthedocs.io/)
- Learn about the [`nominatim` package](https://nominatim.org/release-docs/develop/api/Overview/)
- If you get a HTTP Error 403 from Nominatim, use your email ID or your name instead of "myGeocoder" in `Nominatim(user_agent="myGeocoder")`
