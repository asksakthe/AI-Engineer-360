import os
import re
import pandas as pd
import yaml
from datetime import datetime

def load_file(filepath, delimiter=','):
    ext = os.path.splitext(filepath)[1].lower()
    if ext == '.csv':
        return pd.read_csv(filepath, delimiter=delimiter)
    elif ext in ['.xls', '.xlsx']:
        return pd.read_excel(filepath)
    else:
        raise ValueError(f"Unsupported file extension: {ext}")

def check_file_presence(filepath):
    return os.path.exists(filepath)

def check_header(df, required_columns):
    return list(df.columns) == required_columns

def check_delimiter(filepath, expected_delimiter=',', sample_lines=5):
    ext = os.path.splitext(filepath)[1].lower()
    if ext != '.csv':
        return True
    with open(filepath, 'r') as file:
        for _ in range(sample_lines):
            line = file.readline()
            if expected_delimiter not in line:
                return False
    return True

def validate_pattern(value, pattern):
    return bool(re.match(pattern, str(value))) if pd.notnull(value) else True

def validate_date_format(value, date_format):
    try:
        if pd.isnull(value):
            return True
        datetime.strptime(str(value), date_format)
        return True
    except:
        return False

def validate_prefix(value, prefix):
    return str(value).startswith(prefix) if pd.notnull(value) else True

def validate_min_value(value, min_val):
    try:
        return float(value) >= min_val if pd.notnull(value) else True
    except:
        return False

def profile_column(col):
    total = len(col)
    nulls = col.isnull().sum()
    distincts = col.nunique(dropna=True)
    min_val = col.min() if pd.api.types.is_numeric_dtype(col) else None
    max_val = col.max() if pd.api.types.is_numeric_dtype(col) else None
    return {"total": total, "nulls": nulls, "distincts": distincts, "min": min_val, "max": max_val}

def structural_validation(file_rule, base_path='data/'):
    filepath = os.path.join(base_path, file_rule["name"])
    result = {"file": file_rule["name"], "file_exists": False, "header_check": False,
              "delimiter_check": True, "record_count_check": False}

    if not check_file_presence(filepath):
        return result
    result["file_exists"] = True

    if not check_delimiter(filepath, file_rule.get("delimiter", ",")):
        result["delimiter_check"] = False
        return result

    try:
        df = load_file(filepath, delimiter=file_rule.get("delimiter", ","))
    except Exception as e:
        result["header_check"] = False
        return result

    if check_header(df, file_rule["required_columns"]):
        result["header_check"] = True
    else:
        return result

    if len(df) > 0:
        result["record_count_check"] = True

    return result, df

def functional_validation(df, file_rule):
    validation_results = {}
    profiles = {}

    for col_name, rules in file_rule["columns"].items():
        col_data = df[col_name] if col_name in df.columns else pd.Series()

        pattern_fail = 0
        date_fail = 0
        prefix_fail = 0
        min_value_fail = 0

        if "pattern" in rules:
            pattern_fail = (~col_data.apply(lambda x: validate_pattern(x, rules["pattern"]))).sum()

        if "format" in rules:
            date_fail = (~col_data.apply(lambda x: validate_date_format(x, rules["format"]))).sum()

        if "prefix" in rules:
            prefix_fail = (~col_data.apply(lambda x: validate_prefix(x, rules["prefix"]))).sum()

        if "min_value" in rules:
            min_value_fail = (~col_data.apply(lambda x: validate_min_value(x, rules["min_value"]))).sum()

        validation_results[col_name] = {
            "pattern_fail_count": pattern_fail,
            "date_fail_count": date_fail,
            "prefix_fail_count": prefix_fail,
            "min_value_fail_count": min_value_fail
        }

        profiles[col_name] = profile_column(col_data)

    return validation_results, profiles

def main():
    with open('config/validation_rules.yaml') as f:
        rules = yaml.safe_load(f)

    for file_rule in rules['files']:
        print(f"\nValidating {file_rule['name']} (Structure)...")
        struct_result, df = structural_validation(file_rule)
        print("Structural Result:", struct_result)

        if all([struct_result[k] for k in ['file_exists', 'header_check', 'delimiter_check', 'record_count_check']]):
            print(f"Functional/Business Rule Validation for {file_rule['name']}:")
            func_result, profiles = functional_validation(df, file_rule)
            print("Functional Result:", func_result)
            print("Profiling:", profiles)
        else:
            print(f"Skipped functional validation due to failed structural checks for {file_rule['name']}.")

if __name__ == "__main__":
    main()
