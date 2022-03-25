#!/bin/sh
#https://stackoverflow.com/questions/16501663/macs-say-command-to-mp3
# https://gist.github.com/mculp/4b95752e25c456d425c6
# https://stackoverflow.com/questions/1489800/getting-list-of-mac-text-to-speech-voices-programmatically

pandoc -f markdown+tex_math_single_backslash+yaml_metadata_block -o publish/panman.md -F panflute publish/manuscript_v0_.md
say -f publish/panman.md -o publish/sound.aiff -v Allison
lame -m m publish/sound.aiff publish/sound.mp3
rm publish/sound.aiff
say 'done' 
