from pathlib import Path
from typing import Union, List

import re

def traverse_dir_tree_with_validations(
    item_path: Path,
    format_for_level: dict,
    is_root: bool = True,
    errors=[],
    parent: Path | None = None,
):
    # list comprehension to get all the visible directories and files inside current dir path thus we can ignore .DS_Store, cache/meta or OS/System generated folders and files
    
    if is_root:
        contents = [item_path]
    else:
        contents = [
            item
            for item in sorted(item_path.iterdir())
            if not item.name.startswith(".") and item.name != "__MACOSX"
        ]
        
    # pprintpath(contents)
    for path in contents:
        pprintpath(path)
        result = match_iname_with_format(path, format_for_level)
        print(f"RESULT FOR MATCH ---> {result} \n\n")
        if path.is_dir():
            traverse_dir_tree_with_validations(
                path, result[-1], is_root=False, parent=item_path
            )
            
def pprintpath(item : Path | List[Path]):
    if not isinstance(item, list):
        final_items = [item]
    else:
        final_items = item
    for i in final_items:
        itype = "DIR" if i.is_dir() else "FILE" 
        print(f" ==> {i.name} ({itype}) \n")

# dispatcher function
def match_iname_with_format(item,format: Union[dict,str,list]):
    if isinstance(format,dict):
        return match_iname_with_format_dict(item,format)
    return match_iname_with_format_dict_other(item,format)

# handler for dict format type    
def match_iname_with_format_dict(item,format):
    matched = False
    is_regex_matched = False
    re_match = None
    error = None
    
    # checking absolute match
    absmatch = format.get(item.name,False)
    
    if not absmatch:
        # checking for a regex based match on the item name
        regex_dict = re.compile("|".join(format))
        matches = re.findall(regex_dict, item.name)
        if len(matches) == 0:
            error = "Error1"
        elif len(matches) > 1:
            error = "Error2"
        else:
            re_match= matches[0]
            is_regex_matched = matched = True
            
            # Searching for the specific pattern (key of dict) that iname matches to
            for pattern, child in format.items():
                if re.match(pattern, re_match):
                    absmatch = child
                    break
    else:
        matched = True
        
    return matched, (is_regex_matched, re_match), error, absmatch

# handler for other format types
def match_iname_with_format_dict_other(item,format):
    matched = False
    is_regex_matched = False
    re_match = None
    error = None
    
    # checking absolute match
    absmatch = item.name == format
    
    if not absmatch:
        # checking for a regex based match on the item name
        regex_dict = re.compile(format)
        matches = re.findall(regex_dict, item.name)
        if len(matches) == 0:
            error = "Error1"
        elif len(matches) > 1:
            error = "Error2"
        else:
            re_match= matches[0]
            is_regex_matched = matched = True
    else:
        matched = True

    return matched, (is_regex_matched, re_match), error, absmatch            