curl --user user:pass1 'https://realtime.oxylabs.io/v1/queries' -H "Content-Type: application/json"
 -d '{"source": "wayfair_search", "query": "sofa", "start_page": 2, "pages": 4}'