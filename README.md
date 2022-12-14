# Wayfair Scraper
asdasd
### How it works

There are two approaches to retrieving data from Wayfair using our Scraper API. You can give us a full [**URL**](#url) or pass parameters via the specifically built data source - [**Search**](#search)**.**

### Overview

Below is a quick overview of all the available data `source` values we support with Wayfair.

| Source           | Description                      | Structured data                                                      |
| ---------------- | -------------------------------- | -------------------------------------------------------------------- |
| `wayfair`        | Submit any Wayfair URL you like. | Depends on the URL (refer [**here**](#url) to learn more). |
| `wayfair_search` | Wayfair search result pages.     | No.                                                                  |

### URL

The `wayfair` source is designed to retrieve content from various Wayfair URLs. Instead of sending multiple parameters, you can provide us with a direct URL to your preferred Wayfair page. We do not strip any parameters or alter your URLs in any other way.

This data source also supports parsed data (structured data in JSON format), as long as the URL submitted is for Wayfair Search (SERP page). If we cannot confirm this is a SERP page request, a failure message will be returned.

#### Query parameters

| Parameter                                                 | Description                                                                                                                                    | Default Value |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| <mark style="background-color:green;">**`source`**</mark> | Data source. [**More info**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#source).                                              | `wayfair`     |
| <mark style="background-color:green;">**`url`**</mark>    | Direct URL (link) to Wayfair page                                                                                                              | -             |
| `user_agent_type`                                         | Device type and browser. The full list can be found [**here**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#user_agent_type). | `desktop`     |
| `callback_url`                                            | URL to your callback endpoint. [**More info.**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#callback_url)                     | -             |

&#x20;   <mark style="background-color:green;"></mark> - required parameter

#### Python code example

In this example, we make a request to retrieve a result for a URL.

```python
import requests
from pprint import pprint

# Structure payload.
payload = {
    'source': 'wayfair',
    'url': 'https://www.wayfair.com/keyword.php?keyword=sofa'
}

# Get response.
response = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('user', 'pass1'),
    json=payload,
)

# Instead of response with job status and results url, this will return the
# JSON response with results.
pprint(response.json())
```

Code examples for other languages can be found [**here.**](https://github.com/oxylabs/wayfair-scraper/tree/main/code%20examples/URL)

### Search

The `wayfair_search` source is designed to retrieve Wayfair Search results (SERP).

#### Query parameters

| Parameter                                                 | Description                                                                                                                                    | Default Value    |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| <mark style="background-color:green;">**`source`**</mark> | Data source. [**More info**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#source).                                              | `wayfair_search` |
| <mark style="background-color:green;">**`query`**</mark>  | UTF-encoded keyword                                                                                                                            | -                |
| `start_page`                                              | Starting page number                                                                                                                           | `1`              |
| `pages`                                                   | Number of pages to retrieve                                                                                                                    | `1`              |
| `limit`                                                   | Number of results to retrieve in each page. Available values: `24`, `48`, `96`                                                                 | `48`             |
| `user_agent_type`                                         | Device type and browser. The full list can be found [**here**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#user_agent_type). | `desktop`        |
| `callback_url`                                            | URL to your callback endpoint. [**More info.**](https://developers.oxylabs.io/scraper-apis/getting-started/api-reference/global-parameter-values#callback_url)                     | -                |

&#x20;   <mark style="background-color:green;"></mark> - required parameter

#### Python code example

In the code example below, we make a request to retrieve `4` `wayfair.com` search results pages, starting from page #`2`, for search term `sofa`.

```python
import requests
from pprint import pprint


# Structure payload.
payload = {
    'source': 'wayfair_search',
    'query': 'sofa',
    'start_page': 2,
    'pages': 4
}


# Get response.
response = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('user', 'pass1'),
    json=payload,
)

# Print prettified response to stdout.
pprint(response.json())
```
Code examples for other languages can be found [**here.**](https://github.com/oxylabs/wayfair-scraper/tree/main/code%20examples/Search)
