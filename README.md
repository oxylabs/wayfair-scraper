# Wayfair Scraper

[![Wayfair ](https://user-images.githubusercontent.com/129506779/249696772-9ae88eb3-404a-445d-8c5a-dd8c2eb3a9d3.png)](https://oxylabs.go2cloud.org/aff_c?offer_id=7&aff_id=877&url_id=102)


Gather data from Wayfair effortlessly and in real-time with Oxylabs Wayfair Scraper solution. The simple, explanatory, and brief guide below shows how the Wayfair Scraper works. At the same time, it provides specific code examples that will help you understand and use the scraper hassle-free.

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

The code above shows how you can extract data easily with our Wayfair Scraper. Collect specific product information that can range from prices to descriptions and other features, allowing you to make detailed comparisons/calculations with whom you can gain your competitive advantage.

If you have any questions, you can always contact us at hello@oxylabs.io. or via live chat on our website.
