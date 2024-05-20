def get_filetype(filename):
    """
    Extracts filetype from filename extension

    Args:
        filename: target file
    Returns:
        String of filetype
    Raises:
        TypeError if filename is not a string
        ValueError if filename does not contain a period
    """
    if not isinstance(filename, str):
        raise TypeError('Input filename must be a string')
    if '.' not in filename:
        raise ValueError('Input filename must contain a period')

    try:
        filename_split_on_period = filename.split('.')
        filetype = filename_split_on_period[-1]
        return filetype

    except Exception as e:
        print(f'Failed to extract filetype from filename: {e}')
