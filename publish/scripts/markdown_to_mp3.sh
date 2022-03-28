#!/bin/sh
# https://stackoverflow.com/questions/16501663/macs-say-command-to-mp3
# https://gist.github.com/mculp/4b95752e25c456d425c6
# https://stackoverflow.com/questions/1489800/getting-list-of-mac-text-to-speech-voices-programmatically

# # would use modified version of cleanup_filter.py here ..
# pandoc -f markdown+tex_math_single_backslash+yaml_metadata_block -o publish/panman.md -F panflute publish/manuscript_v0_.md

python publish/scripts/latex_to_speech.py
say -f publish/gen/mv0_auto_audio.md -o publish/gen/sound.aiff -v Allison
echo '... converting to mp3 ...'
lame -m m publish/gen/sound.aiff publish/outputs/mv0_auto.mp3
rm publish/gen/sound.aiff
say 'done creating audio transcript' 
