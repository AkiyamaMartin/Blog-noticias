from django import template
import re

register = template.Library()

@register.filter
def youtube_embed_url(url):
    if not url:
        return ''
    # Extraer el VIDEO_ID de URLs como https://www.youtube.com/watch?v=VIDEO_ID o https://youtu.be/VIDEO_ID
    match = re.search(r'(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]+)', url)
    if match:
        video_id = match.group(1)
        return f'https://www.youtube.com/embed/{video_id}'
    return ''