def html_chunk(item, cell_height):
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