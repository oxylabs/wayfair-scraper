# Wayfair Scraper

[![Wayfair ](https://user-images.githubusercontent.com/129506779/249696772-9ae88eb3-404a-445d-8c5a-dd8c2eb3a9d3.png)](https://oxylabs.go2cloud.org/aff_c?offer_id=7&aff_id=877&url_id=102)

[![](https://dcbadge.vercel.app/api/server/eWsVUJrnG5)](https://discord.gg/GbxmdGhZjq)

Gather data from Wayfair effortlessly and in real-time with Oxylabs [Wayfair Scraper](https://oxy.yt/naaH) solution. The simple, explanatory, and brief guide below shows how the Wayfair Scraper works. At the same time, it provides specific code examples that will help you understand and use the scraper hassle-free.

### How it works

To retrieve data from Wayfair, provide us a full URL of your target page.

The `universal_ecommerce` source is designed to retrieve content from various Wayfair URLs. Instead of sending multiple parameters, you can provide us with a direct URL to your preferred Wayfair page. We do not strip any parameters or alter your URLs in any other way.

This data source also supports parsed data (structured data in JSON format) as long as the URL submitted is for Wayfair Search (SERP page). If we cannot confirm this is a SERP page request, a failure message will be returned.

#### Query parameters

| Parameter                                                 | Description                                                                                                                                    | Default Value |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| <mark style="background-color:green;">**`source`**</mark> | Data source.                                             | `universal_ecommerce`     |
| <mark style="background-color:green;">**`url`**</mark>    | Direct URL (link) to Wayfair page                                                                                                              | -             |
| `user_agent_type`                                         | Device type and browser. The full list can be found [**here**](https://developers.oxylabs.io/scraper-apis/e-commerce-scraper-api/features/user-agent-type). | `desktop`     |
| `callback_url`                                            | URL to your callback endpoint. [**More info.**](https://developers.oxylabs.io/scraper-apis/e-commerce-scraper-api/integration-methods/push-pull#callback)                     | -             |

&#x20;   <mark style="background-color:green;"></mark> - required parameter

#### Python code example

In this example, we make a request to retrieve a result for a URL.

```python
import requests
from pprint import pprint

# Structure payload.
payload = {
    'source': 'universal_ecommerce',
    'url': 'https://www.wayfair.com/keyword.php?keyword=sofa'
}

# Get response.
response = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('user', 'pass1'),
    json=payload,
)

# Instead of response with job status and results URL, this will return the
# JSON response with results.
pprint(response.json())
```

Code examples for other languages can be found [**here.**](https://github.com/oxylabs/wayfair-scraper/tree/main/code%20examples/URL)

The code above shows how you can extract data easily with our Wayfair Scraper. Collect specific product information that can range from prices to descriptions and other features, allowing you to make detailed comparisons/calculations with whom you can gain your competitive advantage.

If you have any questions, you can always contact us at hello@oxylabs.io. or via live chat on our website.
