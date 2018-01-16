SLACK_CHANNEL = '#dmv' # this should be the slack channel which you want to send messages to
URL = 'https://www.dmv.ca.gov/wasapp/foa/findDriveTest.do' # the url for the DMV web form
LOCATIONS = {
    'San Mateo': '130',
    'San Mateo': '129', # the office ID obtained by inspecting the xpath, this is what selenium uses to identify the correct option
    'Redwood City': '109',
    'San Jose': '125',
    'Daly City': '28',
    'Fremont': '41',
    'Santa Clara': '134',
    'Gilroy' : '47',
    'Los Gatos' : '74',
    'Oakland Claremont' : '87',
    'Oakland Colisum' : '88',
    'Sacramento' : '116',
    'Sacramento South' : '117',
    'Capitola' : '15'

}
PROFILE = {
    'first_name': 'Ritvick',
    'last_name': 'Paliwal',
    'mm': '02',
    'dd': '15',
    'yyyy': '1990',
    'dl_number': 'Y3784329',
    'tel_prefix': '669',
    'tel_suffix1': '292',
    'tel_suffix2': '9629'
    # format: (area-code) prefix - lineNumber
}

