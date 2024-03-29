from functools import partial
from pathlib import Path

from langworld_db_data.constants.paths import CONFIG_DIR
from langworld_db_data.featureprofiletools.data_structures import ValueForFeatureProfileDictionary
from langworld_db_data.featureprofiletools.feature_profile_writer_from_dictionary import (  # noqa E501
    FeatureProfileWriterFromDictionary,
)
from langworld_db_data.filetools.csv_xls import read_dicts_from_xls
from langworld_db_data.filetools.json_toml_yaml import read_json_toml_yaml


def convert_from_excel(path_to_input_excel: Path) -> Path:
    """Converts Excel "questionnaire" file (which researchers produce)
    into feature profile in CSV. Returns output path for convenience.

    The most notable difference between input Excel and output CSV
    is that Excel questionnaire has two columns for value name
    (one for 'listed' and one for 'custom'), whereas a CSV file has only one.
    """

    # It is important to always use the current YAML file in conversion,
    # so I did not include path to it into parameters to allow overriding it in tests
    file_with_names = CONFIG_DIR / "excel_sheet_and_column_names.yaml"
    sheet_or_column_name_for_id = read_json_toml_yaml(file_with_names)
    # for mypy
    if not isinstance(sheet_or_column_name_for_id, dict):
        raise TypeError(
            f"File with names of Excel sheet and columns {file_with_names} was supposed"
            " to be read as a dictionary. Please check the file."
        )

    rows = read_dicts_from_xls(
        path_to_file=path_to_input_excel,
        sheet_name=sheet_or_column_name_for_id["sheet_name"],
    )

    def _get_value_from_row(
        column_id: str, row_: dict[str, str], name_for_id: dict[str, str]
    ) -> str:
        """Returns value from column with relevant name.
        Name of column is looked up by `attr` in YAML file."""
        return row_[name_for_id[column_id]]

    value_for_feature_id = {}

    for row in rows:
        _get = partial(_get_value_from_row, row_=row, name_for_id=sheet_or_column_name_for_id)
        feature_id = _get("feature_id")
        value_id = _get("value_id")
        value_type = _get("value_type")

        # I could do without this object but this seems better for coding and
        # readability, especially given that I had already written a method for
        # writing a resulting dict to CSV.
        value_for_feature_id[feature_id] = ValueForFeatureProfileDictionary(
            feature_name_ru=_get("feature_name_ru"),
            value_type=value_type,
            value_id=value_id,
            value_ru=(
                _get("listed_value_ru").removeprefix(f"{value_id}: ")
                if value_type == "listed"
                else _get("custom_value_ru")
            ),
            comment_ru=_get("comment_ru"),
            comment_en=_get("comment_en"),
            page_numbers=_get("page_numbers"),
        )

    output_path = path_to_input_excel.parent / f"{path_to_input_excel.stem}.csv"
    print(f"Saving converted Excel file as {output_path}")
    FeatureProfileWriterFromDictionary.write(
        feature_dict=value_for_feature_id, output_path=output_path
    )
    return output_path

    # FIXME multiple lines get overwritten


if __name__ == "__main__":
    for file in (Path(__file__).parent.resolve() / "input").glob("*.xlsm"):
        print(f"Converting {file.name}")
        convert_from_excel(file)
