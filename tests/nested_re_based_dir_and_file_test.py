from pathlib import Path
from dirspec import traverse_dir_tree_with_validations

def mock_schema_json_as_dict():
    return {
        "Collectable_Assets": {
            "Collectables_Icons": {"^Collectable_[1-9]$": ".png"},
            "Collectables_Leaderboard": {
                "CommonAssets": ".json",
                "^Leaderboard_[1-9]$": ".bash",
            }
        }
    }
    
def test_using_mock_data(target_dir):
    traverse_dir_tree_with_validations(Path(target_dir),mock_schema_json_as_dict())

if __name__ == "__main__":
    target_dir = "Collectable_Assets"
    test_using_mock_data(target_dir)

