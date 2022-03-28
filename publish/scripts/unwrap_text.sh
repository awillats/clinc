# undoes textwrapping introduced by pandoc
# (?<!\n)\n\w matches mid-paragraph newlines 
# for testing: in vim, try `gqq` to wrap selection, then run this command to `undo`
python publish/scripts/pyrex.py '(?<!\n)\n(\w)' ' \1' $1 $2
