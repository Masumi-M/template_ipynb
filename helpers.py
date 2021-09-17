# @title Helper Functions
import datetime
import inspect
import json
from matplotlib.figure import Figure
import os
from pandas import DataFrame
import pickle
from shutil import Error


# @markdown - add_ending_slash(directory: str) -> str
def add_ending_slash(directory: str) -> str:
    """add_ending_slash function

    Args:
        directory (str): directory that you want to add ending slash

    Returns:
        str: directory name with slash at the end

    Examples:
        >>> add_ending_slash("./data")
        "./data/"
    """
    if directory[-1] != "/":
        directory = directory + "/"
    return directory


# @markdown - add_leading_zero(number: int, digit_num: int = 2) -> str
def add_leading_zero(number: int, digit_num: int = 2) -> str:
    """add_leading_zero function

    Args:
        number (int): number that you want to add leading zero
        digit_num (int): number of digits that you want fill up to. Defaults to 2.

    Returns:
        str: number that has the leading zero

    Examples:
        >>> add_leading_zero(5, 3)
        "005"
    """
    return str(number).zfill(digit_num)


# @markdown - date_now() -> str
def date_now() -> str:
    """date_now function

    Returns:
        str: date info in string style

    Examples:
        >>> print(date_now())
        20210523_113015
    """
    now = datetime.datetime.now()
    return "{0:%Y%m%d_%H%M%S}".format(now)


# @markdown - load_pickle(file_name_with_path: str) -> object
def load_pickle(file_name_with_path: str) -> object:
    """load_pickle function

    Args:
        file_name_with_path (str): file name of the pickle

    Returns:
        object: the variable data that you want to load

    Examples:
        >>> sample = load_pickle('./data/sample.pkl')
    """
    try:
        with open(file_name_with_path, 'rb') as f:
            return pickle.load(f)
    except:
        print(":( Failed to load " + file_name_with_path + ' .')
        return Error()


# @markdown - make_dir(dir_name: str) -> None
def make_dir(dir_name: str) -> None:
    """make_dir function

    Args:
        dir_name (str): directory name which you want to make

    Examples:
        >>> make_dir("./data")
    """
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


# @markdown - print_var(var: any) -> None
def print_var(var: any) -> None:
    """print_var function

    Args:
        var (any): variable that you want to print

    Examples:
        >>> print_var(sample)
        "sample: 10"
    """
    for fi in reversed(inspect.stack()):
        names = [
            var_name for var_name, var_val in fi.frame.f_locals.items()
            if var_val is var
        ]
        if len(names) > 0:
            print(f'{names[0]}: {var}')
            return


# @markdown - read_json(file_name_with_path: str) -> dict
def read_json(file_name_with_path: str) -> dict:
    """read_json function

    Args:
        file_name_with_path (string): file name of json with path

    Returns:
        dict: json dict data

    Examples:
        >>> print(read_json("./name.json"))
        {name: "Masumi"}
    """
    json_open = open(file_name_with_path, 'r')
    return json.load(json_open)


# @markdown - save_df_as_html(df: DataFrame, file_name_with_path: str) -> None
def save_df_as_html(df: DataFrame, file_name_with_path: str) -> None:
    """save_df_as_html function

    Args:
        df (DataFrame): dataframe data that you want to export
        file_name_with_path (str): file name of html with path

    Examples:
        >>> save_df_as_html(sample_df, "./results/sample.html")
    """
    html_template = """
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    </head>
    <body>
        <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
        <div class="container">
            {table}
        </div>
    </body>
</html>
"""
    table = df.to_html(classes=["table", "table-bordered", "table-hover"])
    html = html_template.format(table=table)
    with open(file_name_with_path, "w") as f:
        f.write(html)


# @markdown - save_figure(fig: Figure, file_name_with_path: str, custom_dpi: int = 100) -> None
def save_figure(fig: Figure,
                file_name_with_path: str,
                custom_dpi: int = 100) -> None:
    """save_figure function

    Args:
        fig (Figure): figure data that you want to save
        file_name_with_path (str): file name with path
        custom_dpi (int): custom dpi value. Defaults to 100.

    Examples:
        >>> save_figure(fig, "./data/sample.png", 200)
    """
    make_dir(os.path.dirname(file_name_with_path))
    fig.savefig(file_name_with_path, dpi=custom_dpi, pad_inches='tight')


# @markdown - save_pickle(file_name_with_path: str, save_data: object) -> None
def save_pickle(file_name_with_path: str, save_data: object) -> None:
    """save_pickle function

    Args:
        file_name_with_path (str): file name of the pickle with path,
        save_data (object): the variable data that you want to save

    Examples:
        >>> save_pickle('./data/sample.pkl', sample)
    """
    make_dir(os.path.dirname(file_name_with_path))
    try:
        with open(file_name_with_path, 'wb') as f:
            pickle.dump(save_data, f)
    except:
        print(":( Failed to save " + file_name_with_path + ' .')
