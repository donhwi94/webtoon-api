

def get_WebtoonDetailSerializer(Webtoon, pk=webtoon_id):
    webtoon = get_object_or_404(Webtoon, pk=webtoon_id)
    serializer = WebtoonDetailSerializer(webtoon)
    return serializer
