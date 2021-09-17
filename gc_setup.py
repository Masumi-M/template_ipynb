from google.colab import files
from google.colab import drive


# @markdown - upload_file_to_google_colab() -> list
def upload_file_to_google_colab() -> list:
    """upload_file_to_google_colab function

    Returns:
        list: list of string with the uploaded file name

    Examples:
        >>> upload_file_to_google_colab()
        ['sample1.csv', 'sample2.csv', 'sample3.csv']
    """
    uploaded = files.upload()
    file_name_list = list()
    for fn in uploaded.keys():
        print(':) Upload completed ("{file_name}" with {data_length} bytes).'.
              format(file_name=fn, data_length=len(uploaded[fn])))
        file_name_list.append(fn)
    return file_name_list


# @markdown - mount_google_drive() -> None
def mount_google_drive() -> None:
    """mount_google_drive function

    Examples:
        >>> mount_google_drive()
    """
    drive.mount('/content/drive')
