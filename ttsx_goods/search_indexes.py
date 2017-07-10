from haystack import indexes
from .models import GoodsInfo


class GoodsInfoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return GoodsInfo

    def index_queryset(self, using=None):
        # 对这个类的所有数据进行全文检索
        return self.get_model().objects.all()
