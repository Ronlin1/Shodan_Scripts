import shodan
SHODAN_API_KEY = "your API key"

api = shodan.Shodan(SHODAN_API_KEY)

try:
    # Search Shodan
    results = api.search('apache')
    total_results = results['total']
#     print(results)

    # Show the results
    print('Total results found: {}'.format(total_results))

    matches = results['matches']
    for result in matches:
        print('IP: {}'.format(result['ip_str']))
        print(result['data'])
        print('')
except shodan.APIError as e:
    print('Error: {}'.format(e))
