from haystack import indexes
from reviewInfo.models import ReviewInfo


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    sku = indexes.IntegerField(model_attr='sku')

    def get_model(self):
        return ReviewInfo