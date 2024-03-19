import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def make_tor_request2(url, user_agent, keywords, num_links_to_crawl):
    # Set the headers for the request
    headers = {'User-Agent': user_agent}

    # Initialize the visited set and the link queue
    visited = set()
    data_for_urls = {}

    # Get the list of keywords to search for
    keywords = keywords.split(',')

    # Set the Tor proxy
    proxies = {'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}

    # Initialize the link queue
    queue = [url]

    # Crawl the links
    while queue:
        # Get the next link in the queue
        link = queue.pop(0)

        # Skip the link if it has already been visited
        if link in visited:
            continue

        # Send the request to the URL through Tor
        response = requests.get(link, headers=headers, proxies=proxies)

        # Parse the response
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all links on the page
        links = soup.find_all('a')

        # Add any links that contain the keywords to the queue
        for a in links:
            href = a.get('href')
            full_url = urljoin(link, href)
            if any(keyword in href for keyword in keywords):
                queue.append(full_url)

        # Add the link to the visited set
        visited.add(link)

        # Store data for the URL
        data_for_urls[link] = {
            'title': soup.title.string,
            'text_content': soup.get_text(),
            'links': [urljoin(link, a.get('href')) for a in links],
        }

        # Check if the number of visited links has reached the limit
        if len(visited) >= num_links_to_crawl:
            break

    # Print data for all visited links
    print('Data for visited links:')
    for link, data in data_for_urls.items():
        print(f"URL: {link}")
        print(f"Title: {data['title']}")
        print(f"Text Content:\n{data['text_content']}")
        print(f"Links on the page: {data['links']}")
        print("\n" + "="*50 + "\n")


if __name__=='__main__':
	# Get the starting URL from the user
	url = input('Enter the URL of the dark web site you want to extract data from: ')

	# Set the user agent to use for the request
	user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'

	# Get the list of keywords to search for
	keywords = input('Enter a list of keywords to search for, separated by commas: ')

	# Set the number of links to crawl
	num_links_to_crawl = 100

	# Make the Tor request
	make_tor_request2(url, user_agent, keywords, num_links_to_crawl)
