import webbrowser

import pandas as pd
import requests



def generate_html(dataframe: pd.DataFrame):
    # get the table HTML from the dataframe
    table_html = dataframe.to_html(table_id="table")
    # construct the complete HTML with jQuery Data tables
    html = f"""
    <html>
    <header>
        <link href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.min.css" rel="stylesheet">
    </header>
    <body>
    {table_html}
    <script src="https://code.jquery.com/jquery-3.6.0.slim.min.js" integrity="sha256-u7e5khyithlIdTpu22PHhENmPcRdFiHRjhAuHcs05RI=" crossorigin="anonymous"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>
    <script>
        $(document).ready( function () {{
            $('#table').DataTable({{
                // paging: false,    
                // scrollY: 400,
            }});
        }});
    </script>
    </body>
    </html>
    """
    # return the html
    return html


if __name__ == "__main__":
    url = 'https://api.artic.edu/api/v1/artworks'

    headers = {
        'Accept': 'application/json',
        'Content-type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=[])
    myjson = response.json()

    data = myjson['data']

    ourdata = []
    ourdata.append(list(data[0].keys()))

    for x in data:
        ourdata.append(list(x.values()))

    df = pd.DataFrame(ourdata)
    print(df)
    html = generate_html(df)
    # write the HTML content to an HTML file
    open("index.html", "w", encoding='UTF8').write(html)
    # open the new HTML file with the default browser
    webbrowser.open("index.html")