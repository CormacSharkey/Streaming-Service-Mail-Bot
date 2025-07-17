# Create the html body with the movie and tv releases lists
def html_body_chunk(movie_releases, tv_releases, cell_height, row_len):
    column = 0

    html = """\
    <html>
    <body>
    <center>
    <h1>Movies</h1>
    <div style="display: table;">
    """

    for item in movie_releases:
        if column == row_len:
            column = 0
            html += """\
            </div>
            <div style="display: table;">
            """

        html += __html_item_chunk(item, cell_height)
        column += 1

    html += """\
    </div>
    <h1>TV</h1>
    """

    for item in tv_releases:
        if column == row_len:
            column = 0
            html += """\
            </div>
            <div style="display: table;">
            """

        html += __html_item_chunk(item, cell_height)
        column += 1

    html += """\
    </div>
    </div>
    </center>
    </body>
    </html>
    """

    return html


def __html_item_chunk(item, cell_height):
    if item.season_number == None:
        return f"""\
        <div style="display: table-cell;">
        <center>
        <img src={item.poster_url} height={cell_height}px style="border: 3px solid black;" alt="Poster Image">
        <p style="width: 260px; background-color:powderblue; border: 3px solid black;">
        <b>{item.title}</b><br>
        Type: {item.type}<br>
        Release Date: {item.source_release_date}<br>
        Platform: {item.source_name}<br>
        {item.description}
        </p>
        </center>
        </div>

        """
    else:
        return f"""\
        <div style="display: table-cell;">
        <center>
        <img src={item.poster_url} height={cell_height}px style="border: 3px solid black;" alt="Poster Image">
        <p style="width: 260px; background-color:powderblue; border: 3px solid black;">
        <b>{item.title}</b><br>
        Type: {item.type}<br>
        Season Number: {item.season_number}<br>
        Release Date: {item.source_release_date}<br>
        Platform: {item.source_name}<br>
        {item.description}
        </p>
        </center>
        </div>

        """
